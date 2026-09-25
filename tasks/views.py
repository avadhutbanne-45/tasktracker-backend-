import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Task


def home(request):
    return JsonResponse({
        "success": True,
        "message": "Task Tracker Backend is running"
    })


def task_to_dict(task):
    return {
        "id": task.id,
        "task_name": task.task_name,
        "description": task.description,
        "status": task.status
    }


@csrf_exempt
def task_list(request):

    if request.method == "GET":
        tasks = Task.objects.all().order_by("-id")

        return JsonResponse({
            "success": True,
            "count": tasks.count(),
            "tasks": [task_to_dict(task) for task in tasks]
        })

    if request.method == "POST":
        try:
            data = json.loads(request.body)

            task_name = data.get("task_name", "").strip()
            description = data.get("description", "").strip()
            status = data.get("status", "pending")

            if not task_name:
                return JsonResponse({
                    "success": False,
                    "error": "Task name is required"
                }, status=400)

            if status not in ["pending", "in_progress", "completed"]:
                return JsonResponse({
                    "success": False,
                    "error": "Invalid status"
                }, status=400)

            task = Task.objects.create(
                task_name=task_name,
                description=description,
                status=status
            )

            return JsonResponse({
                "success": True,
                "message": "Task created successfully",
                "task": task_to_dict(task)
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({
                "success": False,
                "error": "Invalid JSON"
            }, status=400)

    return JsonResponse({
        "success": False,
        "error": "Method not allowed"
    }, status=405)


@csrf_exempt
def task_detail(request, task_id):

    try:
        task = Task.objects.get(id=task_id)

    except Task.DoesNotExist:
        return JsonResponse({
            "success": False,
            "error": "Task not found"
        }, status=404)

    if request.method == "GET":

        return JsonResponse({
            "success": True,
            "task": task_to_dict(task)
        })

    if request.method == "PUT":

        try:
            data = json.loads(request.body)

            task_name = data.get(
                "task_name",
                task.task_name
            ).strip()

            description = data.get(
                "description",
                task.description
            ).strip()

            status = data.get(
                "status",
                task.status
            )

            if not task_name:
                return JsonResponse({
                    "success": False,
                    "error": "Task name is required"
                }, status=400)

            if status not in [
                "pending",
                "in_progress",
                "completed"
            ]:
                return JsonResponse({
                    "success": False,
                    "error": "Invalid status"
                }, status=400)

            task.task_name = task_name
            task.description = description
            task.status = status

            task.save()

            return JsonResponse({
                "success": True,
                "message": "Task updated successfully",
                "task": task_to_dict(task)
            })

        except json.JSONDecodeError:

            return JsonResponse({
                "success": False,
                "error": "Invalid JSON"
            }, status=400)

    if request.method == "DELETE":

        task.delete()

        return JsonResponse({
            "success": True,
            "message": "Task deleted successfully"
        })

    return JsonResponse({
        "success": False,
        "error": "Method not allowed"
    }, status=405)