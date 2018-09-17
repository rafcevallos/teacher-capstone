from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render
from readapi.models import Book, Student
from itertools import chain


@login_required
def search_results(request):
    search_terms = request.GET.get('search_terms', '') # get the terms the user has searched for
    lower_search_terms = search_terms.lower() # turn user input into lowercase
    print('Search Terms:', search_terms)
    all_books = Book.objects.all()
    # print('ALL THE BOOKS:', all_books)
    all_students = Student.objects.all()
    # print('ALL THE STUDENTS:', all_students)
    # all_data = all_books|all_students
    all_data = list(chain(all_students, all_books)) # combine two querysets into one list
    print('ALL THE DATA:', all_data)
    if search_terms:
        print('Search Terms:', search_terms)
        search_results = [
            data for data in all_data if lower_search_terms
            ]
        print('Search Results:', search_results)
        # filter all_books and render the filtered stuff
        return render(request, 'search_results.html', {'search_results': search_results})
    # else:
    #     return render(request, 'search_results.html', {'all_data': all_data,})
