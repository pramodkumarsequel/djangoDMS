from email.policy import default
from enum import unique
from random import choices
from secrets import choice
from sre_parse import Verbose
from tabnanny import verbose
from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import AbstractUser
from matplotlib.units import ConversionError
from .manager import UserManager
from django.conf import settings
# from django.db.models import ForeignKey, CASCADE, Model
from gst_field.modelfields import GSTField, PANField
from phone_field import PhoneField
from django.utils.translation import gettext_lazy as _
from account.check import doc_choice, seperator_option, TYPE_SELECT,vendor_choice
from six import text_type



# from auditlog.registry import auditlog

    
class Unit(models.Model):
    unit_class = models.CharField(max_length=50, verbose_name="Unit Class")
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.unit_class

class UOM(models.Model):
    UNT = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name="Unit Class")
    unit_notation = models.CharField(max_length=20, unique=True, verbose_name="Unit Notation")
    unit_name = models.CharField(max_length=30, unique=True, verbose_name="Unit Name")
    conversion_factor = models.DecimalField(max_digits=20, decimal_places=15, verbose_name="Conversion Factor")
    status = models.BooleanField(verbose_name="Status")
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    base_unit = models.BooleanField(verbose_name="Base Unit")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.unit_name
    

class TaxMaster(models.Model):
    tax_type = (
        ('GST','GST'),
        ('VAT','VAT'),
    )
    Tax_Type = models.CharField(choices=tax_type,max_length=20, verbose_name="Tax Type")
    name = models.CharField(max_length=30, verbose_name="Tax Name", unique=True)
    value = models.PositiveIntegerField(default=0, verbose_name="Tax Value(%)")
    CGST = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='CGST(%)')
    SGST = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='SGST(%)')
    taxinputrecoverable = models.BooleanField(default=False, verbose_name="Tax Input Recoverable")
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)
    


# Create your models here.



