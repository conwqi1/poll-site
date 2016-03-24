from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")

def detail(request, question_id):
    return HttpResponse("You are looking at qestion %s." % question_id)

def results(request, question_id):
    return HttpResponse("You are looking at the result of question %s.")

def vote(request, question_id):
	return HttpResponse("You are voting on quesiton %s." % question_id)