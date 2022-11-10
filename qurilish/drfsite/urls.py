from django.urls import path, include, re_path

from drfsite.views import Listrest, CategoryList, Listrestdetail, detail, ProductdataList, adslist,Categortsearch, Listrestdetailandroid,CategoryListAndroid,adslistandroid,CityAndroid
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'data', Listrestdetail, basename='Products')
router.register(r'data', Listrest, basename='Products')
appname = 'drfsite'
urlpatterns = [
   path("v1/", include(router.urls)),
   path("v1/category/", CategoryList.as_view({'get': 'list'})),
   path("v1/category/filter/", Categortsearch.as_view()),
   path("v1/categoryandroid/", CategoryListAndroid.as_view({'get': 'list'})),
   path("v1/two/", Listrest.as_view({'get': 'list'})),
   path("v1/CityAndroid/", CityAndroid.as_view({'get': 'list'})),
   path("v1/adslistandroid/", adslistandroid.as_view({'get': 'list'})),
   path("v1/ads/", adslist.as_view({'get': 'list'})),
   path("v1/adslistandroid/", adslistandroid.as_view({'get': 'list'})),
   path("v1/two/android/", Listrestdetailandroid.as_view({'get': 'list'})),
   path("v1/two/category/android/", CategoryListAndroid.as_view({'get': 'list'})),
   path('v1/posts/<int:id>/',detail ),
   path('v1/drf_login/', include('rest_framework.urls')),
   path('v1/drf_auth/', include('djoser.urls')),
   re_path(r'^auth/', include('djoser.urls.authtoken')),
   path("v1/productdata/", ProductdataList.as_view({'get': 'list'})),
]

# from django.urls import path, include, re_path
#
# from drfsite.views import Listrest
# from rest_framework import routers
# router=routers.DefaultRouter()
# router.register(r'data',Listrest,basename='Products')
#
# appname='drfsite'
# urlpatterns=[
#    path("v1/",include(router.urls)),
#    path('v1/drf_login/',include('rest_framework.urls')),
#    path('v1/drf_auth/',include('djoser.urls')),
#    re_path(r'^auth/',include('djoser.urls.authtoken')),
# ]