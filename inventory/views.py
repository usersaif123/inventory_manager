from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from .forms import ItemForm #type: ignore

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Cart, CartItem, Order, OrderItem
from django.core.paginator import Paginator

# Updated item_list view with search functionality
@login_required
def item_list(request):
    print("item_list view called")
    items = Item.objects.all()  # type: ignore[attr-defined]
    categories = Category.objects.all()  # type: ignore[attr-defined]
    category_id = request.GET.get('category')
    if category_id:
        items = items.filter(category_id=category_id)
    query = request.GET.get('q', '')
    if query:
        items = Item.objects.filter(name__icontains=query)  # type: ignore[attr-defined]

    paginator = Paginator(items, 9)  # 9 items par page (tu peux changer ce nombre)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'inventory/item_list.html', {
        'items': page_obj,
        'categories': categories,
        'query': query,
    })
    
@permission_required('inventory.add_item', raise_exception=True)
@login_required
def item_add(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)  # <-- add request.FILES
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'inventory/item_form.html', {'form': form, 'title': 'Add Item'})

@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)  # <-- add request.FILES
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/item_form.html', {'form': form, 'title': 'Edit Item'})

@permission_required('inventory.delete_item', raise_exception=True)
@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'inventory/item_confirm_delete.html', {'item': item})

@require_POST
@login_required
def bulk_action(request):
    action = request.POST.get('action')
    selected_ids = request.POST.getlist('selected_items')
    if not selected_ids:
        messages.warning(request, "No items selected.")
        return redirect('item_list')

    if action == 'delete':
        from .models import Item  # Ensure Item is imported from the correct location
        Item.objects.filter(id__in=selected_ids).delete()  # type: ignore[attr-defined]
        messages.success(request, f"Deleted {len(selected_ids)} items.")
    # You can add more actions here (e.g., bulk update)
    return redirect('item_list')

@login_required
def purchase_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    user = request.user

    # Only allow viewers (optional: check user group)
    # if not user.groups.filter(name='Viewer').exists():
    #     messages.error(request, "Only viewers can purchase items.")
    #     return redirect('item_list')

    from .models import Cart, CartItem  # Ensure Cart and CartItem are imported from the correct location

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=user)  # type: ignore[attr-defined]

    # Check if the item is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)  # type: ignore[attr-defined]
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"Added another {item.name} to your cart.")
    else:
        messages.success(request, f"Added {item.name} to your cart.")

    # Optionally, decrease item quantity in inventory
    # if item.quantity > 0:
    #     item.quantity -= 1
    #     item.save()

    return redirect('item_list')

@login_required
def cart_view(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user) # type: ignore[attr-defined]
        cart_items = cart.items.select_related('item')
    except Cart.DoesNotExist: # type: ignore[attr-defined]
        cart = None
        cart_items = []

    # Calculate the total price for the cart
    cart_total = sum(item.quantity * item.item.price for item in cart_items)

    return render(request, 'inventory/cart.html', {
        'cart': cart,
        'cart_items': cart_items,
        'cart_total': cart_total,
    })

@login_required
def cart_remove(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart_view')

@login_required
def checkout(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user)  # type: ignore[attr-defined]
        cart_items = cart.items.select_related('item')
    except Cart.DoesNotExist: # type: ignore[attr-defined]
        cart_items = []

    if request.method == 'POST' and cart_items:
        # 1. Create an Order
        order = Order.objects.create(user=user) # type: ignore[attr-defined]
        for cart_item in cart_items:
            item = cart_item.item
            if cart_item.quantity > item.quantity:
                messages.error(request, f"Not enough stock for {item.name}.")
                return redirect('cart_view')
            # 2. Deduct stock
            item.quantity -= cart_item.quantity
            item.save()
            # 3. Save order item
            OrderItem.objects.create( # type: ignore[attr-defined]
                order=order,
                item=item,
                quantity=cart_item.quantity,
                price_at_purchase=item.price
            )
        # 4. Clear cart
        cart.items.all().delete()
        messages.success(request, "Thank you for your purchase!")
        return render(request, 'inventory/checkout_success.html', {'order': order})

    cart_total = sum(item.quantity * item.item.price for item in cart_items)
    return render(request, 'inventory/checkout.html', {
        'cart_items': cart_items,
        'cart_total': cart_total,
    })

