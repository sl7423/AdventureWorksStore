from django.shortcuts import render, get_object_or_404
from .models import Category, Detail, Product
from django.forms import ModelForm
from django.views.generic import ListView, View
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q
import pandas as pd


class AllProductList(ListView):
    template_name = 'store/store.html'
    model = Product

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['products'] = self.get_queryset()
        return context


class Search(View):
    template_name = 'store/store.html'

    def get(self, request, **kwargs):
        keyword = request.GET['keyword']
        context = {}
        if keyword:
            context['products'] = Detail.objects.filter(Q(subcategory__icontains=str(keyword)))
            context['categories'] = Category.objects.all()
            context['keyword'] = keyword
            return render(request, self.template_name, context)
        else:
            print("NO!")
            context['products']  = Product.objects.all()
            context['categories'] = Category.objects.all()
            return render(request, self.template_name, context)
    

class BaseMixin:
    model = None #You will get all products
    base = None #You will only get some of the products 

    def get_queryset(self, **kwargs):
        category = get_object_or_404(self.base, productcategoryid=kwargs['productcategoryid'])
        return self.model.objects.filter(category=category.category, is_available='TRUE')


    def get_context_view(self, **kwargs):
        context = {
            'categories': self.base,
            'products': self.get_queryset(productcategoryid=kwargs['productcategoryid']),
        }
        return context


    def get(self, request, **kwargs):
        context = self.get_context_view(productcategoryid=kwargs.get('productcategoryid'))
        return render(request, self.template_name, context)



class ProductListByCategoryView(BaseMixin, ListView):
    template_name = 'store/store.html'
    model = Product
    base = Category.objects.all()



class ProductNewView(View):
    template_name = 'store/product.html'

    def get_context_view(self, **kwargs):
        context = {
            'subcategories': Detail.objects.filter(productcategoryid=kwargs['productcategoryid'], productsubcategoryid = kwargs['productsubcategoryid']),
            'subcategory': Product.objects.filter(productsubcategoryid=kwargs['productsubcategoryid'])
        }
        return context


    def get(self, request, *args, **kwargs):
        productcategoryid = kwargs.get('productcategoryid')
        productsubcategoryid = kwargs.get('productsubcategoryid')
        context = self.get_context_view(productcategoryid=productcategoryid, productsubcategoryid=productsubcategoryid)
        return render(request, self.template_name, context)


class ProductDetailView(View):
    template_name = 'store/product_detail.html'

    def get_similar_products(self, productID):
        correlation_matrix = pd.read_csv('store/Data/Similarity_Products.csv')
        correlation_matrix.set_index('ProductID', inplace=True)
        final_table = correlation_matrix[str(productID)].sort_values(ascending=False)[1:] #We don't care about the top item because that value 
        return list(final_table.index[:5])

    def get_context_view(self, **kwargs):

        products = Detail.objects.filter(productcategoryid=kwargs['productcategoryid'], productsubcategoryid = kwargs['productsubcategoryid'], productid = kwargs['productid'])

        top5similarproducts = self.get_similar_products(products.values_list('productid', flat=True).get(productid=kwargs['productid'])) 

        context = {
            'products': products,
            'similar_products': Detail.objects.filter(productid__in=top5similarproducts),
        }
        return context


    def get(self, request, *args, **kwargs):
        productcategoryid = kwargs.get('productcategoryid')
        productsubcategoryid = kwargs.get('productsubcategoryid')
        productid = kwargs.get('productid')

        context = self.get_context_view(productcategoryid=productcategoryid, productsubcategoryid=productsubcategoryid, productid = productid)

        return render(request, self.template_name, context)


