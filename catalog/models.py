import uuid

from django.db import models
from django.urls import reverse


# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this user")
    email = models.EmailField
    user_name = models.CharField(max_length=20)
    password = models.CharField
    last_login = models.TimeField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_name


class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this book")
    title = models.CharField(max_length=200)
    author_id = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    cover = models.BinaryField(null=True)
    book_text = models.TextField(default="")

    def __str__(self):
        return self.title

    def get_book_raw_text(self):
        return self.book_text

    def get_absolute_url(self):
        return reverse('book-text', args=[str(self.book_id)])


class Author(models.Model):
    author_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this author")
    author_name = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=10, default="ENG", null=True)

    def __str__(self):
        return self.author_name


class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this category")
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Comment unique ID")
    comment_text = models.TextField(default="")
    book_id = models.ForeignKey('Book', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text


class Read(models.Model):
    num_times_read = models.IntegerField(default=0)
    book_id = models.ForeignKey('Book', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    last_read = models.TimeField
