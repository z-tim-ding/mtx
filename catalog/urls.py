from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='catalog_home'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category-books/<uuid:category_id>',
         views.get_category_books,
         name='category_books')
]
