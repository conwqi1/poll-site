from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    question_list = Question.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context = { 
		'question_list': question_list,
	}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You are looking at qestion %s." % question_id)

def results(request, question_id):
    return HttpResponse("You are looking at the result of question %s.")

def vote(request, question_id):
	return HttpResponse("You are voting on quesiton %s." % question_id)