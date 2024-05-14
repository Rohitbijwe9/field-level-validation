from django.db import models



class Order(models.Model):
    oid=models.IntegerField(primary_key=True)
    odate=models.DateTimeField(auto_now_add=True)
    oname=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    price=models.IntegerField()


    def __str__(self,request):
        return self.oname
