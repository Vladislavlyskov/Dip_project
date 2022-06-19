from django.contrib import admin
from project.models import Comment, Model

# Register your models here.
admin.site.register(Model)
admin.site.register(Comment)
