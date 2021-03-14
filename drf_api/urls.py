from core.views import TestView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TestView.as_view(), name="test"),
]
