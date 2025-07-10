# Inventory Manager

A modern Django web application for managing and purchasing tech inventory items. Features a user-friendly Bootstrap interface, image uploads, shopping cart, checkout, search, filter, and pagination.

## Features
- User authentication (login/logout)
- Add, edit, and delete inventory items (with image upload)
- Category management
- Search and filter items by name and category
- Responsive Bootstrap UI
- Shopping cart: add, remove, and update items
- Checkout process with order saving
- Pagination for item lists
- Admin panel for advanced management
- stripe service api for paiment
- 

## Screenshots
<!-- Add screenshots here -->

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/inventory_manager.git
   cd inventory_manager
   ```
2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Create a superuser (admin):**
   ```sh
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
7. **Access the app:**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
   - Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Usage
- Log in to add, edit, or delete items.
- Use the search bar and filters to find items.
- Add items to your cart and proceed to checkout.
- Manage inventory and orders via the admin panel.

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** Bootstrap 5, HTML5, CSS3
- **Other:** Django Widget Tweaks, Pillow (for images) , stripe (for paiment)


