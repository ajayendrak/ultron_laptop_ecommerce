from django.shortcuts import render, HttpResponse, redirect
from .models import Product
from math import ceil
from django.contrib import messages


# Create your views here.



def tracker(request):
    return HttpResponse(".............tracker")

def search(request):
    return HttpResponse(".............search")

def productadd(request):
    if request.method == 'POST' :
        
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        sub_category = request.POST.get('sub_category')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        pub_date = request.POST.get('pub_date')
        image = request.FILES.get('image')
        r_info = Product(product_name=product_name, category=category, sub_category=sub_category, price=price, desc=desc, pub_date=pub_date, image=image)
        print(r_info)
        r_info.save()
        messages.success(request, 'Product uploaded in database successfuly.')
    
    return render(request, 'productsform.html')

def accessories_page(request):

    products=Product.objects.filter(category='accessories')
    print(products)

    n=len(products)
    nRows=n//3 + ceil((n/3)-(n//3))
    params = {'no_of_rows':nRows, 'range': range(nRows), 'product':products}

    return render(request, 'accessories_page.html', params)


def checkout(request):
    return HttpResponse(".............checkout")

def products_page(request):
    
    products=Product.objects.filter(category='laptops')
    print(products)


    n=len(products)
    nRows=n//3 + ceil((n/3)-(n//3))
    params = {'no_of_rows':nRows, 'range': range(nRows), 'product':products}




    return render(request, 'products_page.html', params)


# imp views edited 
    # productid=request.POST.get('productid')
    # print(productid)
    # print('djnfjgejng')


    # myfile = request.FILES['myfile']
    # fs = FileSystemStorage()
    # filename = fs.save(myfile.name, myfile)
    # uploaded_file_url = fs.url(filename)





    
    