from django.db import models


STATUS=(
    ("pending","pending"),
    ("completed","completed"),
    ("canceled","canceled")
    
    )


# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=20)
    contact_details=models.TextField()
    address=models.TextField()
    vendor_code=models.CharField(max_length=100)
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()
  
    def  __str__(self):
         return self.name
     

class PurchaseOrder(models.Model):
    po_number=models.CharField(max_length=50)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name="vendor_info")
    order_date=models.DateTimeField(auto_now_add=True)    
    delivery_time=models.DateTimeField(auto_now_add=True)     
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.CharField(choices=STATUS,max_length=20)
    quality_rating=models.FloatField(blank=True, null=True)
    issue_date=models.DateTimeField(auto_now=True)
    acknowledgement_date=models.DateTimeField(auto_now=True,blank=True, null=True)
    
    def __str__(self):
        return self.vendor.name

class HistoricalPerformance(models.Model):
    venfor=models.ForeignKey(Vendor, on_delete=models.CASCADE)    
    date=models.DateTimeField(auto_now=False, auto_now_add=False)
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()