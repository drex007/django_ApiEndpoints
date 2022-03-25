from django.urls import path,include
from . import views 

urlpatterns =[
        # path('<int:pk>/', views.product_listMixin_view), products detail
       path('<int:pk>/', views.product_detail_view, name="product-detail"),
        path('create/', views.product_listMixin_view),
       # path('create/', views.product_create_view), create ordiucts
       path('<int:pk>/update/', views.product_update_view),
       path('<int:pk>/delete/', views.product_destroy_view),
       path('', views.product_listview, name= "products-list"),
#        path('', views.product_listMixin_view), listproducts
]