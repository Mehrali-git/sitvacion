from django.contrib import admin
from . import models
from django_jalali.admin.filters import JDateFieldListFilter
# #you need import this for adding jalali calander widget
# import django_jalali.admin as jadmin

@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branchId', 'name', 'manager', 'ip','status')
    list_filter = ('name',)
    search_fields = ('branch', 'name')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['branchId']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'status')
    list_filter = ('title', 'status')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['title']


@admin.register(models.Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'category', 'price', 'status', 'count')
    list_filter = ('count',)
    search_fields = ('title', 'category')
    prepopulated_fields = {'slug': ('title', 'count', 'price', 'position')}
    ordering = ['position']


@admin.register(models.Cash)
class CashAdmin(admin.ModelAdmin):
    list_display = ('branch', 'recive_day', 'peymen_day', 'inventory_end_day', 'jpublish', 'date_persian')
    list_filter = ('branch', 'publish')
    search_fields = ('branch', 'jpublish')
    ordering = ['publish','branch']


@admin.register(models.Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('branch','total', 'publish', 'date_persian')
    list_filter = ('branch', 'publish',('date_persian', JDateFieldListFilter))
    search_fields = ('branch', 'jpublish')
    ordering = ['publish','branch']