
# KOMII - Community Complaint System (Backend API)

A Django REST Framework backend for a **Community Complaint Management System** that allows residents to submit complaints, attach images, categorize them, and track status.  
Admins and stakeholders can manage, assign, and report on complaints.

> **Note:** The original **prototype frontend** for this project is available on my GitHub:  
> https://github.com/dulagudeta/KOMII-community-compliant-system-prototype

---

## 📌 Features Implemented

### 1. **User Management with JWT Authentication**
- Custom `users` app for handling user accounts.
- Authentication via **JWT (JSON Web Tokens)** using `djangorestframework-simplejwt`.
- Secure token-based login and refresh tokens.
- Two main roles:
  - **Residents**: Submit complaints.
  - **Stakeholders/Admins**: Manage, assign, and resolve complaints.

---

### 2. **Complaint Management**
- **Complaint Model**:
  - Title, Description, Location, Category.
  - Status: `new`, `in_progress`, `resolved`, `declined`.
  - `reported_by` (complaint submitter).
  - `assigned_to` (optional stakeholder).
  - Auto timestamps for creation & updates.
- **ComplaintImage Model**:
  - Linked to Complaint.
  - Stores uploaded images in `complaint_images/`.

---

### 3. **REST API Endpoints**
All endpoints are JSON-based with no HTML templates.

#### **Authentication**
- `POST /api/token/` → Obtain JWT access and refresh tokens.
- `POST /api/token/refresh/` → Refresh access token.

#### **Complaints**
- `GET /complaints/` → List all complaints.
- `POST /complaints/` → Create a new complaint.
- `GET /complaints/<id>/` → Retrieve a specific complaint.
- `PUT /complaints/<id>/` → Update a complaint.
- `DELETE /complaints/<id>/` → Delete a complaint.

#### **Categories**
- `GET /categories/` → List all categories.
- `POST /categories/` → Create a new category.

#### **Admin Reports**
- `GET /reports/admin/` → View complaint statistics (status count, category count, stakeholder assignment count).
  - **Admin-only access**.

---

### 4. **Technologies Used**
- **Backend Framework**: Django 5.x
- **API Framework**: Django REST Framework (DRF)
- **Authentication**: JWT via `djangorestframework-simplejwt`
- **Database**: SQLite (development), can be switched to PostgreSQL/MySQL
- **Image Handling**: Django's `ImageField` (supports Pillow)

---

## 🛠 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/dulagudeta/KOMII-community-compliant-system-prototype-backend.git
cd KOMII-community-compliant-system-prototype-backend
````

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate     # For Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server

```bash
python manage.py runserver
```

---

## 📂 Project Structure

```
KOMII/
│
├── complaints/
│   ├── models.py          # Complaint & ComplaintImage models
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views & admin reports
│   ├── urls.py            # Complaints API routes
│
├── users/
│   ├── models.py          # Custom user model (if extended)
│   ├── serializers.py     # DRF serializers for user management
│   ├── views.py           # User registration/login endpoints with JWT
│
├── KOMII/
│   ├── settings.py        # Django settings including JWT config
│   ├── urls.py            # Main URL routing
│
├── manage.py
└── requirements.txt
```

---

## 📊 Admin Report Example

Example response from `GET /reports/admin/`:

```json
{
    "status_counts": [
        {"status": "new", "total": 10},
        {"status": "resolved", "total": 5}
    ],
    "category_counts": [
        {"category": "Road", "total": 4},
        {"category": "Electricity", "total": 6}
    ],
    "stakeholder_counts": [
        {"assigned_to__username": "Stakeholder1", "total": 3}
    ]
}
```
---
Developed by [DULA](github.com/dulagudeta)
