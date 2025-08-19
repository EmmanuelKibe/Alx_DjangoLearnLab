from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('price', 'stock')
    ordering = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'flagged')
    search_fields = ('text',)
    list_filter = ('flagged', 'created_at')
    ordering = ('-created_at',)