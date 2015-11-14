from django.shortcuts import render
from .models import Txt
import re

def home(request):
	page = 1
	cnt = Txt.objects.count()
	maxpage = (cnt+9)/10
	if 'page' in request.GET:
		temp = request.GET['page']
		good = re.search('^[0-9]{1,8}$',temp)
		if good and int(temp)>0 and int(temp)<=maxpage:
			page = int(temp)

	tagsList = Txt.objects.all()[max(0,cnt-page*10):cnt-page*10+10:-1]
	pageList = [str(max(page-1,1)),str(page),str(maxpage),str(min(page+1,maxpage))]

	return render(request,'home.html', {'tagsList':tagsList,'pageList':pageList})

# Create your views here.
