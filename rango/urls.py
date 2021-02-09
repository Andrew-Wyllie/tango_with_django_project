from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
	path('about/', views.about, name='about'),
	path('category/<slug:category_name_slug>/', 
		views.show_category, name='show_category'),
	path('add_category/', views.add_category, name='add_category'),
	path('index/', views.index, name='index'),
	path('register/', views.register, name='register'),
	path('restricted/', views.restricted, name='restricted'),
	path('login/', views.user_login, name='login'),

]