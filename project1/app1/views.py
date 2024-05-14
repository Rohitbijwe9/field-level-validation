from rest_framework.generics import CreateAPIView,RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .models import Order
from .serializer import Orderserializer

class Orderview(CreateAPIView,RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = Orderserializer
    lookup_field = 'pk'  # Assuming your primary key field is named 'pk'

class OrderListView(ListAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = Orderserializer