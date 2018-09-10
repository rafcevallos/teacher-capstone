from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.template import RequestContext
from readapi.models import Book
from readapi.forms import BookForm


@login_required
def add_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():
            new_book = book_form.save()
            new_book.save()
            return redirect('readapi:list_book')
    else:
        book_form = BookForm()
    return render(request, 'book/add_book.html', {'book_form': book_form})