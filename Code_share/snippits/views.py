from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
    return render(request,'index.html')
def share(request):
    return HttpResponse('sharing data# add to data base')

def delete(request):
    return HttpResponse("404")