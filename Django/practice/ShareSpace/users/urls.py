from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('categories/', views.categories, name="categories"),
    path('categories/productdetails/<int:id>', views.productdetails, name="productdetails"),
    path('testing/', views.testing, name='testing'), 
]
