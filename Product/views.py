from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse

# Create your views here.
from Product.models import Product
from Product.models import CartItem


@login_required
def addToCart_view(req, id):
    if req.method == "POST":
        qty = req.POST.get('qty')
        product = Product.objects.get(pk = id)
        user = req.user

        cartItem = CartItem.objects.create(user=user, product=product, quantity=qty)
        cartItem.save()

        data = Product.objects.get(id=id)
        context = {
            'product': data
        }
        return render(req, "prodDetails.html", context)
    else:
        return HttpResponse("get req to add to cart")


@login_required
def products_view(request):
    data = Product.objects.all()
    context = {
        'products':data
    }
    return render(request, "viewProd.html", context)


@login_required
def prodDetails_view(request, id):
    data = Product.objects.get(id=id)
    context = {
        'product': data
    }
    return render(request, "prodDetails.html", context)


@login_required
def showCart_view(req):
    user = req.user
    products = CartItem.objects.filter(user = user)

    bill=0

    for obj in products:
        bill+=(obj.quantity*obj.product.price)
        pass

    context = {
        'products': products,
        'bill' : bill
    }

    return render(req, "cart.html", context)


@login_required
def removeCartItem(req,id):
    CartItem.objects.get(pk=id).delete()
    user = req.user
    products = CartItem.objects.filter(user=user)

    bill = 0

    for obj in products:
        bill += (obj.quantity * obj.product.price)
        pass

    context = {
        'products': products,
        'bill': bill
    }

    return render(req, "cart.html", context)
