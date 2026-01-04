# Movie Review API (ALX Backend Capstone)

A Django + Django REST Framework project for managing movie reviews.  
Users can register, authenticate, and perform CRUD operations on reviews.  
Includes search, filtering, pagination, and optional JWT authentication.

---

## Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/capstone_ALX_backend.git
cd capstone_ALX_backend

Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

### 2. Install Dependencies

pip install -r requirements.txt

## Start Django Project

django-admin startproject movie_review_api_project .
python manage.py startapp reviews


### Configurations

Add Apps in settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'reviews',
]


REST Framework Settings

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',  # optional
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

### Review Model

from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    movie_title = models.CharField(max_length=255, db_index=True)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_title} ({self.rating}/5) by {self.user.username}"


### Migrations

python manage.py makemigrations
python manage.py migrate

## User Management

python manage.py createsuperuser


## Authentication

Log in at: http://127.0.0.1:8000/api-auth/login/


### API Endpoints


/api/users/	POST	Register new user
/api/users/	GET	List users
/api/reviews/	GET	List reviews
/api/reviews/	POST	Create review (auth required)
/api/reviews/{id}/	PUT/PATCH	Update own review
/api/reviews/{id}/	DELETE	Delete own review
/api/reviews/?movie_title=movie_title	GET	Filter reviews by movie
/api/reviews/?rating=5	GET	Filter reviews by rating
/api/reviews/?search=movie_title	GET	Search reviews
/api/reviews/?ordering=-created_at	GET	Sort reviews


TEsting with REST Client 

### Register User
POST http://127.0.0.1:8000/api/users/
Content-Type: application/json

{
  "username": "eddem",
  "email": "eddem@example.com",
  "password": "securepassword123"
}

### Login (JWT)
POST http://127.0.0.1:8000/api/token/
Content-Type: application/json

{
  "username": "eddem",
  "password": "securepassword123"
}

### Create Review
POST http://127.0.0.1:8000/api/reviews/
Authorization: Bearer <ACCESS_TOKEN>
Content-Type: application/json

{
  "movie_title": "Inception",
  "content": "Mind-bending sci-fi masterpiece.",
  "rating": 5
}

### Get Reviews
GET http://127.0.0.1:8000/api/reviews/?movie_title=Inception