class RoleMaster(models.Model):
    ROLES_IN_CHOICES = (

        ('Approver', 'Approvel'),
        ('AreaSalesManager', 'AreaSalesManager'),
        ('CentralAdmin', 'CentralAdmin'),
        ('DataUploader', 'DataUploader'),
        ('DSR', 'DSR'),
        ('Execute', 'Execute'),
        ('HOADMIN', 'HOADMIN'),
        ('IT', 'IT'),
        ('OTC', 'OTC'),
        ('PIC', 'PIC'),
        ('RM', 'RM'),
        ('Rollback', 'Rollback'),
        ('SOA2', 'SOA2'),
        ('SU', 'Super User'),
        ('TEST', 'TEST'),

    )

    ROLES_TYPE_CHOICE = (
        ('SU', 'SU'),
        ('USER', 'USER'),
    )

    # id= models.PositiveSmallIntegerField(choices=ROLES_IN_CHOICES, primary_key=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Role Name")
    roletype = models.CharField(choices=ROLES_TYPE_CHOICE, max_length=100, verbose_name="Role Type")
    description = models.CharField(max_length=50, verbose_name=" Role Description")
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Role Master"

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True, unique=True)
    userid = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField()
    Phone = PhoneField(null=True, blank=True)
    Arole = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='Images', null=True, blank=True)
    isauth = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)
    role = models.ForeignKey(RoleMaster, on_delete=models.CASCADE, null=True,related_name='role_qry')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    object = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
    def get_username(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_Pic = models.ImageField(null=True, blank=True, verbose_name="Profile Pic")
    forgot_password_token = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Zone(models.Model):
    CHOICE = (
        ('Active', 'Active'),
        ('InActive', 'InActive'),
    )
    name = models.CharField(max_length=50, unique=True)
    #status = models.CharField(choices=CHOICE, max_length=10)
    isactive=models.BooleanField(default=0 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_status(self):
        return self.status

    class Meta:
        verbose_name = "Zone"


class RegionMaster(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    Region_Name = models.CharField(max_length=50, verbose_name='Region Name',unique=True)
    isactive=models.BooleanField(default=0 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.Region_Name


class StateMaster(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey(RegionMaster, on_delete=models.CASCADE)
    State_Name = models.CharField(max_length=50, verbose_name="State Name",unique=True)
    isactive=models.BooleanField(default=0 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.State_Name


class CityMaster(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey(RegionMaster, on_delete=models.CASCADE, null=True, blank=True)
    State = models.ForeignKey(StateMaster, on_delete=models.CASCADE)
    City_Name = models.CharField(max_length=50, verbose_name="City Name",unique=True)
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.City_Name


class Hierarchy1(models.Model):
    Name = models.CharField(max_length=50)
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hierarchy1"

    def __str__(self):
        return self.Name


class Hierarchy2(models.Model):
    hierarchy1 = models.ForeignKey(Hierarchy1, max_length=20, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hierarchy2"

    def __str__(self):
        return self.Name


class Hierarchy3(models.Model):
    hierarchy1 = models.ForeignKey(Hierarchy1, max_length=20, on_delete=models.CASCADE)
    hierarchy2 = models.ForeignKey(Hierarchy2, max_length=20, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hierarchy3"

    def __str__(self):
        return self.Name


class Hierarchy4(models.Model):
    hierarchy1 = models.ForeignKey(Hierarchy1, max_length=20, on_delete=models.CASCADE)
    hierarchy2 = models.ForeignKey(Hierarchy2, max_length=20, on_delete=models.CASCADE)
    hierarchy3 = models.ForeignKey(Hierarchy3, max_length=20, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hierarchy4"

    def __str__(self):
        return self.Name


class Hierarchy5(models.Model):
    hierarchy1 = models.ForeignKey(Hierarchy1, max_length=20, on_delete=models.CASCADE)
    hierarchy2 = models.ForeignKey(Hierarchy2, max_length=20, on_delete=models.CASCADE)
    hierarchy3 = models.ForeignKey(Hierarchy3, max_length=20, on_delete=models.CASCADE)
    hierarchy4 = models.ForeignKey(Hierarchy4, max_length=20, on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hierarchy5"

    def __str__(self):
        return self.Name


class Distributor(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Distributor_Name = models.CharField(max_length=100, unique=True)
    Distributor_Code = models.CharField(max_length=25, unique=True)
    Distributor_For_Code = models.CharField(max_length=30, null=True, blank=True)
    zones = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Zone')
    region = models.ForeignKey(RegionMaster, on_delete=models.SET_NULL, null=True, blank=True)
    State = models.ForeignKey(StateMaster, on_delete=models.CASCADE, null=True, blank=True)
    City = models.ForeignKey(CityMaster, on_delete=models.CASCADE, null=True, blank=True)
    Address = models.TextField(max_length=150, null=True, blank=True)
    PinCode = models.IntegerField(null=True, blank=True)
    Contact_Person_Name = models.CharField(max_length=100, null=True, blank=True)
    Contact_Number = PhoneField()
    Email_ID = models.EmailField(max_length=100, null=True, blank=True)
    gstin = GSTField()
    DL_NO = models.CharField(max_length=100, null=True, blank=True)
    DL_NO_Valid_UPTO = models.DateField(null=True, blank=True)
    pan = PANField()
    TM_Email = models.EmailField(max_length=200, null=True, blank=True)
    RIS_Email = models.EmailField(max_length=200, null=True, blank=True)
    PS_Email = models.EmailField(max_length=200, null=True, blank=True)
    PSM_Email = models.EmailField(max_length=200, null=True, blank=True)
    ASM_Email = models.EmailField(max_length=200, null=True, blank=True)
    RSM_Email = models.EmailField(max_length=200, null=True, blank=True)
    BM_Email = models.EmailField(max_length=200, null=True, blank=True)
    SH_Email = models.EmailField(max_length=200, null=True, blank=True)
    BDM_Email = models.EmailField(max_length=200, null=True, blank=True)
    HO_Email = models.EmailField(max_length=200, null=True, blank=True)
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Distributor_Code

    def get_name(self):
        return f'{self.Distributor_Code} , {self.Distributor_Name}'
    
    def getbyname(self):
        return self.Distributor_Name


class Customer(models.Model):
    CUSTOMER_CODE_CHOICE = (
        ('200253', '200253'),
        ('200326', '200326'),
        ('200385', '200385'),
        ('200625', '200625'),
        ('201184', '201184'),
        ('201494', '201494'),
        ('265848', '265848'),
        ('266684', '266684'),
        ('264104', '264104'),
        ('264101', '264101'),
    )
    
    retailer_group = (
        ('Distributor','Distributor'),
        ('Retailer','Retailer'),   
    )
    #Distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)
    Distributor = models.CharField(max_length=50, verbose_name="Distributor_Name",null=True, blank=True)
    Customer_Code = models.CharField(max_length=20, verbose_name='Retailer Code', unique=True)
    Customer_Group = models.CharField(choices=retailer_group,max_length=50, blank=True, null=True, verbose_name='Retailer Group')
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(RegionMaster,on_delete = models.SET_NULL, null=True)
    city = models.ForeignKey(CityMaster, on_delete=models.CASCADE, null=True, blank=True)
    Pincode = models.CharField(max_length=10, null=True, blank=True)
    Contact_person_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Contact Person Name')
    gstin = GSTField(verbose_name='GSTIN')
    ZIN_NO = models.CharField(max_length=50, null=True, blank=True, verbose_name="ZIN No")
    Customer_Name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Retailer Name")
    state = models.ForeignKey(StateMaster, on_delete=models.CASCADE, null=True, blank=True)
    Address = models.TextField(max_length=150, null=True, blank=True)
    Contact_Number = PhoneField(verbose_name="Contact Number")
    Email_ID = models.EmailField(null=True, blank=True, verbose_name="Email ID")
    pan = PANField(verbose_name="PAN NO")
    Customer_For_Code = models.CharField(choices=CUSTOMER_CODE_CHOICE, max_length=10, verbose_name="Retailer For Code")
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Customer"

    def __unicode__(self):
        return self.Customer_Name

    def __str__(self):
        return str(self.Customer_Code)


class Item(models.Model):
    unit_of_measurement = (
        ('Meter(m)', 'Meter(m)'),
        ('Kilogram(kg)', 'Kilogram(kg)'),
        ('Piece(pc)', 'Piece(pc)'),
    )
    batch_enable = (
        ('Yes','Yes'),
        ('No', 'No'),
    )
    # distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)
    Item_Name = models.CharField(max_length=100)
    Item_Code = models.CharField(max_length=30, unique=True)
    Batch_Enabled = models.CharField(choices=batch_enable,max_length=20, null=True, blank=True)
    base_uom = models.ForeignKey(UOM, on_delete=models.CASCADE)
    sale_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, related_name="sale_unit_m")
    purchase_uom = models.ForeignKey(UOM, on_delete=models.CASCADE,related_name="sale_unit_p")
    Principal_Company = models.CharField(max_length=100, null=True, blank=True)
    MRP = models.DecimalField(max_digits=20,decimal_places=2,default=0, verbose_name="Base Price")
    purchase_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Purchase Price",default=0)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Sale Price", default=0)
    HSN_Code = models.CharField(max_length=5, null=True, blank=True)
    TaxRate = models.ForeignKey(TaxMaster, on_delete=models.CASCADE,null=True, blank=True, verbose_name="Tax Rate")  
    GST_Applicable_From = models.DateField(null=True, blank=True)
    Hierarchy1 = models.ForeignKey(Hierarchy1, on_delete=models.CASCADE)
    Hierarchy2 = models.ForeignKey(Hierarchy2, on_delete=models.CASCADE)
    Hierarchy3 = models.ForeignKey(Hierarchy3, on_delete=models.CASCADE)
    Hier4 = models.ForeignKey(Hierarchy4, on_delete=models.CASCADE,null=True, blank=True, verbose_name="Hierarchy4")
    Hier5 = models.ForeignKey(Hierarchy5, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Hierarchy5")
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Item_Code


class DBPriceMaster(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, verbose_name='Distributor Code')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Item Code')
    Rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=True)
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item.Item_Code)

    def __int__(self):
        return self.Rate


class Warehouse(models.Model):
    wcode = models.CharField(max_length=50, verbose_name="Warehouse Code")
    wname = models.CharField(max_length=50, verbose_name="Warehouse Name")
    isactive=models.BooleanField(default=True , verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, editable=False) 
    
    
    def __str__(self):
        return self.wcode
    
    

class Sales(models.Model):
    Customers = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Customer Code')
    Customer_Name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Customer Name")
    sales_order_no = models.CharField(max_length=50, verbose_name="Sales Order No", unique=True)
    Bill_Date = models.DateField(verbose_name='Sales Order Date')
    cust_po_no = models.CharField(max_length=50, verbose_name="Customer PO No")
    cust_po_date = models.DateField(verbose_name="Customer PO Date")
    Invoice_No = models.CharField(max_length=50, verbose_name="Invoice No")
    Tally_MasterID = models.CharField(max_length=15, null=True, blank=True)
    Total_Inventory_Amount = models.DecimalField(max_digits=20, default=0, decimal_places=2, null=True, blank=True)
    gst_type = models.ForeignKey(TaxMaster, on_delete=models.CASCADE, verbose_name="GST Type", null=True)
    Total_GST = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True, blank=True)
    SGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True, blank=True)
    CGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True, blank=True)
    IGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True, blank=True)
    Cash_Discount_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True, blank=True)
    Total_Invoice_Amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sales_order_no
    
    def created_date(self):
        return self.created_on.strftime("%b %d %Y, %I:%M %p")


    # def save(self, *args, **kwargs):
    #     self.Customer_Name = self.Customers.Customer_Name
    #     self.Total_Invoice_Amount = self.CGST_AMOUNT + self.SGST_AMOUNT
    #     super(Sales, self).save(*args, **kwargs)

    def createdAt(self):
        return self.created_on.strftime('%Y' '%B' '%d')


class Sales_Detail(models.Model):
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE, null=True, blank=True)
    entity_id = models.PositiveIntegerField(default=0,verbose_name = "TID")
    Sales_Item_Code = models.ForeignKey(Item, on_delete=models.CASCADE)
    Sales_Item_Name = models.CharField(max_length=50, null=True, blank=True)
    Sales_Quantity = models.IntegerField(default=0)
    bal_qty = models.IntegerField(default=0, verbose_name="BAL QTY", null=True, blank=True)
    sale_uom = models.CharField(max_length=50,null=True, verbose_name="Sales UOM")
    Sales_Rate = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    Sales_Serial_No = models.CharField(max_length=50, null=True, blank=True)
    Sales_Batch = models.CharField(max_length=50, null=True, blank=True)
    Sales_Discount = models.PositiveIntegerField(null=True, verbose_name="Sales Discount(%)", default=0)
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sales Detail"

    def __str__(self):
        res = self.Sales_Quantity
        return str(res)


class Delivery_Note(models.Model):
    Customers = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Customer Code')
    Customer_Name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Customer Name')
    Bill_Date = models.DateField(verbose_name='Bill Date', null=True, blank=True)
    Invoice_No = models.CharField(max_length=100, verbose_name='Sales Invoice No', null=True, blank=True)
    delivery_note_no = models.CharField(max_length=50, verbose_name="Delivery Note No", unique=True)
    delivery_note_date = models.DateField(verbose_name="Delivery Note Date")
    cust_po_no = models.CharField(max_length=50, verbose_name="Customer PO No")
    cust_po_date = models.DateField(verbose_name="Customer PO Date")
    sales_order_no = models.ForeignKey(Sales, on_delete=models.CASCADE, verbose_name="Sales Order No")
    warehouse=models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name="Warehouse")
    sales_order_date = models.DateField(verbose_name="Sales Order Date")
    gst_type = models.ForeignKey(TaxMaster, on_delete=models.CASCADE, verbose_name="GST Type", null=True)
    Total_Inventory_Amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Total Inventory Amount',default=0)
    Total_GST = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='Total GST', null=True,blank=True)
    SGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='SGST AMOUNT', null=True,blank=True)
    CGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='CGST AMOUNT', null=True,blank=True)
    IGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='IGST AMOUNT', null=True,blank=True)
    Cash_Discount_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0,verbose_name='Cash Discount Amount', null=True, blank=True)
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name="Total Invoice Amount")
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Delivery Note"

    def __str__(self):
        return self.delivery_note_no


