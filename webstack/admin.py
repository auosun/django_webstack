from django.contrib import admin
from .models import Menu,Website

# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'icon', 'weight')
    list_editable = ['icon','weight']

class WebsiteAdmin(admin.ModelAdmin):
    list_filter = ['menu']
    list_display = ('name', 'description', 'url', 'weight', 'menu')
    list_editable = ['description','url','weight','menu']

admin.site.register(Menu,MenuAdmin)
admin.site.register(Website,WebsiteAdmin)

