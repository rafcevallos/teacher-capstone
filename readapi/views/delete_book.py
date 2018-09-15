from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.template import RequestContext
from readapi.models import Book


@login_required
def delete_book(request, pk):
    """Displays template for deleting a book"""
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('readapi:list_book')