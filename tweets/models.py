from django.conf import settings
from django.db import models
from django.urls import reverse
from .validators import validate_content,validate_content1
class Tweet(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	image = models.FileField(null=True, blank=True)
	content = models.CharField(max_length=140,validators=[validate_content,validate_content1])
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return str(self.content)
	def get_absolute_url(self):
		return "/tweets/%s/" %(self.id)

	# def clean(self,*args,**kwargs):
	# 	content = self.content
	# 	if content=="abc":
	# 		raise ValidationError("cannot be abc")
	# 	return content
	class Meta:
		ordering = ['-updated_at']

class Test(models.Model):
	username=models.CharField(max_length=10)
	password=models.CharField(max_length=10)
	email=models.EmailField(max_length=60)

	def __str__(self):
		return str(self.username)

class Post(models.Model):
	Title=models.CharField(max_length=140)
	Content=models.CharField(max_length=140)

	def __str__(self):
		return str(self.Title)

	def get_absolute_url(self):
		return "/tweets/post/%s" %(self.id)


	