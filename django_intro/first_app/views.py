from django.shortcuts import render

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return HttpResponse(index(request))

def show(request, num):
    return HttpResponse(f"Placeholder to display blog number:{num}")
    
def edit(request, num):
    return HttpResponse(f"Placeholder to edit blog {num}")

def destroy(request, num):
    return HttpResponse(index(request))