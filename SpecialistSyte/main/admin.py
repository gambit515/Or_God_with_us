from django.contrib import admin
from .models import *
# Register your models here.

#class UsersAdmin(admin.ModelAdmin):
#   list_display = ('id','Login','UserType','Photo')
#   search_fields = ('id','Login','UserType')


#admin.site.register(Users, UsersAdmin)
class OtklAdmin(admin.ModelAdmin):
    list_display = ('id','Anketa','Otkl_User')
    search_fields = ('id','Anketa','Otkl_User')


admin.site.register(Otkl, OtklAdmin)

class AnketaAdmin(admin.ModelAdmin):
    list_display = ('id','Tittle')
    search_fields = ('id','Tittle')


admin.site.register(Anketa, AnketaAdmin)


class Lang_catAdmin(admin.ModelAdmin):
    list_display = ('id','Tittle')
    search_fields = ('id','Tittle')


admin.site.register(Lang_categori, Lang_catAdmin)


class Main_categoriAdmin(admin.ModelAdmin):
    list_display = ('id','Tittle')
    search_fields = ('id','Tittle')


admin.site.register(Main_categori, Main_categoriAdmin)