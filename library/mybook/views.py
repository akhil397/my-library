from multiprocessing import context
from django.shortcuts import render, redirect
from mybook.models import Author, Book
from mybook.forms import Purchaseform
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# user book pass 12345
# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        auth_user = (request, user)
        return redirect('/')
    return render(request, 'registration/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()

                return redirect('/')

        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'registration/register.html', {'messages': messages})


def view_authors(request):
    author_names = Author.objects.all()
    return render(request, 'auther.html', {"author_names": author_names})

def author_books(request, id):
    author_name = Author.objects.get(id=id)
    author_books = Book.objects.filter(author_name=author_name)
    return render(request, 'author_books.html', {
        
        "author_books": author_books
        })

def view_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})
def despatch(request):
    return render(request, 'despatch.html')


def purchase(request):
    if request.method == 'POST':
        pform = Purchaseform(request.POST)
        if pform.is_valid():
            pform.save()
            return redirect('despatch',)  # despach
        else:
            messages.info(request, 'Fill form Mantory')
        context['form'] = pform

    return render(request, 'purchase.html', context)

def branche(request):
    return render(request, 'branche.html')


