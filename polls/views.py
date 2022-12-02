from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
import numpy as np
# Create your views here.

def index(request):
    test = np.arange(0, 5)
    res = "Numpy Test(np.arange(0, 5)): " + str(test)
    res2 = "Hello World!" + res
    return HttpResponse(res2)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse("You're looking at question %s." % question)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voiting on question %s." % question_id)

