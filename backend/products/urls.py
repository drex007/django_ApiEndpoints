from django.urls import path,include
from . import views 

urlpatterns =[
       path('<int:pk>/', views.product_detail_view),
       path('create/', views.product_create_view),
]