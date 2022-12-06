from django.shortcuts import render, redirect
from mybook.models import Author, Book
from django.contrib.auth.models import User
from django.contrib import messages
from fillform import views
from django.contrib.auth import login as auth_login,authenticate

# user winner pass ?
# user good pass 12345
# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user, password=password)
        
        if user is not None:
            
            auth_login(request,user)
            return redirect('formview')
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
    author_books = Book.objects.filter(book_author=author_name)
    return render(request, 'author_books.html', {
        
        "author_books": author_books
        })

def despatch(request):
    return render(request, 'despatch.html')

def branche(request):
    return render(request, 'branche.html')


