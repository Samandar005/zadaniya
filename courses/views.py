from django.shortcuts import render, redirect, get_object_or_404
from .models import Course


def course_list(request):
    courses = Course.objects.all()
    ctx = {'courses': courses}
    return render(request, 'courses/course-list.html', ctx)

def course_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        max_student = request.POST.get('max_student')
        if (name and description and start_date
                and end_date and max_student):
            Course.objects.create(
                name=name,
                description=description,
                start_date=start_date,
                end_date=end_date,
                max_student=max_student
            )
            return redirect('courses:course_list')
    return render(request, 'courses/course-form.html')

def course_detail(request, pk):
    courses = get_object_or_404(Course, pk=pk)
    ctx = {'courses': courses}
    return render(request, 'courses/course-detail.html', ctx)

def course_delete(request, pk):
    courses = get_object_or_404(Course, pk=pk)
    courses.delete()
    return redirect('courses:course_list')