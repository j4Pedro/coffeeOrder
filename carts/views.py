from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Cart, CartItem
from products.models import Product

def view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart":cart}
    else:              #沒作用要修改，先改從cart/view.html判斷
        empty_message = " 購物車中沒有物品 "
        context = {"emty": True, "empty_message":empty_message}

    template_name = "cart/view.html"
    return render(request,template_name,context)


def update_cart(request, slug):
    request.session.set_expiry(300000)
    try:
        qty = request.GET.get('qty')
        update_qty=True
    except:
        qty = None
        update_qty=False
    notes={}
    try:
        size = request.GET.get('size')
        notes['size'] = size
    except:
        size = None
    print(size)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id  
        the_id = new_cart.id 

    cart = Cart.objects.get(id = the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart,product=product)
    if created:
        print("OK!!! cart_item, created")

    print(qty)
    print(int(qty))
 
    if update_qty and qty:
        if int(qty) <= 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.notes = notes
            cart_item.save()
    else:
        pass
    # if not cart_item in cart.items.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)

    new_total = 0.00
    for item in cart.cartitem_set.all():
        line_total = float(item.product.price) * item.quantity
        new_total += line_total

    request.session['items_total'] = cart.cartitem_set.count()

    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse("cart"))
    