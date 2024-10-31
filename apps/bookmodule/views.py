from django.shortcuts import render
from django.http import HttpResponse

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