from .views import *
from django.urls import path


urlpatterns = [
    path('', all, name="cat-all"),
    path('edit/', edit, name="cat-edit"),
    path('product/', product, name="cat-product"),
    path('create/', create, name="cat-create"),
    path('delete/', delete, name="cat-delete")
]



    