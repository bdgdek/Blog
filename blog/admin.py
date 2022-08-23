from django.contrib import admin
from .models import Post

#import post from .models and register it would add a section for the post in admin django
admin.site.register(Post)
