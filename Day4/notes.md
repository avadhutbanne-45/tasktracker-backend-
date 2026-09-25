# Day 4 — Database Integration

## Topic

Models, Migrations, and SQLite Database

## Objective

The objective of Day 4 was to integrate a database with the Django Task Tracker backend and create a Task model for storing task information.

## What I Learned

### 1. Django Models

Django models are used to define the structure of data that the application stores in the database.

For the Task Tracker application, I created a `Task` model with the following fields:

* `task_name` — stores the name of the task.
* `description` — stores the task description.
* `status` — stores the current task status.
* `created_date` — stores the date and time when the task was created.

I also created status choices:

* Pending
* In Progress
* Completed

### 2. Migrations

Django migrations are used to convert changes made in models into database structure.

I created the initial migration using:

```bash
python manage.py makemigrations
```

The migration created was:

```text
tasks/migrations/0001_initial.py
```

### 3. Applying Migrations

I applied the migrations to the database using:

```bash
python manage.py migrate
```

The Task model migration was successfully applied:

```text
Applying tasks.0001_initial... OK
```

### 4. SQLite Database

The Django project uses SQLite as the database.

The database file is:

```text
db.sqlite3
```

The Task model is stored in the database after applying the migration.

### 5. Migration Verification

I verified that the Task migration was successfully applied using:

```bash
python manage.py showmigrations tasks
```

Output:

```text
tasks
 [X] 0001_initial
```

The `[X]` indicates that the migration has been successfully applied.

## Commands Used

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations tasks
```

## Day 4 Outcome

Successfully created the Task model, generated the initial migration, applied the migration to the SQLite database, and verified that the migration was successfully applied.

## Key Takeaways

* Django models define the structure of application data.
* Migrations keep Django models and the database structure synchronized.
* `makemigrations` creates migration files.
* `migrate` applies migrations to the database.
* SQLite can be used as a database for a Django application.
* `showmigrations` can be used to verify migration status.
