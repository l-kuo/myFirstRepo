from django.shortcuts import render, redirect
from .models import Product


list_of_dict = [
    {"id": "1", "name": "Tom", "created_at": "10"},
    {"id": "2", "name": "Toms", "created_at": "101"},
    {"id": "3", "name": "Tomss", "created_at": "1011"}
]


def all(request):
    # context={"title":"Home Page","dict":list_of_dict}
    return render(request, "category/all.html", {"dict": Product.objects.all()})


def create(request):
    return render(request, "category/create.html")


def edit(request):
    return render(request, "category/edit.html")


def product(request):
    return render(request, "category/product.html")


def delete(request):
    return redirect("cat-all")
