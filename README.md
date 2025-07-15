# Inventory Manager

A modern Django web application for managing and purchasing tech inventory items. Features a user-friendly Bootstrap interface, image uploads, shopping cart, checkout, search, filter, and pagination.

---

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
- Stripe API integration for payments (setup required)

---

## Screenshots

<!-- Add screenshots here (e.g., ![screenshot](path/to/screenshot.png)) -->

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/inventory_manager.git
   cd inventory_manager
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
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
   - Main site: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Usage

- Log in to add, edit, or delete items.
- Use the search bar and filters to find items.
- Add items to your cart and proceed to checkout.
- Manage inventory and orders via the admin panel.

---

## Running Tests

To run the automated tests, use:

```sh
python manage.py test
```

---

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Bootstrap 5, HTML5, CSS3
- **Other:** Django Widget Tweaks, Pillow (for image handling), Stripe (for payments)

---

## Stripe Integration

> **Note:** Stripe integration is included for payment processing. You must add your Stripe API keys to `settings.py` and complete the setup as described in the documentation or code comments.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

[MIT](LICENSE) (or your chosen license)


