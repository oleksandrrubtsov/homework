from django.urls import path

from . import views

app_name = "note"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("primary/", views.primary, name="primary"),
    path("secondary/", views.secondary, name="secondary"),
    path("success/", views.success, name="success"),
    path("danger/", views.danger, name="danger"),
    path("warning/", views.warning, name="warning"),
    path("info/", views.info, name="info"),
    path("light/", views.light, name="light"),


]