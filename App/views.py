from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.http import JsonResponse
from django.http import Http404, HttpResponse
from datetime import datetime
from .models import *
from django.db.models import Q
from .help import IPdetect, browserDetect
from .dbSerializers import CoursesSerializer
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(req):
    try:
        common_data = BaseCMS.objects.get(id=1)
    except Exception as e:
        common_data = ''
    try:
        index_data = HomeCMS.objects.get(id=1)
    except Exception as e:
        index_data = ''

    course_list = Courses.objects.all()
    paginator = Paginator(course_list, 20)
    try:
        page = req.GET.get('page', 1)
        course_list = paginator.page(page)
    except PageNotAnInteger:
        course_list = paginator.page(1)
    except EmptyPage:
        course_list = paginator.page(paginator.num_pages)

    context = {'common_data': common_data, 'index_data': index_data, 'course_list': course_list}
    return render(req, 'learnit/index.html', context=context)


def contact(req):
    if req.method == 'GET':
        try:
            common_data = BaseCMS.objects.get(id=1)
        except Exception as e:
            common_data = ''
        context = {'common_data': common_data, "status": 0}
        return render(req, 'learnit/contact.html', context=context)
    elif req.method == 'POST':
        try:
            name = req.POST['name']
            email = req.POST['email']
            subject = req.POST['subject']
            message = req.POST['message']
            ip = IPdetect.GetRemotePCIP(req)
            user_browser = browserDetect.BrowserDetails(req)

            cu = ContactUs.objects.filter(
                user_ip=ip, user_browser=user_browser
            )
            if len(cu) == 0:
                ContactUs(name=name, email=email, subject=subject, message=message, user_ip=ip, user_browser=user_browser).save()
                req.method = 'GET'
                return contact(req)
            else:
                try:
                    common_data = BaseCMS.objects.get(id=1)
                except Exception as e:
                    common_data = ''
                context = {'common_data': common_data, "status": 1}
                return render(req, 'learnit/contact.html', context=context)

        except Exception as e:
            req.method = 'GET'
            return contact(req)
    else:
        raise Http404


def subscribe(req):
    try:
        mail = req.GET.get("mail")
        Subscriber.objects.get(email=mail)
        success = False
    except Exception as e:
        success = True
    try:
        mail = req.GET["mail"]
        ip = IPdetect.GetRemotePCIP(req)
        user_browser = browserDetect.BrowserDetails(req)
        location = req.GET.get('location')
        Subscriber(email=mail, user_ip=ip, user_browser=user_browser, location=location).save()
        success = True
    except Exception as e:
        success = False

    data = {"success": success}
    return JsonResponse(data, safe=True)


def courses(req):
    try:
        common_data = BaseCMS.objects.get(id=1)
    except Exception as e:
        common_data = ''
    try:
        index_data = HomeCMS.objects.get(id=1)
    except Exception as e:
        index_data = ''
    try:
        subject = req.GET['title']
        course_list = Courses.objects.filter(tag=subject)
    except Exception as e:
        course_list = Courses.objects.all()

    paginator = Paginator(course_list, 20)
    try:
        page = req.GET.get('page', 1)
        course_list = paginator.page(page)
    except PageNotAnInteger:
        course_list = paginator.page(1)
    except EmptyPage:
        course_list = paginator.page(paginator.num_pages)


    context = {'common_data': common_data, 'index_data': index_data, 'course_list': course_list}
    return render(req, 'learnit/courses.html', context=context)


def course_details(req):
    try:
        common_data = BaseCMS.objects.get(id=1)
    except Exception as e:
        common_data = ''
    try:
        c_id = req.GET['id']
    except Exception as e:
        c_id = 1
    try:
        course = Courses.objects.get(id=c_id)
    except Exception as e:
        raise Http404

    context = {'common_data': common_data, 'course': course}
    return render(req, 'learnit/course-details.html', context=context)


@api_view(('GET',))
def get_courses_Api(req):
    try:
        start = req.GET.get('start')
        end = req.GET.get('end')
        course_list_data = Courses.objects.all()
        course_list = CoursesSerializer(course_list_data, many=True)
    except:
        course_list = ''

    data={'course_list': course_list.data}
    return Response(data)
