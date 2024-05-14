from django.urls import path
from .views import Orderview,OrderListView



urlpatterns=[
   path('order/', Orderview.as_view(), name='order-detail'),
    path('order-list/<int:pk>/', OrderListView.as_view(), name='order-list'),
]