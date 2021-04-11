from django.urls import path
from . import views

urlpatterns = [
	path('', views.main_page, name='main_page'),
	path('voronoi', views.voronoi_prikaz, name='voronoi_prikaz'),
	path('unesikoord', views.unesi_koordinatu, name='unesi_koordinatu'),
	path('toggle', views.toggle_visibility, name='toggle_visibility'),
]