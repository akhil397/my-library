from os import name
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from mybook.models import Author, Book,District,Branches
from cartpage.models import cartlist,items,PurchasModel
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User

import json

from django.http import JsonResponse

import datetime

import uuid
# Create your views here.

@login_required(login_url='login')
def cart_details(request,total=0,count=0,cart_items=None):
    person = User.objects.get(id=request.user.id)
    try:
        ct = cartlist.objects.get(customer=person,complete=False)

        ct_items = items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            total += (i.prodt.book_price*i.quan)
            count += i.quan
    except ObjectDoesNotExist:
        ct_items=[]
        total=0
        count=0
    return render(request, 'cart.html', {'ci': ct_items, 't': total, 'cn': count})

@login_required(login_url='login')
def add_cart(request,product_id):
    
    person = User.objects.get(id=request.user.id)
    prod = Book.objects.get(id=product_id)

    cart_id=str(uuid.uuid4().time_low)[0:7]
    try:
        ct = cartlist.objects.get(customer=person, complete=False)
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(customer=person,complete=False,cart_id=cart_id)
        ct.save()
    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        if c_items.quan < c_items.prodt.stock:
            c_items.quan += 1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quan=1,cart=ct)
        c_items.save()
    return redirect('cartDetails')




@login_required(login_url='login')
def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print(productId)

    
    person = User.objects.get(id=request.user.id)

    print(person)
    #prod=Book.objects.get(id=productId)
    
    ct = cartlist.objects.get(customer=person,complete=False)
    print(ct)
    prod = get_object_or_404(Book, id=productId)
    c_items = items.objects.get(prodt=prod, cart=ct)
    
    if action=="add":
        c_items.quan = (c_items.quan + 1)

    elif action=='remove':
        c_items.quan = (c_items.quan - 1)

    c_items.save()

    if c_items.quan <0:
        c_items.delete()

    return JsonResponse('Item was added',safe=False)


@login_required(login_url='login')
def checkout(request):
    person = User.objects.get(id=request.user.id)

    districts=District.objects.all()

    branches=Branches.objects.all()

    if person:
        ct= cartlist.objects.get(customer=person,complete=False)

        c_items = items.objects.all().filter(cart=ct)

        print(c_items)
    
    else:
        c_items=[]
        ct={'get_cart_toal':0,'get_cart_items':0}
    return render(request,"checkout.html",{'items':c_items,'order':ct, 'districts':districts,'branches':branches})


@login_required(login_url='login')
def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()

    data=json.loads(request.body)

    person = User.objects.get(id=request.user.id)
    print(person)

    if person:
        ct=cartlist.objects.get(customer=person,complete=False)
        total=float(data['form']['total'])
        quantity=data['form']['cart_quant']


        print(data,total,quantity)

        

        ct.complete=True

        ct.save()

        place=PurchasModel.objects.create(customer=person,order=ct, CName=data['form']['customer'], CMail=data['form']['CMail'], Bquatity=quantity,Total_Amount=data['form']['total'],  CAddress=data['shipping']['adrs'],CDistric=data['shipping']['CDistric'],CBranch=data['shipping']['CBranch'], CPhone=data['shipping']['CPhone'],CZipcode=data['shipping']['pincode'], BName=data['shipping']['BName'])

        place.save()

    else:
        print("user is not logged in")

    return JsonResponse('Payment complete',safe=False)
