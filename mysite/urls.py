from django.contrib import admin
from django.urls import path

from api.views import BlogRUDView, BlogListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/<pk>/", BlogRUDView.as_view(), name="rud"),
    path("api/", BlogListView.as_view()),
]
