from multiprocessing import context
from django.shortcuts import render, redirect
from fillform.models import PurchasModel
from mybook import views
from fillform.forms   import Shippingform
# Create your views here.
def formview(request):
    if request.method == "POST":
        form = Shippingform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Shippingform()
        return redirect('view_authors')
    return render(request,'purchase.html',{'frm':form})

def despach(request):
    context=PurchasModel.objects.all()
    return render(request,'despach.html',{"form":context})