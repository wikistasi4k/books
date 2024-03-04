from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Tag, Borrow

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books/book_list.html', {'page_obj': page_obj})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    borrow, created = Borrow.objects.get_or_create(book=book, user=request.user, is_returned=False)
    if created:
        return redirect('book_list')
    else:
        return redirect('book_detail', book_id=book_id)

@login_required
def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrow, pk=borrow_id)
    borrow.returned_date = timezone.now()
    borrow.is_returned = True
    borrow.save()
    return redirect('borrowed_books')

@login_required
def borrowed_books(request):
    borrows = Borrow.objects.filter(user=request.user, is_returned=False)
    return render(request, 'books/borrowed_books.html', {'borrows': borrows})


