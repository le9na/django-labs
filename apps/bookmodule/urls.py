from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('one_book/', views.viewbook, name="books.one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links, name="books.links"),
    path('html5/text/formatting/', views.formatting, name="books.formatting"),
    path('html5/tables/', views.tables, name="books.tables"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('search/', views.search, name="books.search"),
    path('simple/query/', views.simple_query, name="books.simple_query"),
    path('complex/query/', views.lookup_query, name="books.complex_query"),
    path('lab8/task1', views.task1, name="books.task1"),
    path('lab8/task2', views.task2, name="books.task2"),
    path('lab8/task3', views.task3, name="books.task3"),
    path('lab8/task4', views.task4, name="books.task4"),
    path('lab8/task5', views.task5, name="books.task5"),
    path('lab8/task6', views.task6, name="books.task6"),
    path('lab9_part1/listbooks', views.list_books, name='list_books'),
    path('lab9_part1/addbook', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
    path('lab9_part2/listbooks', views.list_books_with_forms, name='list_books_with_forms'),
    path('lab9_part2/addbook', views.add_book_with_form, name='add_book_with_form'),
    path('lab9_part2/editbook/<int:id>', views.edit_book_with_form, name='edit_book_with_form'),
    path('lab9_part2/deletebook/<int:id>', views.delete_book_with_form, name='delete_book_with_form'),
    path('students/', views.list_students, name='list_students'),
    path('students/add', views.add_student, name='add_student'),
    path('students/edit/<int:id>', views.edit_student, name='edit_student'),
    path('students/delete/<int:id>', views.delete_student, name='delete_student'),
        path('students2/', views.list_students2, name='list_students2'),
    path('students2/add', views.add_student2, name='add_student2'),
    path('students2/edit/<int:id>', views.edit_student2, name='edit_student2'),
    path('students2/delete/<int:id>', views.delete_student2, name='delete_student2'),
]
