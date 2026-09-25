# Task Tracker Backend API

## Week 4 — Python Backend & Django Fundamentals

This project was developed as part of the ZoyaSofts Internship Training Program — Week 4.

The project demonstrates a Python Django backend for a Task Tracker application and connects the backend API with a React frontend.

## Technologies Used

* Python
* Django
* SQLite
* REST-style API endpoints
* JSON
* React
* JavaScript
* Fetch API
* Postman

## Project Features

The backend provides APIs for:

* Creating tasks
* Viewing all tasks
* Viewing a single task
* Updating tasks
* Deleting tasks

Each task contains:

* Task name
* Description
* Status
* Created date

## API Endpoints

| Method | Endpoint           | Purpose                |
| ------ | ------------------ | ---------------------- |
| GET    | `/api/tasks/`      | Retrieve all tasks     |
| POST   | `/api/tasks/`      | Create a new task      |
| GET    | `/api/tasks/<id>/` | Retrieve a single task |
| PUT    | `/api/tasks/<id>/` | Update a task          |
| DELETE | `/api/tasks/<id>/` | Delete a task          |

## Project Structure

```text
tasktracker-backend/
│
├── manage.py
├── README.md
├── .gitignore
│
├── tasktracker/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── tasks/
    ├── admin.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── migrations/
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd tasktracker-backend
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install django
pip install django-cors-headers
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

The backend will run at:

```text
http://127.0.0.1:8000/
```

## API Testing

The APIs can be tested using Postman or another API testing tool.

## Week 4 Learning Outcomes

This project covers:

* Python backend setup
* Virtual environments
* pip
* Django project structure
* Django applications
* URL routing
* Views
* GET, POST, PUT and DELETE requests
* Request bodies
* Django models
* Migrations
* SQLite database integration
* JSON API responses
* React and Django integration using `fetch()`
* API testing

## Author

Avadhut Banne
