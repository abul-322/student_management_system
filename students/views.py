from django.shortcuts import render, redirect, get_object_or_404

from .models import Student
from .forms import StudentForm


# ================================
# DASHBOARD
# ================================

def dashboard(request):

    students = Student.objects.all()

    return render(
        request,
        "students/dashboard.html",
        {
            "students": students
        }
    )


# ================================
# ADD STUDENT
# ================================

def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("dashboard")

    else:

        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {
            "form": form
        }
    )


# ================================
# EDIT STUDENT
# ================================

def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()

            return redirect("dashboard")

    else:

        form = StudentForm(instance=student)

    return render(
        request,
        "students/student_form.html",
        {
            "form": form,
            "student": student
        }
    )


# ================================
# DELETE STUDENT
# ================================

def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect("dashboard")