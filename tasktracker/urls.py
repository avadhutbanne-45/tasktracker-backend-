from django.contrib import admin
from django.urls import include, path

from tasks.views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("api/tasks/", include("tasks.urls")),
]