class Delivery_Note_Details(models.Model):
    entity_id = models.IntegerField(verbose_name = "TID")
    note = models.ForeignKey(Delivery_Note, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Sales Item Code')
    Item_Name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Item Name')
    Quantity = models.PositiveIntegerField(verbose_name='Sales Quantity',default=0)
    bal_qty = models.IntegerField(default=0,verbose_name="BAL QTY", null=True, blank=True)
    DN_QTY = models.IntegerField(default=0)
    uom = models.CharField(max_length=50,null=True, verbose_name="UOM")
    Rate = models.FloatField(verbose_name='Sales Rate')
    Serial_No = models.CharField(max_length=50, verbose_name='Sales Serial No',null=True, blank=True)
    Discount = models.FloatField(null=True, blank=True, default=0, verbose_name='Sales Discount')
    Amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Total Amount')
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Delivery Note Detail"

    def __str__(self):
        return self.Item_Name






class salesInvoice(models.Model):
    Customers = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Customer Code')
    Customer_Name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Customer Name")
    Bill_Date = models.DateField(verbose_name="Sales Invoice Date")
    Invoice_No = models.CharField(max_length=50, verbose_name="Sales Invoice No", unique=True)
    sale_order = models.ForeignKey(Sales, verbose_name="Sales Order No", on_delete=models.CASCADE)
    sale_order_date = models.DateField(verbose_name="Sales Order Date")
    dl_note_no = models.ForeignKey(Delivery_Note, on_delete=models.CASCADE, verbose_name="Delivery Note No")
    dl_note_date = models.DateField(verbose_name="Delivery Note Date")
    Total_Inventory_Amount = models.DecimalField(max_digits=20, default=0, decimal_places=2, null=True, blank=True, verbose_name="Total Inventory Amount")
    gst_type = models.ForeignKey(TaxMaster, on_delete=models.CASCADE, verbose_name="GST Type", null=True)
    Total_GST = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True, blank=True, verbose_name="Total GST Amount")
    SGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True, blank=True, verbose_name="SGST Amount")
    CGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True, blank=True, verbose_name="CGST Amount")
    IGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True, blank=True, verbose_name='IGST Amount')
    Cash_Discount_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True, blank=True, verbose_name="Total Discount Amount")
    Total_Invoice_Amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, verbose_name="Total Invoice Amount")
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Invoice_No
    
        
    
