from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet
from .models import Test
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .forms import TweetModelForm
from .forms import TestModelForm 
from .forms import PostModelForm
from django import forms  
from django.forms.utils import ErrorList
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect,Http404
from .models import Post
from .forms import UserModelForm,LoginModelForm
from django.views import generic
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
# from .forms import NameForm 

#Retrieve
# def tweet_detail_view(request,pk=None):
# 	obj = Tweet.objects.get(id=pk) #get data from database
# 	print(obj)
# 	# def read():
# 	# 	file=open("pl.txt","r")
# 	# 	values=[]
# 	# 	for line in file:
# 	# 		values.append(line)
# 	# 		print(line)
# 	# read()
# 	context={
# 	'object':obj
# 	}
# 	return render(request,'tweets/detail.html',context)

# def tweet_list_view(request):
	# queryset=Tweet.objects.all()#gets all elements in database
	# print(queryset)
	# for obj in queryset:#getting contents in loop
	# 	print(obj.content)

	# context={
	# 'objects':queryset
	# }#sending data to html

	# file=open("pl.txt","r")
	# values=[]
	# for line in file:
	# 	values.append(line)
	# 	print(line)
	# return render(request,'tweets/list.html',{'values':values})

#class based views
class TweetListView(ListView):
	template_name='tweets/list.html'
	queryset = Tweet.objects.all()
	# def get_queryset(self,*args,**kwargs):
	# 	qs = Tweet.objects.all()
	# 	print(self.request.GET)
	# 	query=self.request.GET.get('q',None)
	# 	if query is not None:
	# 		qs=qs.filter(content__icontains=query)
	# 	return qs
		# print(self.request.GET)
		# query=self.request.GET.get('q',None)
		# if query is not None:
		# 	qs = qs.filter(content__icontains=query)
		# 	return qs

	# def read():
	# 	file=open("pl.txt","r")
	# 	values=[]
	# 	for line in file:
	# 		values.append(line)
	# 		print(line)
	# read()

class TweetDetailView(DetailView):
	template_name='tweets/detail.html'
	queryset=Tweet.objects.all()

	# def get_object(self):
	# 	return Tweet.objects.get(id=1)
#Create
class TweetCreateView(CreateView):
	# if not instance.user.is_staff or not instance.user.is_superuser:
		# 	
	form_class=TweetModelForm
	template_name='tweets/create_view.html'
	# success_url='/tweets/create'
	login_url='admin/login/'

	def form_valid(self, form):
		# if self.request.user.is_authenticated():
		form.instance.user=self.request.user
		return super(TweetCreateView,self).form_valid(form)
		# else:
		# 	form._errors[forms.forms.NON_FIELD_ERRORS] =ErrorList(["user must be logged in"])
		# 	return self._form_invalid(form)

class TestCreateView(CreateView):
	form_class = TestModelForm
	template_name = 'tweets/test_create.html'
	success_url='/tweets/test'

	def form_valid(self, form):
		# if self.request.user.is_authenticated():
		# form.instance.user=self.request.user
		if form.is_valid():
			save_it=form.save(commit=False)
			save_it.save()
			subject='My First mail'
			message='I did it'
			g=[save_it.email]
			print(g)
			from_email=settings.EMAIL_HOST_USER
			to_email = [save_it.email]
			send_mail(subject=subject,from_email=from_email,recipient_list=to_email,message=message,fail_silently=False)

		return super(TestCreateView,self).form_valid(form)

# def get_name(request):
# 	if request.method=='POST':
# 		form=NameForm(request.POST)

# 	if form.is_valid():
# 		return HttpResponseRedirect('/thanks/')
# 	else:
# 		form=NameForm()
# 	return render(request,'tweets/name.html',{'form':form})

#Update
class TweetUpdateView(UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = 'tweets/update_view.html'
	# success_url = '/tweets/'

#Delete
class TweetDeleteView(DeleteView):
	model = Tweet
	template_name ='tweets/delete_confirm.html'
	success_url = reverse_lazy('tweet:list')

def tweet_update_view(request,pk):
	object = Tweet.objects.get(id=pk)
	form = TweetModelForm(instance=object)
	return render(request,'tweets/my_test',{'form':form})

def post_create(request):
	form = PostModelForm(request.POST or None)
	df = [1,2,3,4,5,6]
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
	'form':form,
	'df':df
	}

	return render(request,'tweets/posts_create.html',context)

def post_detail(request , id=None):
	queryset = Post.objects.get(id=id)
	context = {
	'detail':queryset
	}

	return render(request,'tweets/post_detail.html',context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
	"object_list":queryset
	}
	return render(request,'tweets/post_list.html',context)
def post_update(request,id=None):
	queryset = Post.objects.get(id=id)
	form = PostModelForm(request.POST or None,instance=queryset)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
	'instance':queryset,
	'form':form 
	} 

	return render(request,'tweets/update_form.html',context)

def post_delete(request,id=None):
	instance=Post.objects.get(id=id)
	instance.delete()
	return HttpResponseRedirect("/tweets/post/list") 

class UserFormView(View):
	form_class = UserModelForm
	template_name = 'tweets/registration.html'
	# success_url='/tweets/register'

	def get(self, request):	
		form = self.form_class(None)
		return render(request , self.template_name , {'form':form})

	def post(self, request):

		form = self.form_class(request.POST)


		if form.is_valid():

			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username=username,password=password)

			if user is not None:
				login(request,user)
				return HttpResponseRedirect('/tweets/')

		return render(request , self.template_name , {'form':form})

class LoginUserView(View):
	form_class = LoginModelForm
	template_name = 'tweets/login.html'
	# success_url = '/tweets/'

	def get(self, request):	
		form = self.form_class(None)
		return render(request , self.template_name , {'form':form})

	def post(self,request):
		form = self.form_class(request.POST)


		if form.is_valid():

			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			if user is not None:
				login(request,user)
				return HttpResponseRedirect('tweet:list')

		return render(request , self.template_name , {'form':form})

def login_user(request):
	if request.method == 'POST':
 		form = AuthenticationForm(data=request.POST)

 		if form.is_valid():
 			user = form.get_user()
 			login(request,user)
 			return redirect('/tweets/')
 		else:
 			return render(request,'tweets/login.html',{'form':form})
	else:
 		form = AuthenticationForm() 	
 		return render(request,'tweets/login.html',{'form':form})

def logout_user(request):
	logout(request)
	return redirect('/tweets/login1')