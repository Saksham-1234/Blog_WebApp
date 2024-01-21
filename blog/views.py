from django.shortcuts import render

# create your views


def index(request):
    return render(request,index.html)