class saleinvoicelineItem(models.Model):
    inv = models.ForeignKey(salesInvoice, on_delete=models.CASCADE, null=True, blank=True)
    parent_id = models.PositiveIntegerField(default=0,verbose_name = "TID")
    Item_Code = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Item Code")
    Item_Name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Item Name")
    Quantity = models.PositiveIntegerField(default=0)
    bal_qty = models.IntegerField(default=0,verbose_name="BAL QTY", null=True, blank=True)
    SI_QTY = models.IntegerField(default=0)
    uom = models.CharField(max_length=50,null=True, verbose_name="UOM")
    Rate = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    Serial_No = models.CharField(max_length=50, null=True, blank=True)
    Discount = models.PositiveIntegerField(null=True, verbose_name="Discount(%)", default=0)
    Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sales Invoice LineItem"

    def __str__(self):
        res = self.Quantity
        return str(res)

    def save(self, *args, **kwargs):
        
        # self.entity_id = Sales.objects.last().id
        self.Item_Name = self.Item_Code.Item_Name
        self.Dis = (self.Rate * self.Quantity)
        self.amount = self.Dis * self.Discount / 100
        self.Total_Amount = self.Rate * self.Quantity - self.amount
        super(saleinvoicelineItem, self).save(*args, **kwargs)



class SalesReturn(models.Model):
    Customers = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer Code")
    Customer_Name = models.CharField(max_length=50, null=True, blank=True)
    sale_invoice_no = models.ForeignKey(salesInvoice, on_delete=models.CASCADE, verbose_name="Sales Invoice No", null=True)
    warehouse=models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name="Warehouse")
    Bill_Date = models.DateField(verbose_name="Sales Invoice Date")
    sales_return_no = models.CharField(max_length=50,verbose_name="Sales Return No", unique=True)
    sales_return_date = models.DateField(verbose_name="Sales Return Date")
    Tally_Master_ID = models.CharField(max_length=15, null=True, blank=True)
    Total_Inventory_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    gst_type = models.ForeignKey(TaxMaster, on_delete=models.CASCADE, verbose_name="GST Type", null=True)
    Total_GST = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    SGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    CGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, blank=True)
    IGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    Cash_Discount_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    Total_Invoice_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name="Total Invoice Amount")
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.sales_return_no
        
    class Meta:
        verbose_name = "Sales Return"

    @property
    def total_price(self):
        cost = 0
        for item in self.items.all():
            cost += item.total_price
        return str(cost)


class Sales_Return_Detail(models.Model):
    salereturn = models.ForeignKey(SalesReturn, on_delete=models.CASCADE, null=True, blank=True)
    entity_id = models.IntegerField(null=True,verbose_name = "TID")
    Sales_Item_Code = models.ForeignKey(Item, on_delete=models.CASCADE)
    Sales_Item_Name = models.CharField(max_length=50, null=True, blank=True)
    Sales_Quantity = models.PositiveIntegerField(default=0)
    sale_uom = models.CharField(max_length=50,null=True, verbose_name="Sales UOM")
    Sales_Rate = models.DecimalField(max_digits=20, decimal_places=2)
    Sales_Serial_No = models.CharField(max_length=50, null=True, blank=True)
    Sales_Discount = models.PositiveIntegerField(null=True, verbose_name="Sales Discount(%)", default=0)
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        res = self.Sales_Quantity
        return str(res)



