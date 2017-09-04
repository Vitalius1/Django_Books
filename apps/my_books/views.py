from django.shortcuts import render

def index(request):
    return render(request, "my_books/index.html")
# Create your views here.
