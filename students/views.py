from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def home(request):
    return render(request, 'index.html')

def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/student-list.html', ctx)

def student_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        data_birth = request.POST.get('data_birth')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        if (first_name and last_name and
                email and data_birth
                and gender and address):
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                data_birth=data_birth,
                gender=gender,
                address=address
            )
            return redirect('students:student_list')
    return render(request, 'students/student-form.html')

def student_detail(request, pk):
    students = get_object_or_404(Student, pk=pk)
    ctx = {'students': students}
    return render(request, 'students/student-detail.html', ctx)

def student_delete(request, pk):
    students = get_object_or_404(Student, pk=pk)
    students.delete()
    return redirect('students:student_list')