class PurchaseDocument(models.Model):
    Distributors = models.ForeignKey(Distributor, on_delete=models.CASCADE, verbose_name='Distributor Code')
    Distributor_Name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Distributor Name')
    Bill_Date = models.DateField(verbose_name='Purchase Order Date')
    SAP_Order_No = models.CharField(max_length=50, null=True, blank=True, verbose_name='Purchase Order No', unique=True)
    gst_type = models.ForeignKey(TaxMaster, on_delete=models.CASCADE, verbose_name="GST Type", null=True)
    Total_Inventory_Amount = models.FloatField(null=True, verbose_name='Total Inventory Amount', default=0)
    Total_GST = models.FloatField(null=True, verbose_name='Total GST Amount', default=0)
    SGST_AMOUNT = models.FloatField(null=True, blank=True, verbose_name='SGST AMOUNT', default=0)
    CGST_AMOUNT = models.FloatField(null=True, blank=True, verbose_name='CGST AMOUNT', default=0)
    IGST_AMOUNT = models.FloatField(null=True, blank=True, verbose_name='IGST AMOUNT', default=0)
    Vendor_Name = models.CharField(max_length=100, choices=vendor_choice, verbose_name='Billing Entity')
    PO_No = models.CharField(max_length=50, null=True, blank=True, verbose_name='PO No')
    Total_Invoice_Amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Total Invoice Amount')
    total_discount_amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Total Discount Amount')
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Purchase Document"

    def __str__(self):
        return self.SAP_Order_No 
    
    def get_orderno(self):
        return self.SAP_Order_No

class DetailOfPurchase(models.Model):
    purchase = models.ForeignKey(PurchaseDocument, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Item Code')
    entity_id = models.IntegerField(verbose_name = "TID")
    item_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Item Name')
    Purchases_Quantity = models.IntegerField(verbose_name='Purchase Quantity',default=0)
    bal_qty = models.IntegerField(default=0, verbose_name="BAL QTY", null=True, blank=True)
    purchase_uom = models.CharField(max_length=50,null=True, verbose_name="Purchase UOM")
    Purchase_Rate = models.FloatField(verbose_name='Purchase Rate')
    Purchase_Product_Discount = models.FloatField(null=True, blank=True, default=0,verbose_name='Purchase Discount(%)')
    Purchases_Serial_No = models.CharField(max_length=50, verbose_name='Puchase Serial No', null=True, blank=True)
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Total Amount')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Purchase Document Detail"

    # def __str__(self):
    #     return str(self.item_name)

    # def save(self, *args, **kwargs):
    #     self.item_name = self.items.Item_Name
    #     self.amount = self.Purchase_Rate * self.Purchases_Quantity
    #     self.Product_Discount = self.amount * self.Purchase_Product_Discount / 100
    #     self.Total_Amount = self.amount - self.Product_Discount
    #     super(DetailOfPurchase, self).save(*args, **kwargs)


class Receipt_Note(models.Model):
    Distributors = models.ForeignKey(Distributor, on_delete=models.CASCADE, verbose_name='Distributor Code')
    Distributor_Name = models.CharField(max_length=50,null=True, blank=True, verbose_name="Distributor Name")
    Customers = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Customer Code', null=True, blank=True)
    Invoice_No = models.CharField(max_length=100, verbose_name='Supplier Invoice No',null=True, blank=True)
    supplier_invoice_date = models.DateField(verbose_name='Supplier Invoice Date')
    recipt_no = models.CharField(max_length=50, verbose_name="MRN No", unique=True)
    receipt_note_date = models.DateField(verbose_name="MRN Date")
    p_order_no = models.ForeignKey(PurchaseDocument, on_delete=models.CASCADE, verbose_name="Purchase Order Number")
    Bill_Date = models.DateField(verbose_name='Purchase Order Date')
    gst_type = models.ForeignKey(TaxMaster, on_delete=models.CASCADE, verbose_name="GST Type", null=True)
    warehouse=models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name="Warehouse")
    Total_Inventory_Amount = models.CharField(max_length=100, verbose_name='Total Inventory Amount', default=0)
    Total_GST = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='Total Gst Amount')
    SGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='SGST AMOUNT', null=True,blank=True)
    CGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='CGST AMOUNT', null=True,blank=True)
    IGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='IGST AMOUNT', null=True,blank=True)
    Cash_Discount_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0,verbose_name='Total Discount Amount', null=True, blank=True)
    R_O_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='R O AMOUNT', null=True,blank=True)
    billing_entity = models.CharField(max_length=100, choices=vendor_choice, verbose_name='Billing Entity')
    Total_Amount = models.CharField(max_length=20, verbose_name="Total Invoice Amount")
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Receipt Note"

    def __str__(self):
        return str(self.recipt_no)


class Receipt_Note_Detail(models.Model):
    receipt = models.ForeignKey(Receipt_Note, on_delete=models.CASCADE, null=True, blank=True)
    entity_id = models.IntegerField(verbose_name = "TID")
    items = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Item Code')
    Item_Name = models.CharField(max_length=50, null=True, blank=True)
    uom = models.CharField(max_length=50,null=True, verbose_name="UOM")
    bal_qty = models.IntegerField(default=0,verbose_name="BAL QTY", null=True, blank=True)
    MRN_QTY =models.IntegerField(default=0)
    Quantity = models.PositiveIntegerField(verbose_name='Quantity',default=0)
    Rate = models.FloatField(verbose_name='Rate')
    Serial_No = models.CharField(max_length=50, verbose_name='Serial No', null=True, blank=True)
    Discount = models.FloatField(null=True, blank=True, default=0, verbose_name='Discount')
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Total Amount')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Receipt Note Detail"

    def save(self, *args, **kwargs):
        self.Item_Name = self.items.Item_Name
        self.amount = (self.Rate * self.Quantity)
        self.discount = self.amount * self.Discount / 100
        self.Total_Amount = self.amount - self.discount
        super(Receipt_Note_Detail, self).save(*args, **kwargs)





    
