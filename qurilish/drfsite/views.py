from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, GenericViewSet

import shop.models
from shop.models import Product, Category,ads,City
from .serialesers import productserialers, categoryserialers, productserialersdetail, adsserialers, \
    categoryserialers,cityserialers
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.pagination import PageNumberPagination

class any(BasePermission):
    def has_permission(self, request, view):
        return True

class pag(PageNumberPagination):
    page_size=20
    page_size_query_param='page_size'
    max_page_size=10000000


class adslist(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,

               GenericViewSet):
    serializer_class = adsserialers
    permission_classes = (AllowAny,)
    def get_queryset(self):



        queryset = ads.objects.all()
        return queryset


class Listrestdetail(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,

               GenericViewSet):
    serializer_class = productserialersdetail
    permission_classes = (AllowAny,)
    pagination_class = pag
    def get_queryset(self):



        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        city = self.request.query_params.get('city')
        if category is not None:
            queryset = queryset.filter(category__slug=category)
            if city is not None:
                queryset = queryset.filter(city__slug=city)
        return queryset.order_by('created')

    @action(methods=['get', 'post'], detail=False)
    def category(self, request):
        cat = categoryserialers(Category.objects.all())
        return Response({"category": [car.image for car in cat]})

@csrf_exempt
def detail(request,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=="GET":
        serializer=productserialersdetail(product)
        return JsonResponse(serializer.data)
    elif request.method=="PUT":
        data=JSONParser().parse(request)
        serializer=productserialersdetail(product,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method=="DELETE":
        product.delete()
        return HttpResponse(status=204)


class Listrest(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,

               GenericViewSet):
    serializer_class = productserialers
    permission_classes = (AllowAny,)
    pagination_class = pag
    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category__slug=category)
        return queryset

    @action(methods=['get', 'post'], detail=False)
    def category(self, request):
        cat = categoryserialers(Category.objects.all())
        return Response({"category": [car.image for car in cat]})


class CategoryList(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,

                   GenericViewSet):
    serializer_class = categoryserialers
    permission_classes = (AllowAny,)

    def get_queryset(self):
        pk = shop.models.Category.objects.all()
        print(pk)
        if not pk:
            return Category.objects.all()[:10]

        return Category.objects.all().order_by('pk')
class ProductdataList(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,

                   GenericViewSet):
    serializer_class = productserialers
    permission_classes = (AllowAny,)
    pagination_class = pag
    def get_queryset(self):
        pk = shop.models.Product.objects.all()
        print(pk)


        return Product.objects.all().order_by('created')

class Categortsearch(generics.ListAPIView):
    """
    GET
    """
    queryset = Category.objects.all()
    serializer_class = categoryserialers
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields=('slug','slugone')
    search_fields=('slug','slugone')
    pagination_class = pag
# from rest_framework import generics, viewsets, mixins
# from rest_framework.decorators import action
# from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.viewsets import ViewSet, GenericViewSet
#
# from shop.models import Product, Category
# from .serialesers import productserialers
#
# class any(BasePermission):
#     def has_permission(self, request, view):
#         return True
#
# class Listrest(mixins.CreateModelMixin,
#                    mixins.ListModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#
#                    GenericViewSet):
#
#     serializer_class = productserialers
#     permission_classes = (IsAdminUser,)
#     def get_queryset(self):
#         pk=self.kwargs.get('pk')
#         if not pk:
#             return Product.objects.all()[:3]
#
#         return Product.objects.filter(pk=pk)
#     @action(methods=['get','post'],detail=True)
#     def category(self,request,pk=None):
#         cat=Category.objects.get(pk=pk)
#         return Response({"category":cat.name})
#







    # def get(self,request):
    #
    #     data = Product.objects.all()
    #
    #     return Response({'get':productserialers(data,many=True).data})
    # def post(self,request):
    #
    #    serilazater=productserialers(data=request.data)
    #    serilazater.is_valid(raise_exception=True)
    #    serilazater.save()
    #    return Response({"post":serilazater.data})
    #
    # def put(self,request,*args,**kwargs):
    #
    #     pk=kwargs.get('pk')
    #     print(kwargs.get("pk"))
    #     if  pk:
    #         instance=Product.objects.get(pk=pk)
    #
    #     else:
    #         return Response("id yoq")
    #
    #     serilazer=productserialers(data=request.data,instance=instance)
    #     serilazer.is_valid(raise_exception=True)
    #     serilazer.save()
    #     return Response(serilazer.data)
    #
    # def delete(self,request,*args,**kwargs):
    #     pk=kwargs.get("pk")
    #     delete=Product.objects.get(pk=pk).delete()
    #     return Response(delete)
class Listrestdetailandroid(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,

               GenericViewSet):
    serializer_class = productserialersdetail
    permission_classes = (AllowAny,)

    def get_queryset(self):



        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category__slug=category)
        return queryset.order_by('created')

    @action(methods=['get', 'post'], detail=False)
    def category(self, request):
        cat = categoryserialers(Category.objects.all())
        return Response({"category": [car.image for car in cat]})

    def list(self, request, *args, **kwargs):
        old_response_data = super(Listrestdetailandroid, self).list(request, *args, **kwargs)
        new_response_data = {"items": old_response_data.data, "count_items": len(old_response_data.data)}
        return Response(new_response_data)


class Listrestandroid(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,

               GenericViewSet):
    serializer_class = productserialers
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category__slug=category)
        return queryset

    @action(methods=['get', 'post'], detail=False)
    def category(self, request):
        cat = categoryserialers(Category.objects.all())
        return Response({"category": [car.image for car in cat]})
    def list(self, request, *args, **kwargs):
        old_response_data = super(Listrestandroid, self).list(request, *args, **kwargs)
        new_response_data = {"items": old_response_data.data, "count_items": len(old_response_data.data)}
        return Response(new_response_data)

class CategoryListAndroid(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,

                   GenericViewSet):
    serializer_class = categoryserialers
    permission_classes = (AllowAny,)

    def get_queryset(self):
        pk = shop.models.Category.objects.all()
        print(pk)
        if not pk:
            return Category.objects.all()[:10]

        return Category.objects.all().order_by('pk')

    def list(self, request, *args, **kwargs):
        old_response_data = super(CategoryListAndroid, self).list(request, *args, **kwargs)
        new_response_data = {"items": old_response_data.data, "count_items": len(old_response_data.data)}
        return Response(new_response_data)


class adslistandroid(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,

               GenericViewSet):
    serializer_class = adsserialers
    permission_classes = (AllowAny,)
    def get_queryset(self):



        pk = shop.models.ads.objects.all()

        if not pk:
            return ads.objects.all()[:10]

        return ads.objects.all().order_by('pk')

    def list(self, request, *args, **kwargs):
        old_response_data = super(adslistandroid, self).list(request, *args, **kwargs)
        new_response_data = {"items": old_response_data.data, "count_items": len(old_response_data.data)}
        return Response(new_response_data)

class CityAndroid(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,

                   GenericViewSet):
    serializer_class = cityserialers
    permission_classes = (AllowAny,)

    def get_queryset(self):
        pk = shop.models.City.objects.all()
        print(pk)
        if not pk:
            return City.objects.all()[:10]

        return City.objects.all().order_by('pk')
    def list(self, request, *args, **kwargs):
        old_response_data = super(CityAndroid, self).list(request, *args, **kwargs)
        new_response_data = {"items": old_response_data.data, "count_items": len(old_response_data.data)}
        return Response(new_response_data)