from django.http import HttpResponse
from .models import Product
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as loginAuth, logout as logoutAuth

# Create your views here.
error = None
success= None
def signup(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2 :
            return render(request, 'signup.html', {'error': "Pssword dose not match"})
    
        if len(password1) < 8 :
            return render(request, 'signup.html', {'error': "Password length must be more than eight"})

        if User.objects.filter(username = username).exists():
            return render(request, 'signup.html', {'error': "Username already exists"})
    
        if user.objects.filter(email = email).exists():
            return render(request, 'signup.html', {'error' "This email has already been used"})
    
        user = User.objects.create_user(username = username, email = email, password = password1)
        user.save()

        Customer.objects.create(user = user)
        return redirect('login')
    return render(request, 'signup.html',{'error':error})



def login(request):
    error = None
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            loginAuth(request, user)
            return redirect("product_list")
        else:
            return render(request, 'login.html', {"error": 'invalid credentials'})
    return render(request, "storeapp/login.html")



def storeapp_view(requst):
    return HttpResponse("storeapp page")

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'storeapp/product_list.html', {'products':products})


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'storeapp/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    # Add the product or increase quantity
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    # Save back to session
    request.session['cart'] = cart

    return redirect('view_cart')  # Go to cart page after adding

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        product.quantity = quantity
        product.subtotal = product.price * quantity
        products.append(product)
        total += product.subtotal

    context = {
        'products': products,
        'total': total,
    }
    return render(request, 'storeapp/cart.html', context)
