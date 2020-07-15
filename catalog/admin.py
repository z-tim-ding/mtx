from django.contrib import admin
from .models import Book, Author, Category, Comment, User, Read

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Read)