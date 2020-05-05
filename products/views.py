from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Product
from django.http import Http404
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from ecommerce.views import home_page


class FeaturedProductListView(ListView):
    model = Product
    template_name = 'products/featured_products.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data( object_list=object_list, **kwargs)
        data = Product.objects.filter(featured=True)
        context = {
            "products" : data 
        } 
        return context

class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = 'products/list.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

@login_required(login_url='login-route')
def product_list_view(request):
    qs = Product.objects.all()
    context = { 'qs' : qs }
    return render(request, 'products/product_list.html', context )

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     return context

    # def get_queryset(self, **args, **kwargs):
    #     super().get_queryset()
    #     request = self.request 
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)

@login_required
def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk)
    instance = get_object_or_404(Product, pk=pk)

    try:
        instance = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        print('No products found!')
        raise Http404('Product doesnt exist')

    context = { 'qs' : instance }
    print(context['qs'].image.url)
    return render(request, 'products/product_detail.html', context )
