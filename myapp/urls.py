from django.urls import path
from . import views
urlpatterns = [
	path('',views.index,name='index'),
	path('demo1',views.demo1,name='demo1'),
	path('demo2',views.demo2,name='demo2'),
	path('showdistrict/',views.showdistrict,name='showdistrict'),
	path('district/<int:id>',views.district,name="district")
] 