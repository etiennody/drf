from core.views import PostView
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", PostView.as_view(), name="post"),
    path("api/token/", obtain_auth_token, name="obtain-token"),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
]
