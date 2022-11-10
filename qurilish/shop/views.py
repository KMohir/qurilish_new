from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .form import findForm
from .models import Category, Product, City


# Create your views here.

class L_List(ListView):
    queryset = Product.objects.all()
    model=Product
    form=findForm()
    template_name = 'shop/product/list.html'
    paginate_by = 7
    context_object_name = 'products'
    def get_context_data(self,**kwargs):
        context=super(L_List,self).get_context_data(**kwargs)
        context['city'] = self.request.GET.get('city')
        context['category']=self.request.GET.get('category')
        context['form']=self.form
        return context
    def get_queryset(self):
        city=self.request.GET.get('city')
        category=self.request.GET.get('category')
        qs=[]
        _filter={}
        _filter['available']=True
        if city or category:

            if city:
                category=''
                _filter['city__slug']=city
            if category:
                _filter['category__slug']=category

            qs=Product.objects.filter(**_filter)

        return qs
def list_home(request):
    form = findForm()
    city = request.GET.get('city')
    category = request.GET.get('category')
    _context={'form': form,'city':request.GET.get('city'),'category':request.GET.get('category')}
    if city or category:
        _filter={}
        if city:
            _filter['city__slug']=city
        if category:
            _filter['category__slug'] = category
        v = Product.objects.filter(**_filter)
        vak = Paginator(v,5)
        p=request.GET.get('page')
        if p:
            page=p
        else:
            page=1
        page_number = vak.page(page)

        _context.update({'product':page_number})
    return render(request,'shop/product/list.html',_context)
def product_detail(request, id, slug):
  product = get_object_or_404(Product, id=id, slug=slug)
  print(product.get_absolute_url)
  return render(request,
                      'shop/product/detail.html', 
                                        {'product':product})

