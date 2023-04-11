from django.contrib import admin
from .models import *
# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','Login','UserType','Photo')
    search_fields = ('Login','UserType')


admin.site.register(Users, UsersAdmin)