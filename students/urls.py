from django.urls import path

from . import views


urlpatterns = [

    # Login
    path(
        "",
        views.login_view,
        name="login"
    ),

    # Dashboard
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    # Add Student
    path(
        "add/",
        views.add_student,
        name="add_student"
    ),

    # Edit Student
    path(
        "edit/<int:id>/",
        views.edit_student,
        name="edit_student"
    ),

    # Delete Student
    path(
        "delete/<int:id>/",
        views.delete_student,
        name="delete_student"
    ),

]