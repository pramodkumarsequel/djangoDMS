from django.db import models
from account.models import (Distributor, Sales, FieldMaster,User, Zone, RoleMaster, Warehouse, Item)
from reportsapp.Choices import choice_Document_type




# Create your models here.

class Event(models.Model):
    start_date = models.DateField(verbose_name="Start Date")
    start_time = models.TimeField(verbose_name="Start Time")
    start_datetime = models.DateTimeField(verbose_name='Start DateTime')
    start_month = models.CharField(max_length=50, verbose_name='Start Month')
    start_year = models.CharField(max_length=50, verbose_name='Start Year')
    created_on = models.DateField(auto_now_add=True, verbose_name='Created on')
    updated_on = models.DateField(auto_now=True, verbose_name='Updated on')


class FieldMaster(models.Model):
    DocType = models.CharField(max_length=50)
    Field_Name = models.CharField(max_length=50)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Field_Name


class ReportsMaster(models.Model):
    choice_Date_Type = (
        ('Creation Date', 'Creation Date'),
        ('Date', 'Date'),
    )
    Document_Type = models.CharField(max_length=50, blank=True, null=True, choices=choice_Document_type,
                                     verbose_name="Document Type")
    fields = models.ForeignKey(FieldMaster, on_delete=models.CASCADE, verbose_name="Field Type", null=True, blank=True)
    value = models.CharField(max_length=50, null=True, blank=True, verbose_name="Value")
    Date_Type = models.CharField(max_length=50, blank=True, null=True,verbose_name="Date Type")
    From_Date = models.DateField(verbose_name="From Date")
    To_Date = models.DateField(verbose_name="To Date")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Document_Type


class MainMenu(models.Model):
    menucode = models.IntegerField()
    menuname = models.CharField(max_length=100)
    menutype = models.IntegerField()
 
    def __str__(self):
        return self.menuname


class MenuMaster(models.Model):
    MenuName= models.CharField(max_length=50, unique=True, verbose_name="Menu Name")
    Pmenu = models.IntegerField(default=0,verbose_name="Root Menu")
    pagelink = models.CharField(max_length=50, null=True, blank=True, verbose_name="Page Link")
    Dord = models.IntegerField(null=True, blank=True, verbose_name="Display Order")
    Image = models.ImageField(upload_to="MenuMaster/Images",null=True, blank=True)
    faicon = models.CharField(max_length=50 ,null=True, blank=True)
    Roles = models.CharField(max_length=100, null=True, blank=True, verbose_name="Role")
    usrole = models.ManyToManyField(RoleMaster, null=True, blank=True, verbose_name="ROLE")
    IsMobile = models.BooleanField(default=False)
    MTYPE = models.CharField(max_length=20, null=True, blank=True, verbose_name="Menu Type")
    Is_View = models.BooleanField(default=False, verbose_name="Is View")
    Is_Create = models.BooleanField(default=False, verbose_name="Is Create")
    is_Edit = models.BooleanField(default=False, verbose_name="Is Edit")
    is_Delete = models.BooleanField(default=False, verbose_name="Is Delete")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        ordering = ['Dord']
  
    def __str__(self):
        return self.MenuName
    
    
    def get_pagelink(self):
        return f'{self.MenuName}'
    
    def iscreate(self):
        return self.Is_Create
    
    def isedit(self):
        return self.Is_View
    
    def isdelete(self):
        return self.is_Delete



class RoleAssignment(models.Model):
    EID = models.PositiveIntegerField(blank=True, null=True)
    UID = models.PositiveBigIntegerField()
    ROLEID = models.PositiveIntegerField(null=True, blank=True)
    distributors =models.ManyToManyField(Distributor, null=True, blank=True , verbose_name="Distributor")
    zones =models.ManyToManyField(Zone,null=True, blank=True, verbose_name="Zone")
    documents =models.ManyToManyField(ReportsMaster,null=True, blank=True, verbose_name="Document Type")
    fld1 = models.CharField(max_length=500, null=True, blank=True)
    fld2 = models.CharField(max_length=300, null=True, blank=True)
    fld3 = models.CharField(max_length=300, null=True, blank=True)
    fld4 = models.CharField(max_length=300, null=True, blank=True)
    fld5 = models.CharField(max_length=300, null=True, blank=True)
    fld6 = models.CharField(max_length=300, null=True, blank=True)
    fld7 = models.CharField(max_length=300, null=True, blank=True)
    fld8 = models.CharField(max_length=300, null=True, blank=True)
    fld9 = models.CharField(max_length=300, null=True, blank=True)
    fld10 = models.CharField(max_length=300, null=True, blank=True)
    fld11 = models.CharField(max_length=300, null=True, blank=True)
    rolename = models.CharField(max_length=50)
    documenttype = models.CharField(max_length=50)
    iscreate = models.BooleanField(default=False)
    isedit = models.BooleanField(default=False)
    isview = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.distributors)

    def has_create(self):
        return self.iscreate
    
    def has_view(self):
        return self.isview
    
    def has_edit(self):
        return self.isedit
    

class stockstatement(models.Model):
    document_type=models.CharField(max_length=50,verbose_name="Document Type")
    docid=models.IntegerField(default=0, verbose_name="Document ID")
    doc_date=models.DateField(verbose_name="Document Date")
    warehouse_id=models.IntegerField(default=0,verbose_name="Warehouse ID")
    w_house = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    warehouse_name=models.CharField(max_length=50,verbose_name="Warehouse Name")
    items=models.IntegerField(default=0,verbose_name="Item ID")
    itm = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_name=models.CharField(max_length=50,verbose_name="Item Name")
    Qty=models.IntegerField(default=0, verbose_name="Quantity")
    uom=models.CharField(max_length=50, verbose_name="UOM", null=True)
    amount=models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Amount")
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    
    

class Qtystatement(models.Model):
    document_type=models.CharField(max_length=50,verbose_name="Document Type")
    docid=models.IntegerField(default=0, verbose_name="Document ID")
    document_order_no = models.CharField(max_length=100, null=True, blank=True)
    doc_date=models.DateField(verbose_name="Document Date")
    warehouse_id=models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name="Warehouse ID", null=True, blank=True)
    warehouse_name=models.CharField(max_length=50,verbose_name="Warehouse Name")
    items=models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Item ID", null=True, blank=True)
    item_name=models.CharField(max_length=50,verbose_name="Item Name")
    Qty=models.IntegerField(default=0, verbose_name="Quantity")
    uom=models.CharField(max_length=50, verbose_name="UOM", null=True)
    amount=models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Amount")
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="Created Date")    
        