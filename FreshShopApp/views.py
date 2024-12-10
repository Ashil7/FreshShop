from django.shortcuts import render, redirect,get_object_or_404
from .models import productModel
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .models import profile, cart

# Create your views here.
def home(request):
    return render(request,'sitepages/base.html')

def view_products(request):
    items=productModel.objects.all()
    paginator=Paginator(items,4)
    page_no=request.GET.get('page')
    try:
        page=paginator.get_page(page_no)
    except:
        page=paginator.get_page(paginator.num_pages)
    return render(request,'sitepages/view_products.html',{'items':page})

def user_registration(request):
    if request.method=='POST':

        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.info(request,"Email Taken")
            return redirect('user_registration')
        else:
            user=User.objects.create_user(username=user_name,email=email,password=password)
            user.save()

            profobj=profile(user=user, mobile=mobile)
            profobj.save()

            print("user created")
                      
    return render(request,'user/reg.html')

def Login(request):
    message=None
    if request.method=='POST':
        user_name=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=user_name,password=password)
        if user:
            login(request,user)
            return redirect('products')
        else:
            message="Invalid credentials"
            print(message)
            return render(request,'user/login.html',{'message':message})
            
    return render(request,'user/login.html')

def add_to_cart(request,product_id):
    if request.user.is_authenticated:
        product=get_object_or_404(productModel,id=product_id)
        print(product)
        exists=cart.objects.filter(user=request.user,product=product).first()
        if exists:
            exists.quantity+=1
            exists.save()
        else:
            new_cart_item=cart(user=request.user,product=product,quantity=1)
            new_cart_item.save()
        return redirect('products')
    else:
        return redirect('login')

def view_cart(request):
    if request.user.is_authenticated:
        cartitems=cart.objects.filter(user=request.user)
        for item in cartitems:
            item.total_price = item.product.price * item.quantity

        total_price = sum(item.total_price for item in cartitems)
        return render(request,'sitepages/view_cart.html',{'cartitems':cartitems,'total_price':total_price})
    else:
        return redirect('login')

def remove_cart(request,item_id):
    cartitem=get_object_or_404(cart,id=item_id, user=request.user)
    cartitem.delete()
    return redirect('view_cart')

def update_quantity(request, product_id, action):

    cart_item = cart.objects.get(product_id=product_id,user=request.user)
    
    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease':
        if cart_item.quantity > 1:  
            cart_item.quantity -= 1
        else:
            cart_item.delete() 
            return redirect('view_cart')

    cart_item.save()
    return redirect('view_cart')

def Logout(request):
    logout(request)
    return redirect('login')

def checkout(request):
    return render(request,'sitepages/checkout.html')

def search_product(request):
    query=request.GET.get('q')
    if query:
        results=productModel.objects.filter(name__icontains=query)
    else:
        results=productModel.objects.none()
    paginator=Paginator(results,4)
    page_no=request.GET.get('page')
    page=paginator.get_page(page_no)

    return render(request,'sitepages/search.html',{'items':page,'query':query})