class PurchaseInvoice(models.Model):
    vendor_choice = (
        ('Johnson and Johnson Surgical Vision India Pvt. Ltd.', 'Johnson and Johnson Surgical Vision India Pvt. Ltd.'),
        ('Johnson and Johnson .', 'Johnson and Johnson '),
    )
    Distributors = models.ForeignKey(Distributor, on_delete=models.CASCADE, verbose_name='Distributor Code')
    Distributor_Name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Distributor Name')
    Bill_Date = models.DateField(verbose_name='Purchase Order Date')
    purchase_invoice_no = models.CharField(max_length=50, verbose_name="Purchase Invoice No", unique=True)
    purchase_invoice_date = models.DateField(verbose_name="Purchase Invoice Date")
    Supplier_Invoice_No = models.CharField(max_length=50, verbose_name='Supplier Invoice No')
    purchase_invoice = models.ForeignKey(PurchaseDocument, verbose_name=_("Purchase Order No"), on_delete=models.CASCADE)
    SAP_Order_Date = models.DateField(verbose_name='Supplier Invoice Date')
    mrn_no = models.ForeignKey(Receipt_Note, on_delete=models.CASCADE, verbose_name="MRN No")
    mrn_date = models.DateField(verbose_name="MRN Date")
    gst_type = models.ForeignKey(TaxMaster, on_delete=models.CASCADE, verbose_name="GST Type", null=True)
    Total_Inventory_Amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Total Inventory Amount', default=0)
    Total_GST = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Total GST Amount', default=0)
    SGST_AMOUNT = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='SGST AMOUNT', default=0)
    CGST_AMOUNT = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='CGST AMOUNT', default=0)
    IGST_AMOUNT = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='IGST AMOUNT', default=0)
    Vendor_Name = models.CharField(max_length=100, choices=vendor_choice, verbose_name='Billing Entity')
    PO_No = models.CharField(max_length=50, null=True, blank=True, verbose_name='PO No')
    total_discount_amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Total Discount Amount')
    Total_Invoice_Amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Total Invoice Amount')
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Purchase Invoice"
        
    class Meta:
        get_latest_by = 'purchase_invoice_no'    

    def __str__(self):
        return str(self.purchase_invoice_no) 
    

    

class PurchaseinvoicelineItem(models.Model):
    pinvoice = models.ForeignKey(PurchaseInvoice, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Item Code')
    parent_id = models.CharField(max_length=30,verbose_name = "TID")
    item_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Item Name')
    Quantity = models.PositiveIntegerField(verbose_name='Quantity',default=0)
    bal_qty = models.IntegerField(default=0,verbose_name="BAL QTY", null=True, blank=True)
    PI_QTY = models.IntegerField(default=0)
    UOM = models.CharField(max_length=50,null=True, verbose_name="UOM")
    Rate = models.FloatField(verbose_name='Rate')
    Discount = models.FloatField(null=True, blank=True, default=0, verbose_name='Discount(%)')
    Serial_No = models.CharField(max_length=50, verbose_name='Serial No', null=True, blank=True)
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Total Amount')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.item_name  

class PurchaseReturnDocument(models.Model):
    vendor_choice = (
        ('Johnson and Johnson Surgical Vision India Pvt. Ltd.', 'Johnson and Johnson Surgical Vision India Pvt. Ltd.'),
        ('Johnson and Johnson .', 'Johnson and Johnson '),
    )
    Distributors = models.ForeignKey(Distributor, on_delete=models.CASCADE, verbose_name='Distributor Code')
    distributor_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Distributor Name")
    Bill_Date = models.DateField(verbose_name='PR Date')
    pi_no = models.ForeignKey(PurchaseInvoice, on_delete=models.CASCADE, verbose_name="PI No")
    warehouse=models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name="Warehouse")
    pi_date = models.DateField(verbose_name="PI Date")
    Supplier_Invoice_No = models.CharField(max_length=50, verbose_name='Supplier Invoice No')
    SAP_Order_No = models.CharField(max_length=50, null=True, blank=True, verbose_name='PR No', unique=True)
    SAP_Order_Date = models.DateField(verbose_name='Supplier Invoice Date')
    gst_type = models.ForeignKey(TaxMaster, on_delete=models.CASCADE, verbose_name="GST Type", null=True)
    Total_GST = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Total GST Amount', default=0)
    Total_GST = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Total GST', default=0)
    SGST_AMOUNT = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='SGST AMOUNT', default=0)
    CGST_AMOUNT = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='CGST AMOUNT', default=0)
    IGST_AMOUNT = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='IGST AMOUNT', default=0,blank=True)
    Vendor_Name = models.CharField(max_length=100, choices=vendor_choice, verbose_name='Billing Entity')
    total_discount_amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Total Discount Amount')
    Total_Inventory_Amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Total Inventory Amount',default=0)
    Total_Invoice_Amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Total Invoice Amount')
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Updated on")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created on")  
    class Meta:
        verbose_name = "Purchase Return Document"

    def __str__(self):
        return self.SAP_Order_No
    


