from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    path('course/list', views.course_list, name='course_list'),
    path('course/form', views.course_form, name='course_form'),
    path('detail/<int:pk>/', views.course_detail, name='course_detail'),
    path('delete/<int:pk>/', views.course_delete, name='course_delete'),
]
