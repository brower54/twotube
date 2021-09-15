from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # import rules from posts app
    path("", include("posts.urls")),
    # import rules from admin app
    path('admin/', admin.site.urls),
]
