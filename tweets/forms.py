from django import forms
from .models import Tweet
from .models import Test
from .models import Post
from django.contrib.auth.models import User

class TweetModelForm(forms.ModelForm):
	class Meta:
		model = Tweet
		fields = [
			# "user",
			"image",
			"content"
		]
class TestModelForm(forms.ModelForm):
	class Meta:
		model = Test
		fields = [
		"username","password","email"
		]
# class NameForm(forms.Form):
# 	your_name = forms.CharField(Label='Your name',max_length=100)

	# def clean_content(self,*args,**kwargs):
	# 	content = self.cleaned_data.get('content')
	# 	if content=='abc':
	# 		raise forms.ValidationError('cannot be abc')
	# 	return content

class PostModelForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"Title",
			"Content"
			]

class UserModelForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	
	class Meta:
		model = User
		fields = [
			"username","email","password"
		]

class LoginModelForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ["username","password"]