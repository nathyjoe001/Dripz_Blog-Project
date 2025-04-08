

# Blog Project API



A RESTful API for a blogging platform built with Django and Django REST Framework. The project includes full CRUD operations for posts and comments, user authentication using JWT, and secure profile access.



## Features



- User registration and login with JWT authentication

- Create, retrieve, update, and delete blog posts

- Commenting system with CRUD operations

- Authenticated users can view and edit their own profiles

- Secure token-based access for protected endpoints



## Technologies Used



- Python 3

- Django

- Django REST Framework

- djangorestframework-simplejwt (JWT Authentication)

- SQLite (default, can be changed to PostgreSQL/MySQL)


## Installation

1. Clone the repository:
2. Install dependencies:
3. Set up your database:
4. Run the development server:
5. startproject blog_project
6. startapp blog, users and comments.
7. register the apps on settings.py
8. create models  and serializers for blog,comments and users
9. create urls.py and update views.py
9. register the users and comments on admin site
11. update to main urls.py 
12. run the migrations
13.  python manage.py runserver

Project Status

This project is actively being developed. Key features like search, pagination, and likes system may be added in the future.

License

This project is open-source and available under the MIT License.