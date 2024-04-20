from django.contrib import admin
from .models import Category, Menus, Promos, Medias, Home_banners

# Register your models here.
admin.site.register(Category)
admin.site.register(Menus)
admin.site.register(Promos)
admin.site.register(Medias)
admin.site.register(Home_banners)