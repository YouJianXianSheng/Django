from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Index(request):
    return HttpResponse("Hello Python!!!!")

def detail(request,num):
	return HttpResponse("detail-%s"%num)