class DetailsOfPurchaseReturn(models.Model):
    preturn = models.ForeignKey(PurchaseReturnDocument, on_delete=models.CASCADE, null=True, blank=True)
    entity_id = models.IntegerField(verbose_name = "TID")
    items = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Item Code')
    Item_Name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Purchase Return Item Name")
    Purchases_Return_Quantity = models.PositiveIntegerField(verbose_name='Purchase Return Quantity',default=0)
    purchase_uom = models.CharField(max_length=50,null=True, verbose_name="Purchase UOM")
    Purchase_Rate = models.FloatField(verbose_name='Purchase Rate')
    Purchase_Product_Discount = models.FloatField(null=True, blank=True, default=0,
                                                  verbose_name='Purchase Product Discount(%)')
    Purchases_Serial_No = models.CharField(max_length=50, verbose_name='Puchase Serial No')
    Reference_No = models.CharField(max_length=50, null=True, blank=True)
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Total Amount')
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Updated on")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created on")  


    class Meta:
        verbose_name = "Purchase Return Detail"

    def __str__(self):
        res = self.items
        return str(res)

    def save(self, *args, **kwargs):
        self.Item_Name = self.items.Item_Name
        self.amount = (self.Purchase_Rate * self.Purchases_Return_Quantity)
        self.discount = self.amount * self.Purchase_Product_Discount / 100
        self.Total_Amount = self.amount - self.discount
        super(DetailsOfPurchaseReturn, self).save(*args, **kwargs)



class FieldMaster(models.Model):
    DocType = models.CharField(max_length=50)
    Field_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Field_Name


# auditlog.register(RoleMaster)
# auditlog.register(User)
# auditlog.register(Distributor)
# auditlog.register(Customer)


class ExcelFileUploaded(models.Model):
    excel_file_upload = models.FileField(upload_to="excel")


class Entity(models.Model):
    CHOICES = (
        (1, 'ANY CHARACTER'),
        (2, 'ALPHA NUMERIC'),
        (3, 'ALPHA NUMERIC WITH CAPS LETTER'),
        (4, 'ALPHA NUMERIC WITH SPECIAL CHARACTER'),
    )
    other_choices = (
        (1, 'User ID'),
        (2, 'Distributor Name'),
        (3, 'Distributor Code'),
    )
    # user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    EID = models.AutoField(primary_key=True)
    Code = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    isAuth = models.BooleanField(null=True, blank=True)
    Account_Type = models.CharField(max_length=20, null=True, blank=True)
    MinChar = models.PositiveIntegerField(null=True, blank=True, verbose_name='*Minimum Character [?]:')
    MaxChar = models.PositiveIntegerField(null=True, blank=True, verbose_name="*Maximum Character [?]:")
    PassType = models.CharField(choices=CHOICES, max_length=50, null=True, blank=True,
                                verbose_name="*Password Type [?]:")
    Passexpdays = models.PositiveIntegerField(null=True, blank=True, verbose_name="*Password Expiry Days [?]:")
    PassexpMsgDays = models.PositiveIntegerField(null=True, blank=True,
                                                 verbose_name="Password Expiry Message Days [?]:")
    Autounlockhour = models.PositiveIntegerField(null=True, blank=True, verbose_name="*Auto Unlock Hours [?]:")
    minPassAttempt = models.PositiveIntegerField(null=True, blank=True, verbose_name="*Min Password Attempt [?]:")
    LoginField = models.CharField(max_length=50, null=True, blank=True)
    Email_ID = models.BooleanField(null=True, blank=True, verbose_name="Email ID")
    others = models.CharField(max_length=50, choices=other_choices, null=True, blank=True)
    UserID = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.MinChar)


class StockMaster(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)

    sales = models.ForeignKey(Sales_Detail, on_delete=models.CASCADE)
    salesreturn = models.ForeignKey(Sales_Return_Detail, on_delete=models.CASCADE)
    purchases = models.ForeignKey(PurchaseDocument, on_delete=models.CASCADE)
    purchasereturn = models.ForeignKey(PurchaseReturnDocument, on_delete=models.CASCADE)
    #openingbalance = models.ForeignKey(Opening_Balance, on_delete=models.CASCADE)
    #openingbalancechild = models.ForeignKey(Opening_Balance_Child, on_delete=models.CASCADE)
    closingbalance = models.PositiveIntegerField()

    def __str__(self):
        return str(self.closingbalance)

    def save(self, *args, **kwargs):
        super(StockMaster, self).save(*args, **kwargs)


class ClosingBalance(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    sales = models.ForeignKey(Sales_Detail, on_delete=models.CASCADE)
    salesreturn = models.ForeignKey(Sales_Return_Detail, on_delete=models.CASCADE)
    purchases = models.ForeignKey(PurchaseDocument, on_delete=models.CASCADE)
    purchasereturn = models.ForeignKey(PurchaseReturnDocument, on_delete=models.CASCADE)
    purchasedetail = models.ForeignKey(DetailOfPurchase, on_delete=models.CASCADE)
    purchasereturndetail = models.ForeignKey(DetailsOfPurchaseReturn, on_delete=models.CASCADE)
    #openingbalance = models.ForeignKey(Opening_Balance, on_delete=models.CASCADE)
    #openingbalancechild = models.ForeignKey(Opening_Balance_Child, on_delete=models.CASCADE)
    closingbalance = models.PositiveIntegerField()

    def __str__(self):
        return str(self.closingbalance)

    def save(self, *args, **kwargs):
        self.closingbalance = self.openingbalancechild + self.purchasedetail - self.sales
        super(ClosingBalance, self).save(*args, **kwargs)


class Stock(models.Model):
    Distributor_Code = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    items = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    Distributor_Name = models.CharField(max_length=50, null=True, blank=True)
    Date = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Opening Balance"

    def __str__(self):
        return str(self.Distributor_Code)

class Stock_Child(models.Model):
    entity_id = models.IntegerField(null=True,verbose_name = "TID")
    Item_Code = models.ForeignKey(Item, on_delete=models.CASCADE)
    Item_Name = models.CharField(max_length=50, null=True, blank=True)
    Quantity = models.PositiveIntegerField(default=0)
    base_uom = models.CharField(max_length=50, null=True, verbose_name="Base UOM")
    Rate = models.DecimalField(max_digits=20, decimal_places=2)
    #Serial_No = models.CharField(max_length=50, null=True, blank=True)
    sr = models.CharField(max_length=50, null=True, blank=True,verbose_name="Serial_No")
    Batch = models.CharField(max_length=50, null=True, blank=True)
    Discount = models.PositiveIntegerField(null=True, verbose_name="Sales Discount(%)")
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    Reference_No = models.CharField(max_length=50, null=True, blank=True)
    #Stock = models.ForeignKey(Opening_Balance, on_delete=models.CASCADE, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    def save(self, *args, **kwargs):
        self.Item_Name = self.Item_Code.Item_Name
        super(Stock_Child, self).save(*args, **kwargs)
    
    
    
    

    

class warehouseStock(models.Model):
    warehouseCode = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name='Warehouse Code')
    warehouseName = models.CharField(max_length=50, null=True, blank=True, verbose_name="Warehouse Name")
    w_order_no = models.CharField(max_length=50, null=True, blank=True, verbose_name="Stock ID")
    itemName = models.CharField(max_length=80, null=True, blank=True, verbose_name="ItemName")
    Date = models.DateField(verbose_name="Date")
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "warehouse wise item stock"

    def __str__(self):
        return str(self.warehouseName)   
    

     
     
