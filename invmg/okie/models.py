from django.db import models

# Create your models here.
class Device(models.Model):#name of the table
    type=models.CharField(max_length=100,blank=False)#name of the column
    price=models.IntegerField()
    choices=(
        ('AVAILABLE','item ready to be purchased'),
        ('SOLD','item sold'),
        ('RESTOCKING','item to be restocked')
    )
    status=models.CharField(max_length=10,choices=choices,default="Sold")#avail sold or Restocking
    issues=models.CharField(max_length=100,default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type : {0} Price : {1} Status : {2}'.format(self.type,self.price,self.status)
class Laptop(Device):
    pass
class Desktop(Device):
    pass
class Mobile(Device):
    pass


