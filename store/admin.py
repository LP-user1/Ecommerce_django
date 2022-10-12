from django.contrib import admin
from .models import *

class productAdmin(admin.ModelAdmin):
  list_display = ('name','quantity','category')
  list_display_links = ('name','quantity','category')


admin.site.register(Category),
admin.site.register(Order),
admin.site.register(Cart),
admin.site.register(Profile),
admin.site.register(Product,productAdmin),


