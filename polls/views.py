from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
# Create your views here.

def index(request):
    test = np.arange(0, 5)
    res = "Numpy Test(np.arange(0, 5)): " + str(test)
    return HttpResponse(res)
