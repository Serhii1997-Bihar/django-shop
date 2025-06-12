from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import *
from .forms import *
from .serializers import *
from cart.forms import *
from django.db.models import Q
from django.core.paginator import Paginator
from rest_framework.views import APIView, Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

def main_pg(request):
    search_form = SearchForm(request.GET)
    query = request.GET.get('query')

    if search_form.is_valid() and query:
        all_products = ProductsModel.objects.filter(
            Q(name__icontains=query) | Q(about__icontains=query)).order_by('date').select_related('category', 'country', 'brand', 'sex')
    else:
        all_products = ProductsModel.objects.all().order_by('-date').select_related('category', 'country', 'brand', 'sex')

    paginator = Paginator(all_products, 10)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {'products': products, 'form': search_form, 'query': query}
    return render(request, 'shop_templates/main_templates.html', context)

def category_pg(request, id):
    query = request.GET.get('query')
    category_prod = ProductsModel.objects.filter(category=id).select_related('category', 'country', 'brand', 'sex')

    if query:
        category_prod = category_prod.filter(name__icontains=query)

    paginator = Paginator(category_prod, 10)
    page = request.GET.get('page')
    category = paginator.get_page(page)

    context = {
        'category': category,
        'category_id': id,
        'query': query
    }
    return render(request, 'shop_templates/category.html', context)

def brand_pg(request, id):
    query = request.GET.get('query')
    brand_prod = ProductsModel.objects.filter(brand=id).select_related('category', 'country', 'brand', 'sex')

    if query:
        brand_prod = brand_prod.filter(name__icontains=query)

    paginator = Paginator(brand_prod, 10)
    page = request.GET.get('page')
    brand = paginator.get_page(page)

    context = {
        'brand': brand,
        'brand_id': id,
        'query': query
    }
    return render(request, 'shop_templates/brand.html', context)

def detail_pg(request, id):
    product = ProductsModel.objects.get(id=id)
    sizes = product.size.all()
    cart_product_form = CartAddProductForm(sizes=sizes)
    context = {'product': product, 'sizes': sizes, 'form': cart_product_form}
    return render(request, 'shop_templates/detail.html', context)

def admin_pg(request):
    admins = AdministrationModel.objects.all().order_by('?')
    context = {'admins': admins}
    return render(request, 'shop_templates/administration.html', context)

class admins_api(viewsets.ModelViewSet):
    queryset = AdministrationModel.objects.all()
    serializer_class = AdminSerializer

