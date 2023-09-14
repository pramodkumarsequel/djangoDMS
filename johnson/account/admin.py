from django.contrib import admin
from .models import (RoleMaster, User, Customer, Zone, Distributor, Hierarchy1, Hierarchy2,
                     Hierarchy3, Hierarchy4, Hierarchy5, Item, DBPriceMaster, Sales, Sales_Detail,
                    DetailOfPurchase, PurchaseDocument, DetailsOfPurchaseReturn,
                     PurchaseReturnDocument,
                     Delivery_Note, Delivery_Note_Details, Receipt_Note, Receipt_Note_Detail, SalesReturn, FieldMaster,
                     Entity, Profile, Sales_Return_Detail, RegionMaster,
                     StateMaster, CityMaster, StockMaster, Stock, Stock_Child, TaxMaster, Unit, UOM, warehouseStock, warehouseItemChild
                     )
from import_export.admin import ImportExportModelAdmin


@admin.register(StockMaster)
class StockAdminMaster(admin.ModelAdmin):
    list_display = ('id',
        'items', 'sales', 'salesreturn', 'purchases', 'purchasereturn','closingbalance',)


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('id','user', 'forgot_password_token',)


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    # list_display = ('EID','user','Code','Name','isAuth','Account_Type','MinChar','MaxChar','PassType',
    #                 'Passexpdays','PassexpMsgDays','Autounlockhour','minPassAttempt','minPassAttempt',
    #                 )
    list_display = ('EID',
                    'MinChar', 'MaxChar', 'PassType', 'Passexpdays', 'PassexpMsgDays', 'Autounlockhour',
                    'minPassAttempt',
                    'others',)


@admin.register(Distributor)
class DistributorAdmin(ImportExportModelAdmin):
    list_display = ("id", "Distributor_Name","Distributor_Code", "Email_ID",)
    list_filter = ("Distributor_Name",)
    search_fields = ['id', ]


# Register your models here.

@admin.register(RoleMaster)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'roletype', 'description',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'userid', 'role', 'email',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id',
        'Customer_Code', 'Customer_Name', 'Customer_Group', 'city', 'Pincode', 'Contact_person_name', 'updated_on',)


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id','name',)


@admin.register(Hierarchy1)
class Hierarchy1Admin(admin.ModelAdmin):
    list_display = ('id','Name',)


@admin.register(Hierarchy2)
class Hierarchy2Admin(admin.ModelAdmin):
    list_display = ('id','Name',)


@admin.register(Hierarchy3)
class Hierarchy3Admin(admin.ModelAdmin):
    list_display = ('id','Name',)


@admin.register(Hierarchy4)
class Hierarchy4Admin(admin.ModelAdmin):
    list_display = ('id','Name',)


@admin.register(Hierarchy5)
class Hierarchy5Admin(admin.ModelAdmin):
    list_display = ('id','Name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','Item_Name', 'Item_Code', 'Batch_Enabled', 'Principal_Company', 'MRP', 'HSN_Code',
                    'TaxRate', 'GST_Applicable_From']


from .models import Sales


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'Bill_Date', 'Customer_Name', 'Invoice_No', 'Tally_MasterID',
        'Total_Inventory_Amount',
        'Total_GST', 'SGST_AMOUNT',
        'Total_Invoice_Amount', 'updated_on', 'created_on',)


@admin.register(Sales_Detail)
class Child_DetailsAdmin(admin.ModelAdmin):
    list_display = ('id','entity_id', 'Sales_Item_Name',
                    'Sales_Item_Code', 'Sales_Quantity', 'Sales_Rate', 'Sales_Serial_No',
                    'Sales_Discount',
                    'Total_Amount',)



@admin.register(PurchaseDocument)
class PurchaseDocumentAdmin(admin.ModelAdmin):
    list_display = ['id','Distributors', 'Bill_Date','SAP_Order_No']
    

@admin.register(DetailOfPurchase)
class DetailPurchaseAdmin(admin.ModelAdmin):
    list_display = ('id',"entity_id",
                    'items', 'item_name', 'Purchases_Quantity', 'Purchase_Rate', 'Purchase_Product_Discount',
                    'Purchases_Serial_No',
                    'Total_Amount',)    



