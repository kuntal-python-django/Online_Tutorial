'''
   @ Author     Kuntal
   @ version    0.1
   @date        29/04/2020
'''
from django.urls import path
from .import views


urlpatterns = [
    # path('', views., name=""),
    path('', views.index, name="home"),
    path('contact/', views.contact, name="contact"),
    path('courses/details/', views.course_details, name="course_details"),
    path('courses/', views.courses, name="courses"),
    path('subscribe/', views.subscribe, name="subscribe"),
    path('api/get/courses/', views.get_courses_Api, name="get_courses_Api"),
]
