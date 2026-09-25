# Day 7 — Mini Project: Task Tracker Backend API

## Objective

Complete and verify the Task Tracker backend API by testing CRUD operations, JSON responses, database storage, and React-Django integration.

## Work Completed

### 1. Django Task Model

The Task model contains the required fields:

* `task_name`
* `description`
* `status`
* `created_date`

The status field supports:

* `pending`
* `in_progress`
* `completed`

### 2. API Endpoints

The Task Tracker backend provides the following endpoints:

* `GET /api/tasks/` — Retrieve all tasks
* `POST /api/tasks/` — Create a new task
* `GET /api/tasks/<id>/` — Retrieve a specific task
* `PUT /api/tasks/<id>/` — Update a task
* `DELETE /api/tasks/<id>/` — Delete a task

### 3. JSON Responses

The API returns responses in JSON format using Django `JsonResponse`.

### 4. API Testing

The APIs were tested using Postman.

The following operations were successfully tested:

* GET — Retrieve tasks
* POST — Create a new task
* PUT — Update an existing task
* DELETE — Delete a task

### 5. Database

Task information is stored in the Django SQLite database.

The API successfully creates, retrieves, updates, and deletes task records from the database.

### 6. React-Django Integration

The existing React Task Tracker frontend communicates with the Django backend using the JavaScript `fetch()` API.

The frontend supports:

* Fetching tasks
* Adding tasks
* Updating task status
* Delet
