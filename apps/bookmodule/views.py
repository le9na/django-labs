from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Address, Student, Student2, Address2
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .forms import BookForm, StudentForm, AddressForm, ImageUploadForm, Student2Form, Address2Form

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
    #city_counts = Address.objects.annotate(student_count=Count('student')).values_list('city', 'student_count')
    #city_counts_dict = dict(city_counts)
    #return render(request, 'bookmodule/task6.html', {'city_counts': city_counts_dict})
    return 

# Task 1: List books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9/list_books.html', {'books': books})

# Task 2: Add a new book
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST.get('description', '')
        Book.objects.create(title=title, author=author, description=description)
        return redirect('list_books')
    return render(request, 'bookmodule/lab9/add_book.html')

# Task 3: Edit a book
def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.description = request.POST.get('description', '')
        book.save()
        return redirect('list_books')
    return render(request, 'bookmodule/lab9/edit_book.html', {'book': book})

# Task 4: Delete a book
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books')

# Task 1: List books
def list_books_with_forms(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part2/list_books_with_forms.html', {'books': books})

# Task 2: Add a new book using a form
def add_book_with_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books_with_forms')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab9_part2/add_book_with_form.html', {'form': form})

# Task 3: Edit a book using a form
def edit_book_with_form(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books_with_forms')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab9_part2/edit_book_with_form.html', {'form': form})

# Task 4: Delete a book
def delete_book_with_form(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books_with_forms')

# List students
def list_students(request):
    students = Student.objects.all()
    return render(request, 'students/list_students.html', {'students': students})

# Add student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/add_student.html', {'form': form})

# Edit student
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'bookmodule/edit_student.html', {'form': form})

# Delete student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('list_students')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_images')
    else:
        form = ImageUploadForm()
    return render(request, 'bookmodule/upload_image.html', {'form': form})


# List students
def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/list_students2.html', {'students': students})

# Add student
def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form()
    return render(request, 'bookmodule/add_student2.html', {'form': form})

# Edit student
def edit_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form(instance=student)
    return render(request, 'bookmodule/edit_student2.html', {'form': form})

# Delete student
def delete_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    student.delete()
    return redirect('list_students2')