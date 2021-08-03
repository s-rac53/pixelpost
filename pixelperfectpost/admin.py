from django.contrib import admin
from .models import Work, Service, Portfolio, Customer


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','created','media']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name', 'created',]


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','created','video']
    prepopulated_fields = {'slug': ('description',)}
    list_filter = ['name', 'created',]


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','created','image']
    prepopulated_fields = {'slug': ('description',)}
    list_filter = ['name', 'created',]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['lname','fname','number' ,'created','email']
    list_filter = ['lname','fname', 'created','number', 'email']








