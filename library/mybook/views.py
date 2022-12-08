from multiprocessing import context
from django.shortcuts import render, redirect
from mybook.models import Author, Book, District, Branches
from mybook.forms import Shippingform
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login,authenticate, logout
from django.db.models import Q
from django.http import HttpResponseRedirect

from cartpage.models import PurchasModel,items
# user hook pass 12345
# Create your views here.


def home(request):
    districts=District.objects.all()
    return render(request, 'home.html',{'districts':districts})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username alredy Exits!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email alredy Exits!')
                return redirect('register')
            else:
                data = User.objects.create_user(username=username, email=email, password=password)
                data.save()
                messages.success(request,"User Created Successfully!")
                user = authenticate(username=username,password=password)
                auth_login(request,user)
                return redirect('login')

        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'registration/register.html', {'messages': messages})

def login(request):
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user, password=password)
        
        if user is not None:
            
            auth_login(request,user)
            return redirect('fillform')
    return render(request, 'registration/login.html')
def logout(request):
    return redirect('login')
def branch(request):
    brjs = District.objects.all()
    return render(request, 'branche.html', {'bjs': brjs})
def branches(request,area):
    area=District.objects.get(id=area)
    braju=Branches.objects.filter(DistricNM=area)
    return render(request, 'branche.html',{'brej':braju})

def fillform(request):
    if request.method == "POST":
        form = Shippingform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Shippingform()
    return render(request,'formview.html',{'frm':form})

def view_authors(request):
    author_names = Author.objects.all()
    return render(request, 'auther.html', {"author_names": author_names})

def author_books(request, id):
    author_name = Author.objects.get(id=id)
    author_books = Book.objects.filter(book_author=author_name)
    return render(request, 'author_books.html', {
        
        "author_books": author_books
        })

def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Book.objects.all().filter(Q(book_name__contains=query)| Q(desc__contains=query))

    return render(request, 'search.html', {'qr': query, 'pr': prod})
def despatch(request):
    person = User.objects.get(id=request.user.id)
    my_orders=PurchasModel.objects.all().filter(customer=person)

    orders=[]
    if len(my_orders)>0:
        for i in range(len(my_orders)):
            order=my_orders[i].order
            orders.append(order)
        products=items.objects.all().filter(cart__in=orders) 
    else:
        products=[]

    return render(request,'despatch.html',{'orders':my_orders,'products':products,})


def load_branches(request):
    districtId=request.GET.get('district')

    print(districtId)

    district=District.objects.get(id=districtId)

    print(district)

    branches=Branches.objects.all().filter(DistricNM=district)

    print(branches)
    return render(request,"branches.html", {'branches':branches})




