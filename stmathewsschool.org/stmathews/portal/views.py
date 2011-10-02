from portal.models import Student
from django.shortcuts import render_to_response # shortcut to following
# from django.http import HttpResponse
# from django.template import Context, loader


def index(request):
    student_instance = Student.objects.order_by('last_name')[0]
    return render_to_response('portal/index.html',
                                    {'student_instance': student_instance})

def info(request):
    student_instance = Student.objects.order_by('last_name')[0]
    return render_to_response('portal/info.html',
                                    {'student_instance': student_instance})

def students(request, student_id):
    student_list = Student.objects.order_by('last_name')
    if(student_id):
        student_instance = Student.objects.get(pk=student_id)
    else:
        student_instance = Student.objects.order_by('last_name')[0]
    
    return render_to_response('portal/students.html',
                                    {'student_instance': student_instance,
                                    'student_list': student_list})

def teachers(request):
    student_instance = Student.objects.order_by('last_name')[0]
    return render_to_response('portal/teachers.html',
                                    {'student_instance': student_instance})

def donate(request):
    student_instance = Student.objects.order_by('last_name')[0]
    return render_to_response('portal/donate.html',
                                    {'student_instance': student_instance})
