from django.urls import path
from . import views

urlpatterns = [

    # Dashboard / Student List
    path('', views.dashboard, name='student_list'),

    # Add Student
    path('add/', views.add_student, name='add_student'),

    # Edit Student
    path('edit/<int:id>/', views.edit_student, name='edit_student'),

    # Delete Student
    path('delete/<int:id>/', views.delete_student, name='delete_student'),

]