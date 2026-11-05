from django.contrib import admin
from .models import Book, GuestbookEntry

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(GuestbookEntry)
class GuestbookAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'content', 'is_verified')
    list_editable = ('is_verified',) # 可以在后台直接勾选审核
