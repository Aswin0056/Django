from django.shortcuts import render, get_object_or_404 , redirect
from .models import Product, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import JsonResponse , HttpResponse
from django.contrib import messages
from .models import Product 
from django.contrib.auth.decorators import login_required
from .forms import AddressForm





### Home

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'home.html', context)

###Category

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'category.html', context)

###Product

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
        'range':range(5),
    }
    return render(request, 'product.html', context)

### Cart

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})

    if str(product.id) in cart:
        cart[str(product.id)]['quantity'] += 1
    else:
        cart[str(product.id)] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': 1,
            'image': product.image.url, 
        }

    request.session['cart'] = cart
    messages.success(request, f'{product.name} added to the cart.')

    return redirect('cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())

    return render(request, 'view_cart.html', {'cart': cart, 'total_price': total_price})


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    

    
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        messages.success(request, "Item removed from cart.")
    
    return redirect('cart')

###Payment 

from django.shortcuts import render, redirect



def payment(request):
    # Retrieve the cart from the session
    cart = request.session.get('cart', {})
    
    # Calculate the total price
    total_price = sum(float(product['price']) * product['quantity'] for product in cart.values())
    
    if not cart:
        # If the cart is empty, redirect to the homepage or cart page
        return redirect('homepage')  # Replace 'homepage' with the appropriate view name

    if request.method == 'POST':
        # Logic to handle payment submission (e.g., validate form inputs or process payment)
        
        # For now, assume payment is successful
        request.session['cart'] = {}  # Clear the cart after successful payment
        
        # Redirect to the placed order page
        return redirect('placed_order')  # Replace with the name of the placed order view

    # If it's a GET request, render the payment page
    return render(request, 'payment.html', {'cart': cart, 'total_price': total_price})


###single payment


def single_payment(request, product_id):
   
    product = get_object_or_404(Product, id=product_id)
    context = {
        'products': [product],  
        'total_price': product.price  
    }
    return render(request, 'single_payment.html', context)
    


###signup



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


###search

 

def search(request):
    query = request.GET.get('q')  
    results = []

    if query:
        results = Product.objects.filter(name__icontains=query) 

    return render(request, 'search.html', {'query': query, 'results': results})


###Address


@login_required
def address_fillup(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, "Address saved successfully.")
            return redirect('payment')  # Redirect to the payment page
    else:
        form = AddressForm()
    return render(request, 'address.html', {'form': form})




@login_required
def single_address(request):
    if request.method == 'POST':
        print("POST request received")
        form1 = AddressForm(request.POST)
        if form1.is_valid():
            print("Form is valid")
            address = form1.save(commit=False)
            address.user = request.user
            address.save()
            print("Address saved successfully")
            messages.success(request, "Address saved successfully.")
            return redirect('single_payment')  # Ensure 'single_payment' is a valid URL name
        else:
            print("Form errors:", form1.errors)
    else:
        print("GET request received")
        form1 = AddressForm()
    return render(request, 'single_address.html', {'form': form1})


###order placed

def placed_order(request):
    return render(request, 'placed_order.html')



