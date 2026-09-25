# Day 5 — Building REST APIs

## Objective

The objective of Day 5 was to build REST APIs using Django, return responses in JSON format, and understand the basic API structure required for the Task Tracker backend.

## Concepts Learned

### 1. REST API

A REST API allows the frontend application to communicate with the backend through HTTP requests.

The main HTTP methods used in the Task Tracker API are:

* GET — Retrieve task information
* POST — Create a new task
* PUT — Update an existing task
* DELETE — Delete a task

### 2. JSON Responses

The Django backend returns API responses in JSON format.

Example:

```json
{
    "success": true,
    "message": "Task created successfully"
}
```

JSON provides a simple format for exchanging data between the React frontend and Django backend.

## Task Tracker API Endpoints

### Get All Tasks

```text
GET /api/tasks/
```

This endpoint retrieves all tasks stored in the database.

### Create a Task

```text
POST /api/tasks/
```

This endpoint creates a new task using JSON request data.

Example request:

```json
{
    "task_name": "Complete Week 4 Backend",
    "description": "Build and test Django Task Tracker API",
    "status": "pending"
}
```

### Get a Single Task

```text
GET /api/tasks/<id>/
```

This endpoint retrieves a specific task using its ID.

### Update a Task

```text
PUT /api/tasks/<id>/
```

This endpoint updates the details of an existing task.

Example request:

```json
{
    "task_name": "Complete Week 4 Backend API",
    "description": "Django Task Tracker API is completed",
    "status": "completed"
}
```

### Delete a Task

```text
DELETE /api/tasks/<id>/
```

This endpoint deletes a specific task from the database.

## Implementation

The API was implemented using Django views and URL routing.

The `Task` model is used to store and retrieve task information from the database.

The backend uses JSON request data for POST and PUT operations and returns JSON responses to the client.

Basic validation and error handling were also implemented for invalid JSON, missing task names, invalid status values, and tasks that do not exist.

## API Testing

The APIs were tested using Postman.

The following operations were successfully tested:

1. GET all tasks
2. POST a new task
3. GET a single task
4. PUT/update an existing task
5. GET the updated task
6. DELETE the task
7. GET all tasks again to verify deletion

### Testing Result

All required CRUD operations were successfully tested.

After deleting the test task, the final GET request returned:

```json
{
    "success": true,
    "count": 0,
    "tasks": []
}
```

This confirmed that the task was successfully removed from the database.

## What I Learned

* How REST APIs work in Django.
* How HTTP methods are used for CRUD operations.
* How Django returns JSON responses.
* How JSON data is received from API requests.
* How API endpoints are connected using URL routing.
* How Django API views communicate with the database.
* How to test API endpoints using Postman.
* How the backend API will communicate with a React frontend.

## Day 5 Outcome

The Task Tracker REST API was successfully created and tested.

The backend can now:

* Create tasks
* Retrieve all tasks
* Retrieve a single task
* Update tasks
* Delete tasks
* Return JSON responses
* Store task information in the database

The API is ready for the next step: connecting the React frontend to the Django backend using `fetch()`.

## Tools Used

* Python
* Django
* SQLite
* Postman
* Visual Studio Code
