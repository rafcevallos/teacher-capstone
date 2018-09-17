from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render
from readapi.models import Book


@login_required
def list_book(request):
    search_terms = request.GET.get('search_terms', '')
    print(search_terms)
    all_books = Book.objects.all()
    if search_terms:
        search_results = [
            book for book in all_books if search_terms in book.title]
        print(search_results)
        # filter all_books and render the filtered stuff
        return render(request, 'book/search_book.html', {'search_results': search_results})
    else:
        return render(request, 'book/list_book.html', {'all_books': all_books})
