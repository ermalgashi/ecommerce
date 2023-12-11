from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category
# from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required(login_url="/admin")
def home_view(request, cat_slug=None):
    # Gets products from DB with unqiue Id. to get all products you use Products.objects.all()
    if cat_slug:
        get_category_id = Category.objects.get(slug=cat_slug)
        products = Product.objects.all().filter(category=get_category_id)
    else:
        products = Product.objects.all()

    # return HttpResponse(f"This is the home view, this is the {products.price}")
    return render(request, "home.html", {"products": products})
