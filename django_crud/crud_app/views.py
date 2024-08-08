from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
    )
from .models import Student
from .forms import StudentApplicationForm

# Create your views here.
def index(request):
    return render(request, "crud_app/index.html")

def create_student_view(request):
    if request.method == "POST":
        form = StudentApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = StudentApplicationForm()
    
    context = {
        "form": form,
    }
    
    return render(
        request,
        "crud_app/create.html",
        context
    )

def view_student_view(request):
    students = Student.objects.all()
    context = {
        "students": students
    }
    return render(
        request, 
        "crud_app/view.html", 
        context
    )
    
def view_student_one_view(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        "student": student
    }
    return render(
        request, 
        "crud_app/view_one.html", 
        context
    )
    
def delete_student_view(request, id):
    try:
        student = get_object_or_404(Student, id=id)
        student.delete()
    except Exception as e:
        print(e)
    
    return redirect("index")