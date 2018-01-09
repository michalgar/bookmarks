from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Books
from .forms import BooksForm

def homepage(request):
    # output = ', '.join([book.title for book in book_list])
    book_list = Books.objects.all()
    context = {'all_books': book_list}
    return render(request, 'homepage/homepage.html', context)


# Product page
def product(request, book_id):
    selected_product = Books.objects.get(id=book_id)
    context = {'product': selected_product}
    return render(request, 'homepage/product.html', context)


def add(request):
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            #form_instance = form.save(commit=False)
            #form_instance.save()
            form.save()
            return HttpResponseRedirect('/homepage/')
    else:
        form = BooksForm()
    return render(request, 'homepage/add.html', {'form': form})

