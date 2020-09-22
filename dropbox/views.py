from django.shortcuts import render
from .models import File
# Create your views here.
def show_files(request):
    return render(request, "index.html", {'files': File.objects.all()})