@admin.register(PurchaseReturnDocument)
class PurchaseReturnDocumentAdmin(admin.ModelAdmin):
    list_display = ['id','Bill_Date', 'Supplier_Invoice_No']
    

@admin.register(DetailsOfPurchaseReturn)
class DetailOfPurchaseAdmin(admin.ModelAdmin):
    list_display = ('id','entity_id',
        'items', 'Item_Name', 'Purchases_Return_Quantity', 'Purchase_Rate', 'Purchase_Product_Discount',
        'Purchases_Serial_No',
        'Total_Amount',)    


@admin.register(Delivery_Note)
class DeliveryNoteAdmin(admin.ModelAdmin):
    list_display = ('id','Customers', 'Bill_Date', 'Invoice_No', 'Total_Inventory_Amount', 'Total_GST', 'SGST_AMOUNT',
        'CGST_AMOUNT', 'Total_Amount', 'created_on', 'updated_on',)



@admin.register(Delivery_Note_Details)
class DeliveryNoteDetailAdmin(admin.ModelAdmin):
    list_display = ['id','entity_id', 'items', 'Item_Name', 'Quantity', 'Rate', 'Serial_No', 'Discount',
                    'Amount',
                    'created_on', 'updated_on']


@admin.register(Receipt_Note)
class ReceiptNoteAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'Distributors', 'Customers', 'Bill_Date', 'Invoice_No', 'Total_Inventory_Amount', 'Total_GST',
                    'SGST_AMOUNT',
                    'CGST_AMOUNT', 'Total_Amount', 'created_on', 'updated_on',)
    list_filter = ['Distributors']


@admin.register(Receipt_Note_Detail)
class ReceiptNoteDetailAdmin(admin.ModelAdmin):
    list_display = ['id','entity_id', 'entity_id', 'items', 'Quantity', 'Rate', 'Serial_No', 'Discount',
                    'Total_Amount',
                    'created_on', 'updated_on']


@admin.register(SalesReturn)
class SalesReturnAdmin(admin.ModelAdmin):
    list_display = ['id','Bill_Date']


@admin.register(Sales_Return_Detail)
class AdminSaleReturnDetail(admin.ModelAdmin):
    list_display = ('id','entity_id','Sales_Item_Code', 'Sales_Item_Name', 'Sales_Quantity','sale_uom', 'Sales_Rate', 'Sales_Serial_No',
                     'Sales_Discount', 'Total_Amount', 'updated_on',)



@admin.register(FieldMaster)
class FieldMasterAdmin(admin.ModelAdmin):
    list_display = ['id','DocType', 'Field_Name']

@admin.register(RegionMaster)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id','Region_Name', 'zone',)


@admin.register(StateMaster)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id','zone', 'region', 'State_Name',)


@admin.register(CityMaster)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id','zone', 'region', 'State', 'City_Name',)



@admin.register(Stock)
class OpeningStockAdmin(admin.ModelAdmin):
    list_display = ('id','Distributor_Code','Date',)
    

@admin.register(Stock_Child)
class StockChildAdmin(admin.ModelAdmin):
    list_display = ('id','entity_id','Item_Code','Item_Name','Quantity','base_uom','Rate','Total_Amount')    
    
    
@admin.register(TaxMaster)
class TaxMasterAdmin(admin.ModelAdmin):
    list_display  = ('id','Tax_Type','name','value',)  
    
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display=('id','unit_class',) 

@admin.register(UOM)
class UOMAdmin(admin.ModelAdmin):
    list_display = ('id','unit_notation','unit_name','base_unit','conversion_factor','status',)             
    
@admin.register(warehouseStock)
class warehouseAdmin(admin.ModelAdmin):
    list_display = ('id','warehouseCode','warehouseName','itemName','Date',)


@admin.register(warehouseItemChild)
class warehouseAdmin(admin.ModelAdmin):
    list_display = ('warehouseID','Item_Name','Item_Name','Quantity','base_uom','Rate','SNo','Discount','Total_Amount',)
    
    
from account.models import stockSummary
@admin.register(stockSummary)
class stocksummaryAdmin(ImportExportModelAdmin):
    list_display = ('warehouse','item','Mrn_Qty','purchase_return_qty','delivery_note_qty','sale_return_qty','closing_balance')          