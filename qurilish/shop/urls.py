from django.urls import path
from . import views
from .views import list_home

app_name = 'shop'

urlpatterns = [
  path('', views.L_List.as_view(), name='product_list'),
  path('page/<int:page>/',list_home,name='page'),
  path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]