class warehouseItemChild(models.Model):
    w = models.ForeignKey(warehouseStock, on_delete=models.CASCADE, null=True, blank=True)
    warehouseID = models.IntegerField(null=True, verbose_name="Warehouse Id")
    w_house = models.IntegerField(verbose_name="Warehouse", null=True)
    Item_Code = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Item_Code")
    Item_Name = models.CharField(max_length=50, null=True, blank=True)
    Quantity = models.PositiveIntegerField(default=0)
    base_uom = models.CharField(max_length=50, null=True, verbose_name="Base UOM")
    Rate = models.DecimalField(max_digits=20, decimal_places=2,default=0)
    Batch = models.CharField(max_length=50, null=True, blank=True)
    Discount = models.PositiveIntegerField(null=True, default=0, verbose_name="Sales Discount(%)")
    SNo = models.CharField(max_length=50, null=True, blank=True, verbose_name="Serial No")
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    Reference_No = models.CharField(max_length=50, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateField(auto_now_add=True) 
    
    def __str__(self):
        return self.Item_Name  
    
    

import datetime

def current_year():
    return datetime.date.today().year

def current_month():
    return datetime.date.today().month


class OrderGenerator(models.Model):
    documentType =  models.CharField(max_length=30,choices=doc_choice, verbose_name="Document Type", unique=True)
    seprator_choice = models.CharField(max_length=30,choices=seperator_option, verbose_name='Separtor', null=True, blank=True) 
    prfx = models.CharField(max_length=20, null=True, blank=True, verbose_name="Prefix")  
    Field_selection = models.CharField(max_length=30, choices=TYPE_SELECT, verbose_name="Field Selection")
    num_sequence = models.IntegerField(null=True, blank=True,verbose_name="Number Sequence")
    seqnum = models.CharField(max_length=30,null=True, blank=True,verbose_name=" Start Number Sequence")
    auto_no = models.IntegerField(verbose_name='Auto Number', null=True, blank=True)
    Document_for_prefix = models.CharField(max_length=30, choices=doc_choice, verbose_name='Document for prefix', null=True, blank=True)
    New_auto_no = models.IntegerField(verbose_name="New Auto Number", null=True, blank=True)
    Doc_field = models.CharField(max_length=50, null=True, blank=True, verbose_name="Document Field")
    sufx = models.CharField(max_length=20, null=True, blank=True, verbose_name="Suffix")
    use_FY_as_prfx = models.BooleanField(verbose_name="Use FY as Prefix", default=False)
    use_FY_as_sufx = models.BooleanField(verbose_name="Use FY as Suffix", default=False)
    FY = models.IntegerField(_('year'),default=current_year)
    Fmonth = models.IntegerField(_('month'),default=current_month)
    order_combination = models.CharField(max_length=70 ,verbose_name="Order Combination", null=True, blank=True)
    use_month_as_prfx = models.BooleanField(verbose_name="Use Month as Prefix",default=False)
    use_month_as_sufx = models.BooleanField(verbose_name="Use Month as suffix",default=False)
    isactive=models.BooleanField(default=1 , verbose_name="Is Active")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)  
    
    def __str__(self):
        return self.order_combination




class stockSummary(models.Model):
    warehouse = models.IntegerField(default=0,verbose_name="Warehouse")
    w_code = models.CharField(max_length=100, null=True, blank=True, verbose_name="Warehouse Code")
    item = models.IntegerField(default=0,verbose_name="Item")
    itm_code = models.CharField(max_length=100, null=True, blank=True, verbose_name="Item Code")
    OP = models.IntegerField(default=0, verbose_name="Opening Balance")
    Mrn_Qty = models.IntegerField(default=0, verbose_name="Purchase Qty" , null=True, blank=True)
    purchase_return_qty = models.IntegerField(default=0, verbose_name="Purchase Return Qty", null=True, blank=True)
    delivery_note_qty = models.IntegerField(default=0, verbose_name="Sale Qty", null=True, blank=True)
    uom = models.CharField(max_length=100, null=True, blank=True)
    sale_return_qty = models.IntegerField(default=0, verbose_name="Sale Return Qty", null=True, blank=True)
    closing_balance = models.CharField(max_length=100, verbose_name="Closing Balance", null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    

    
    
