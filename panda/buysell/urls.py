from django.urls import path
from . import views

app_name = 'buysell'

urlpatterns = [
	path('', views.index, name='index'),
	path('signup/', views.signup, name='signup'),
	path('confirm/', views.confirm, name='confirm'),
	path('contin/<str:user_name>/', views.contin, name='contin'),
	path('login/', views.login, name='login'),
	path('postfeed/', views.postfeed, name='postfeed'),
	]