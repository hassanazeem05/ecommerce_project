from django.shortcuts import render, get_object_or_404
from .models import Category, Company, Product
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Product, Order, OrderItem
from django.contrib import messages

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    companies = category.companies.all()

    return render(request, 'shop/category_detail.html', {
        'category': category,
        'companies': companies
    })
def company_detail(request, slug):
    company = get_object_or_404(Company, slug=slug)
    products = company.products.all()

    return render(request, 'shop/company_detail.html', {
        'company': company,
        'products': products
    })
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'shop/product_detail.html', {
        'product': product
    })
@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.name} added to cart.")
    return redirect('product_detail', slug=product.slug)


@login_required
def buy_now(request, product_id):
    # For Buy Now, we add to cart and go to checkout
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')
@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = sum(item.product.price * item.quantity for item in items)

    return render(request, 'shop/cart.html', {'items': items, 'total': total})
@login_required
def checkout(request):
    return render(request, 'shop/checkout.html')