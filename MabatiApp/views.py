from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Contact, ImageModel, Category, CartItem, Register
from MabatiApp.forms import ImageUploadForm, ContactForm, ProductForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test



# Create your views here.
def home(request):
    return render(request, 'home.html')


def base(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about.html')


def product_details(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', {'product': product})


def products(request,category='all'):
    if category == 'all':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category=category)

    return render(request, 'products.html', {'products': products, 'category': category})

def checkout(request):
    return render(request, 'checkout.html')


def order_confirmation(request):
    return render(request, 'order_confirmation.html')


def register_user(request):
    if request.method == 'POST':
        form = Register(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password']
        )
        form.save()
        return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
       if Register.objects.filter(
           username = request.POST['username'],
           password = request.POST['password']
       ).exists():
           members = Register.objects.get(
               username = request.POST['username'],
               password = request.POST['username']
           )
           return render(request, 'dashboard.html', {'members': members})
       else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


@login_required
def dashboard(request):
    user = request.user
    cart_items = user.cartitem_set.all()
    context = {
        'user': user,
        'cart_items': cart_items,
        'user_history': []
    }
    return render(request, 'dashboard.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
        else:
            form = ImageUploadForm()
        return render(request, 'upload_image.html', {'form': form})


def show_image(request):
    product_images = ImageModel.objects.all()
    return render(request, 'product_details.html', {'product_images': product_images})


def image_delete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')

def contact_view(request):
    allcontacts=Contact.objects.all()
    return render(request, 'contact_view.html', {'contact': allcontacts})

def contact(request):
    if request.method == 'POST':
        contact=Contact(
            name=request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        contact.save()
        messages.success(request, "Your message has been sent successfully!")
        return redirect('/contact')
    else:
        return render(request, 'contact.html')


def delete(request,id):
    cont = Contact.objects.get(id=id)
    cont.delete()
    return redirect('/contact_view')

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def products_by_category(request,category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products.html', {'category': category, 'products': products})

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'admin_login.html', {'form': form})


def is_staff(user):
    return user.is_staff
@login_required
@user_passes_test(is_staff)
def admin_dashboard(request):
    total_products = Product.objects.count()
    total_messages = Contact.objects.count()
    context = {
        'total_products': total_products,
        'total_messages': total_messages,
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_cost = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_cost': total_cost})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    if 'quantity' in request.POST:
        cart_item.quantity = int(request.POST['quantity'])
        if cart_item.quantity < 1:
            cart_item.delete()
        else:
            cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')
