from django.shortcuts import render

def home(request):
    return render(request, "todo/home.html")

# Create your views here.