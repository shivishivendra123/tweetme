from django.contrib import admin
from .models import Tweet
from .models import Test
from .models import Post

from .forms import TweetModelForm

# Register your models here.
admin.site.register(Test)

# class TweetModelAdmin(admin.ModelAdmin):
# 	form = TweetModelForm
# 	class Meta:
# 		model = Tweet
		

admin.site.register(Tweet)
admin.site.register(Post)