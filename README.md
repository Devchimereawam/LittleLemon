# 🍋 Little Lemon Restaurant API

A Django REST Framework capstone project for managing restaurant menu items and table reservations.

---

## 📌 Project Overview

This project provides:

* 🍽️ Menu Management API
* 📅 Table Booking API
* 🔐 User Registration & Authentication
* 🧪 Unit Testing
* 🗄️ MySQL Database Integration
* 🎨 Static Frontend Landing Page

Built with:

* Python
* Django
* Django REST Framework
* Djoser Authentication
* MySQL

---

# 📂 Project Structure

```bash
LittleLemon/
│
├── littlelemon/        # Project settings
├── restaurant/         # Main app
├── templates/          # HTML templates
├── tests/              # Unit tests
├── manage.py
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone <your-github-repo-url>
cd LittleLemon
```

---

## 2️⃣ Create Virtual Environment

### macOS/Linux

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Windows

```bash
python -m venv myenv
myenv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install django
pip install djangorestframework
pip install djoser
pip install mysqlclient
```

---

# 🗄️ Database Configuration

Update the `DATABASES` section inside:

```bash
littlelemon/settings.py
```

Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

---

# 🚀 Run Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

---

# 👤 Create Superuser

```bash
python3 manage.py createsuperuser
```

---

# ▶️ Start Development Server

```bash
python3 manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000/
```

---

# 🔐 Authentication Endpoints

## Register User

```text
/auth/users/
```

## Login

```text
/auth/token/login/
```

## Logout

```text
/auth/token/logout/
```

---

# 🍽️ Menu API Endpoints

## Get All Menu Items

```text
/restaurant/menu/
```

## Get Single Menu Item

```text
/restaurant/menu/<id>/
```

---

# 📅 Booking API Endpoints

## Get All Bookings

```text
/restaurant/booking/tables/
```

## Create Booking

```text
/restaurant/booking/tables/
```

---

# 🧪 Run Unit Tests

```bash
python3 manage.py test
```

---

# 📷 Frontend Features

* Responsive landing page
* Static image rendering
* CSS styling
* Navigation bar
* Promotional hero section

---

# 🔒 Protected APIs

Token Authentication is enabled using:

* Django REST Framework Token Authentication
* Djoser

Use Bearer Token inside:

```text
Authorization: Token <your_token>
```

---

# 🧰 Tools Used

| Tool         | Purpose                 |
| ------------ | ----------------------- |
| Django       | Backend Framework       |
| DRF          | REST APIs               |
| MySQL        | Database                |
| Djoser       | Authentication          |
| Git & GitHub | Version Control         |
| VS Code      | Development Environment |

---

# ✅ Features Implemented

* [x] Django project setup
* [x] MySQL integration
* [x] Menu API
* [x] Booking API
* [x] Authentication
* [x] Static frontend
* [x] Unit tests
* [x] GitHub repository

---

# 👨‍💻 Author

Created by Chimere Awam.

---

# 📄 License

This project is for educational purposes as part of the Meta Back-End Developer Capstone Project.
