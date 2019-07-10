from django.contrib import admin
from .models import Parent, Child, Address

# Register your models here.
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Address)
