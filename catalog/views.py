from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Book, Category
from django.views import generic
from django.shortcuts import get_list_or_404


def index(request):
    num_categories = Category.objects.all().count()
    num_books = Book.objects.all().count()
    context = {
        'num_books': num_books,
        'num_categories': num_categories,
    }
    return render(request, 'index.html', context=context)


def get_category_books(request, category_id):
    book_list = get_list_or_404(Book, category_id=category_id)
    return render(request, 'catalog/category_book_list.html', context={'book_list': book_list})


class CategoryListView(generic.ListView):
    model = Category

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(CategoryListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['num_categories'] = Category.objects.all().count()
        context['num_books'] = Book.objects.all().count()
        return context

