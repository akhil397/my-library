from multiprocessing import context
from django.shortcuts import render, redirect
from mybook.models import Author, Book, District, Branches
from mybook.forms import Shippingform
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login,authenticate, logout
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import uuid

from cartpage.models import PurchasModel,items
# user hook pass 12345
# Create your views here.


def home(request):
    home=True
    districts=District.objects.all()
    return render(request, 'home.html',{'districts':districts,'home':home})

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

            if not user.is_superuser:
            
                auth_login(request,user)

                return redirect('fillform')
    return render(request, 'registration/login.html')

@login_required
def Logout(request):
    logout(request)

    return redirect('home')


def branch(request):
    brjs = District.objects.all()
    return render(request, 'branche.html', {'bjs': brjs})
def branches(request,area):
    area=District.objects.get(id=area)
    braju=Branches.objects.filter(DistricNM=area)
    return render(request, 'branche.html',{'brej':braju})

def fillform(request):
    districts=District.objects.all()
    person = User.objects.get(id=request.user.id)
    if request.method == "POST":
        district_id=request.POST.get('form_district')
        branche_id=request.POST.get('form_branche')

        date=request.POST.get('Ddate')
        time=request.POST.get('Dtime')
        
        district=District.objects.get(id=district_id)
        branche=Branches.objects.get(id=branche_id)
        
        form = Shippingform(request.POST)
        if form.is_valid():

           

            
                customer_form=form.save(commit=False)
                customer_form.CBranch=district.DICSTRINM
                customer_form.CDistric=branche.BRANCHNM

                customer_form.Ddate=date
                customer_form.Dtime=time

                customer_form.customer=person

                customer_form.unique_purchase_id=str(uuid.uuid4())

                customer_form.save()

        return redirect('view_authors')
    else:
        form = Shippingform()

        

    return render(request,'formview.html',{'form':form,'districts':districts})

def view_authors(request):
    author=True
    author_names = Author.objects.all()
    return render(request, 'auther.html', {"author_names": author_names,'author':author})

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


    district=District.objects.get(id=districtId)


    branches=Branches.objects.all().filter(DistricNM=district)

    return render(request,"branches.html", {'branches':branches})



def form_load_branches(request):
    districtId=request.GET.get('district')

    district=District.objects.get(id=districtId)

    branches=Branches.objects.all().filter(DistricNM=district)

    
    return render(request,"branches.html", {'branches':branches})

def load_customer_branches(request):
    districtId=request.GET.get('district')


    district=District.objects.get(id=districtId)


    branches=Branches.objects.all().filter(DistricNM=district)


    return render(request,"branches.html", {'branches':branches})

def delete_order(request,pk):
    order=PurchasModel.objects.get(id=pk)

    order.delete()

    return redirect('view_authors')

def form_load_books(request):
    authorId=request.GET.get('author')

    author=Author.objects.get(id=authorId)

    books=Book.objects.all().filter(book_author=author)

    
    return render(request,"books.html", {'books':books})
    






