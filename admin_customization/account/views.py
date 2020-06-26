from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate
from django.views import View
from django.contrib.auth import login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(View):
    context = dict()

    def get(self, request, *arg, **kwargs):
    	# print(">>>>>>>>>>>>>>In get method")
    	return render(request, 'login.html', self.context)

    def post(self, request, *arg, **kwargs):
    	email = request.POST.get('email')
    	password = request.POST.get('password')
    	user = authenticate(
    		email=email,
    		password=password,
    		)
    	# print(user)
    	# print(user.is_superuser)
    	if user:
    		if not user.is_superuser:
    			login(request, user)
    			return redirect('/profile')
    		else:
    			login(request, user)
    			return redirect('/profile')
    	else:
    		return redirect('/registration')



class SignUpView(View):
	context = dict()

	def get(self, request, *args, **kwargs):
		return render(request, 'register.html')

	def post(self, request, *args, **kwargs):

		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')
		try:
			user_obj= User.objects.create(
				email=email,
				username=username,
				)
			user_obj.set_password(password)
			user_obj.save()
			messages.success(request, 
				'User successfully registered'
				)
			return redirect('/login')
		except IntegrityError as e:
			print(str(e))
			if 'UNIQUE constraint' in str(e):
				messages.error(request, 
					'Email already registered'
				)
			return redirect('/registration')




class ProfileView(LoginRequiredMixin, View):
	login_url = '/login'
	context = dict()
	def get(self, request, *args, **kwargs):
		users_list = User.objects.all()
		paginator = Paginator(users_list, 20)
		page = request.GET.get('page')
		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)
		self.context['users_list'] = users

		return render(request, 'profile.html', self.context)

	def post(self, request, *args, **kwargs):
		id = self.request.POST.get('delete')
		user = User.objects.get(id=id)
		user.delete()
		return redirect('/profile') 


class LogoutView(View):
	def get(self, request, *args, **kwargs):
		logout(request)
		return redirect('/login')
