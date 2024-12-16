from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Address, Student
from django.db.models import Q, Count, Sum, Avg, Max, Min

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1 = 0): #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))


def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/html5links.html')

def formatting(request):
    return render(request, "bookmodule/formatting.html")

def listing(request):
    return render(request, "bookmodule/listing.html")

def tables(request):
    return render(request, "bookmodule/tables.html")

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True

            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    else:
        return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='Continuous') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lookup_query(request):
    mybooks=books=Book.objects.filter(author__isnull =
    False).filter(title__icontains='Delivery')[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')



#Only call this function once!
def __insertion_db():
    book1 = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 2)
    book1.save()
    book2 = Book(title = 'Reversing: Secrets of Reverse Engineering', author = 'E. Eilam', edition = 1)
    book2.save()
    book3 = Book(title = 'The Hundred-Page Machine Learning Book', author = 'Andriy Burkov', edition = 1)
    book3.save()
    
    
def task1(request):
    books = Book.objects.filter(Q(price__lte = 50))
    return render(request, 'bookmodule/task1.html',{'books':books})

def task2(request):
    books = Book.objects.filter(Q(edition_gt = 2) & (Q(titleicontains='qu') | Q(author_icontains='qu')))
    return render(request, 'bookmodule/task2.html',{'books':books})

def task3(request):
    books = Book.objects.filter(~Q(edition_gt = 2) & (~Q(titleicontains='qu')| ~Q(author_icontains='qu')))
    return render(request, 'bookmodule/task3.html',{'books':books})

def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task4.html',{'books':books})

def task5(request):
    mybooks = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': mybooks})

def task6(request):
    city_counts = Address.objects.annotate(student_count=Count('student')).values_list('city', 'student_count')
    city_counts_dict = dict(city_counts)
    return render(request, 'bookmodule/task6.html', {'city_counts': city_counts_dict})