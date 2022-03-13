from django.contrib import admin
from .models import Company


# Register your models here.

class AdminCompany(admin.ModelAdmin):
    list_display = ['name', 'location', 'ceo']


admin.site.register(Company, AdminCompany)
