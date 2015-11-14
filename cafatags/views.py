from django.shortcuts import render
from .models import Txt

def home(request):
	tagsList = Txt.objects.all()[:25:-1]
	return render(request,'home.html', {'tagsList':tagsList})

# Create your views here.
