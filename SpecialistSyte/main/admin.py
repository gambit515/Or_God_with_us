from django.contrib import admin
from .models import *
# Register your models here.

#class UsersAdmin(admin.ModelAdmin):
#   list_display = ('id','Login','UserType','Photo')
#   search_fields = ('id','Login','UserType')


#admin.site.register(Users, UsersAdmin)


class AnketaAdmin(admin.ModelAdmin):
    list_display = ('id','Tittle')
    search_fields = ('id','Tittle')


admin.site.register(Anketa, AnketaAdmin)


class Lang_catAdmin(admin.ModelAdmin):
    list_display = ('id','Tittle')
    search_fields = ('id','Tittle')


admin.site.register(Lang_categori, Lang_catAdmin)


class Soft_catAdmin(admin.ModelAdmin):
    list_display = ('id','Tittle')
    search_fields = ('id','Tittle')


admin.site.register(Soft_categori, Soft_catAdmin)