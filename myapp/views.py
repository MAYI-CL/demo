from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from myapp.models import District
# Create your views here.

def index(request):
	return render(request,"myapp/index.html")

def demo1(request):
	context={}
	context['name']='zhangsan'
	context['a']=[10,20,30]
	context['stu']={'name':'list','age':20}
	data=[
		{'name':'q','sex':1,'age':40,'state':0},
		{'name':'w','sex':0,'age':40,'state':2},
		{'name':'e','sex':1,'age':40,'state':1},
		{'name':'r','sex':0,'age':40,'state':2},
	]
	context['dlist']=data
	context['time']=datetime.now
	context['m1']=100
	context['m2']=20
	return render(request,"myapp/demo1.html",context)
def demo2(request):
	return render(request,'myapp/demo2.html')

def showdistrict(request):
	return render(request,"myapp/district.html")

def district(request,id=0):
	dlist = District.objects.filter(pid=id)
	mylist = []
	for ob in dlist:
		mylist.append({'pid':ob.pid,'district_name':ob.district_name})
	return JsonResponse({'data':mylist})