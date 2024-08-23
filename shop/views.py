from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from telegram_bot import send_product_message
# Create your views here.

def shop_page(request):
    products = Product.objects.all()
    if request.method =='POST':
        if request.POST['product_name'] and request.POST['amount'] and request.POST['description'] and request.POST['price'] and request.POST['discount']:
            name = request.POST['product_name']
            amount = request.POST['amount']
            description = request.POST['description']
            price = request.POST['price']
            discount = request.POST['discount']
        
            product = Product(
                name=name,
                amount=amount,
                description=description,
                price=price,
                discount=discount
            )
            product.save()
            send_product_message(product)
        
    return render(request, 'shop_page.html', {'products':products})