from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.student_form, name='student_form'),
    path('detail/<int:pk>/', views.student_detail, name='student_detail'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),

]
