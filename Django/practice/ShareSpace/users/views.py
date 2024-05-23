from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, Category, Product

def members(request):
    mymembers = User.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        "mymembers": mymembers
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = User.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('test.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

def categories(request):
    categories = Category.objects.all() 
    template = loader.get_template("category.html")
    context = {
        "categories": categories
    }
    return HttpResponse(template.render(context, request))

def productdetails(request, id):
   productdetails = Product.objects.get(id=id)
   template = loader.get_template("productdetails.html")
   context = {
      "productdetails": productdetails
   }
   return HttpResponse(template.render(context, request))