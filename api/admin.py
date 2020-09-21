from django.contrib import admin
from .models import CustomUser

# Register your models here.

admin.site.register(CustomUser)			# registering our CustomUser model in admin pannel
