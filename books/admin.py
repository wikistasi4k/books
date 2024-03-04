from django.contrib import admin
from .models import Book, Author, Tag, Borrow

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description')
    list_filter = ('author', 'tags')
    search_fields = ('title', 'author__name')
    ordering = ('title',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BorrowAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrowed_date', 'returned_date', 'is_returned')
    list_filter = ('user', 'book')
    search_fields = ('user__username', 'book__title')
    ordering = ('-borrowed_date',)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Borrow, BorrowAdmin)
