from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from readapi.models import Book


@login_required
def book_detail(request, pk):
    """
    View manages the book detail from the book list view
    """
    if request.method == 'GET':
        book = Book.objects.get(pk=pk)
        return render(request, 'book/detail_book.html', {'book': book})