from django.contrib import admin
from .models import *


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


class OtklikAdmin(admin.ModelAdmin):
    list_display = ('id','FIO','Phone','Email','DatePost')
    search_fields = ('id','FIO','Phone','Email','DatePost')


admin.site.register(Otklik, OtklikAdmin)
