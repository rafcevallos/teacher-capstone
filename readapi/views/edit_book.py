from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.urls import reverse
from readapi.forms import BookForm
from readapi.models import Book


@login_required
def edit_book(request, pk):
    print(pk)
    print(request.method)
    if request.method == "GET":
        print("GET")
        book = Book.objects.get(pk=pk)
        # Here's where we load the form
        book_form = BookForm(initial={'title': book.title,
                                      'author': book.author, 'photo': book.book_photo, 'level': book.level, 'word_count': book.word_count, 'unit': book.unit, 'notes': book.notes, 'genre': book.genre}, )  # create profile fields and set defaults)
        return render(request, 'book/edit_book.html', {'book': book, 'book_form': book_form})

    elif request.method == "POST":
        print("POST")
        # Here's where we post updated info to the book
        book = Book.objects.get(pk=pk)
        book_form = BookForm(request.POST, instance=book)
        print('HERE IS THE STRING')

        if book_form.is_valid():
            book_form.save()

            return redirect(reverse('readapi:list_book'))
