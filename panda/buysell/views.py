from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Account
from django.utils import timezone

def index(request):
	return render(request, 'buysell/index.html')

def signup(request):
	return render(request, 'buysell/signup.html')

def confirm(request):
	empty_field = "This field can't be empty"
	errors = dict()

	first_name = request.POST['inputFirstName']
	if not first_name:
		errors['error_first_name'] = empty_field
		
	last_name = request.POST['inputLastName']
	if not last_name:
		errors['error_last_name'] = empty_field
		
	user_name = request.POST['inputUserName']
	if not user_name:
		errors['error_user_name'] = empty_field
		
	e_mail = request.POST['inputEmail']
	if not e_mail:
		errors['error_email'] = empty_field
		
	first_password = request.POST['inputPass']
	if not first_password:
		errors['error_first_password'] = empty_field
		
	second_password = request.POST['inputPassword']
	if not second_password:
		errors['error_second_password'] = empty_field

	if (first_name and last_name and user_name and e_mail and first_password and second_password):
		if first_password == second_password:
			account = Account(firstName=first_name, lastName=last_name, username=user_name, email=e_mail, 
				password=first_password, datecreated=timezone.now())
			account.save()
			user_name = account.username
			return HttpResponseRedirect(reverse('buysell:contin', args=(user_name,)))
		else:
			error_password = "Passwords don't match"
			return render(request, 'buysell/signup.html', {'error_password': error_password})
	else:
		return render(request, 'buysell/signup.html', {'errors': errors})

def contin(request, user_name):
	account = Account.objects.get(pk=user_name)
	return render(request, 'buysell/contin.html', {'account': account})

def login(request):
	empty_field = "This field cannot be empty"
	errors = dict()

	user_name = request.POST['inputUserName']
	if not user_name:
		errors['empty_user_name'] = empty_field

	pass_word = request.POST['passWord']
	if not pass_word:
		errors['empty_password'] = empty_field

	if user_name and pass_word:
		try:
			account = Account.objects.get(pk=user_name)
		except Account.DoesNotExist:
			error_message = "Incorrect User Name"
			return render(request, 'buysell/index.html', {'error_message': error_message})
		else:
			if pass_word == account.password:
				return HttpResponseRedirect(reverse('buysell:postfeed'))
			else:
				error_password = "Incorrect Password"
				return render(request, 'buysell/index.html', {'error_password': error_password})
	else:
		return render(request, 'buysell/index.html', {'errors': errors})

def postfeed(request):
	return HttpResponse("Bro, Siraj, you are on track")