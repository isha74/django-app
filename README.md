# Django Auth API (task1)

A small Django project that provides simple user registration and login API endpoints using Django REST Framework and a `Profile` model for phone numbers.

---

## 🔧 Features

- **User Registration** via `POST /api/register/` (username, email, password, phone)
- **User Login** via `POST /api/login/` (username, password)
- **Profile model** (`accounts.models.Profile`) with `phone` field
- Uses **Django REST Framework** for API endpoints
- Basic HTML templates for registration and login in `accounts/templates/`

---

## 🧩 Stack & Requirements

- Python 3.8+
- Django 5.2.9 (project generated with this version)
- Django REST Framework
- PostgreSQL (configured in `core/settings.py` by default)

> Tip: For a quick local setup you can switch to SQLite in `core/settings.py` by replacing the `DATABASES` entry.

---

## 🚀 Quickstart (Windows - PowerShell)

1. Create a virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
# If you have a requirements.txt
pip install -r requirements.txt
# OR install minimal deps
pip install django djangorestframework psycopg2-binary
```

3. Configure the database:

- The project uses PostgreSQL by default (see `core/settings.py`).
- Create the DB and update `NAME`, `USER`, `PASSWORD`, `HOST`, and `PORT` in `core/settings.py` or set up environment variable handling.

4. Apply migrations and create a superuser:

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

5. Run the development server:

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ — API endpoints are under `/api/`.

---

## 📡 API Endpoints

- **Register**
  - URL: `POST /api/register/`
  - Payload (JSON):
    ```json
    {
      "username": "yourusername",
      "email": "you@example.com",
      "password": "yourpassword",
      "phone": "1234567890"
    }
    ```
  - Response: 201 on success `{ "message": "Registered successfully" }` or error JSON

- **Login**
  - URL: `POST /api/login/`
  - Payload (JSON):
    ```json
    {
      "username": "yourusername",
      "password": "yourpassword"
    }
    ```
  - Response: 200 on success `{ "message": "Login successful" }` or 401 on failure

---

## 🗂 Project Structure (key files)

```
manage.py
core/                # Django project (settings, urls, wsgi/asgi)
accounts/            # App: models, views, serializers, templates
  ├─ templates/
  │   ├─ login.html
  │   └─ register.html
  ├─ models.py       # Profile model
  ├─ views.py        # RegisterAPI, LoginAPI
  └─ serializers.py  # Serializers for Register/Login
```

---

## ✅ Tests

Run the test suite with:

```powershell
python manage.py test
```

---

## 🤝 Contributing

- Feel free to open issues or submit pull requests.
- Improve tests, add environment-driven configuration, or add token-based authentication.

---

## 📄 License

This project does not include a license file. Add a `LICENSE` if you plan to open-source it.

---

If you'd like, I can also add a `requirements.txt`, add environment variable support for settings, or switch the default DB to SQLite for easier local testing. ✨
