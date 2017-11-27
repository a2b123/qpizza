from django.contrib import admin

# Register your models here.
from app.models import Restaurant, Customer, Driver 

admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)
