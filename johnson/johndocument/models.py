from django.db import models
from account.models import Distributor, Customer, Item

# Create your models here.
#
# class DetailSales(models.Model):
#     Sales_Item_Code = models.ForeignKey(Item, on_delete=models.CASCADE)
#     Sales_Quantity = models.PositiveIntegerField()
#     Sales_Rate = models.DecimalField(max_digits=10, decimal_places=2)
#     Sales_Serial_No = models.CharField(max_length=50)
#     Sales_Batch = models.CharField(max_length=30, null=True, blank=True)
#     Sales_Discount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
#     Total_Amount = models.DecimalField(max_digits=20, decimal_places=2)
#     Reference_No = models.CharField(max_length=50, null=True, blank=True)
#
#     def __str__(self):
#         return self.Sales_Item_Code



# class Sales(models.Model):
#     Bill_Date = models.DateField()
#     Invoice_No = models.CharField(max_length=50)
#     Tally_MasterID = models.CharField(max_length=15, null=True, blank=True)
#     Total_Inventory_Amount = models.DecimalField(max_digits=2,decimal_places=2, null=True, blank=True)
#     Total_GST = models.DecimalField(max_digits=20,decimal_places=2, null=True, blank=True)
#     SGST_AMOUNT = models.DecimalField(max_digits=20,decimal_places=2 , null=True, blank=True)
#     CGST_AMOUNT = models.DecimalField(max_digits=20,decimal_places=2, null=True, blank=True)
#     IGST_AMOUNT = models.DecimalField(max_digits=20,decimal_places=2, null=True, blank=True)
#     Cash_Discount_Amount = models.DecimalField(max_digits=20,decimal_places=2, null=True, blank=True)
#     R_O_Amount = models.DecimalField(max_digits=20,decimal_places=2,null=True, blank=True )
#     Total_Invoice_Amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
#
#
#     def __str__(self):
#         return self.Total_Invoice_Amount

