# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Product

# def home(request):
#     return HttpResponse("Welcome to CampusKart 🚀")

# def home(request):
#     products = Product.objects.all().order_by('-created_at')
#     return render(request, 'marketplace/home.html', {'products': products})

# from django.shortcuts import render, redirect
# from .forms import ProductForm

# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.seller = request.user   # seller assign
#             product.save()
#             return redirect('home')
#     else:
#         form = ProductForm()

#     return render(request, 'marketplace/add_product.html', {'form': form})

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import ProductForm

# @login_required
# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.seller = request.user
#             product.save()
#             return redirect('home')
#     else:
#         form = ProductForm()

#     return render(request, 'marketplace/add_product.html', {'form': form})

# from django.shortcuts import get_object_or_404

# def product_detail(request, id):
#     product = get_object_or_404(Product, id=id)
#     return render(request, 'marketplace/product_detail.html', {'product': product})

# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
# from django.shortcuts import render, redirect

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']

#         user = User.objects.create_user(username=username, email=email, password=password)
#         login(request, user)
#         return redirect('home')

#     return render(request, 'marketplace/register.html')

# from django.contrib.auth import authenticate, login

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user:
#             login(request, user)
#             return redirect('home')

#     return render(request, 'marketplace/login.html')

# from django.contrib.auth import logout

# # def user_logout(request):
# #     logout(request)
# #     return redirect('home')

# from django.contrib.auth import logout
# from django.shortcuts import redirect

# def user_logout(request):
#     logout(request)
#     return redirect('home')

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm


# 🔥 Home Page
# def home(request):
#     products = Product.objects.all().order_by('-created_at')
#     return render(request, 'marketplace/home.html', {'products': products})
def home(request):
    query = request.GET.get('q')   # search input

    if query:
        products = Product.objects.filter(title__icontains=query).order_by('-created_at')
    else:
        products = Product.objects.all().order_by('-created_at')

    return render(request, 'marketplace/home.html', {'products': products})



# 🔥 Add Product (Login required)
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, 'marketplace/add_product.html', {'form': form})


# 🔥 Product Detail
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'marketplace/product_detail.html', {'product': product})


# 🔥 Register
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # duplicate username check
        if User.objects.filter(username=username).exists():
            return render(request, 'marketplace/register.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'marketplace/register.html')


# 🔥 Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'marketplace/login.html', {'error': 'Invalid credentials'})

    return render(request, 'marketplace/login.html')


# 🔥 Logout
def user_logout(request):
    logout(request)
    return redirect('home')
