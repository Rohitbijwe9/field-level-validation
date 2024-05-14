from rest_framework import serializers
from . models import Order




class Orderserializer(serializers.Serializer):
    oid=serializers.IntegerField()
    oname=serializers.CharField(max_length=20)
    address=serializers.CharField(max_length=20)
    price=serializers.IntegerField()


    def validate_oname(self,value):
        if len(value)<5 or len(value)>300:
            raise serializers.ValidationError('oname minimum 5 char and maximum 300 charactor')
        return value
    

    def validate_address(self,value):
        if len(value)<10:
            raise serializers.ValidationError('address charactor must be 10')
        return value
    
    def validate_price(self,value):
        if value<1:
            raise serializers.ValidationError('price must be positive')
        return value
    




            
            