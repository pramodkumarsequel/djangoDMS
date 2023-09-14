# from dataclasses import field, fields
from cProfile import label
from distutils.command.upload import upload
from gettext import install
import re
from typing import Any
# from sre_parse import State
from django import forms
from django.forms.fields import Field
from django.db.models import Q
from matplotlib import widgets
from .models import UOM, RegionMaster, StateMaster, Unit, User, RoleMaster, CityMaster
from django.forms import formset_factory, modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, ButtonHolder, Field
from .models import (Customer, Zone, Distributor, DBPriceMaster, Item, Hierarchy1,
                     Hierarchy2, Hierarchy3, Hierarchy4, Hierarchy5, Sales,
                     Sales_Detail, PurchaseDocument, DetailOfPurchase, PurchaseReturnDocument,
                     DetailsOfPurchaseReturn, Delivery_Note, Delivery_Note_Details, Receipt_Note,
                     Receipt_Note_Detail, SalesReturn, Entity, Sales_Return_Detail, Stock, Stock_Child, TaxMaster,
                     RegionMaster,StateMaster,CityMaster,Warehouse,warehouseItemChild,warehouseStock,PurchaseInvoice,
                     PurchaseinvoicelineItem,salesInvoice,saleinvoicelineItem,OrderGenerator

                     )

from django.core.exceptions import ValidationError
from account.check import seperator_option, doc_choice, TYPE_SELECT

import datetime
def today_ymd():
    """Return today in format YYYY-MM-DD"""
    return datetime.date.today().strftime('%Y-%m-%d')

class MyForm(forms.Form):
    CHOICES = (('-------', 'SELECT'),
               ('Option 1', 'Form Submission Claim'), 
               ('Option 2', 'Document Report'),
               
               )
    DocumentType = forms.ChoiceField(label="Document Type", choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('DocumentType', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            )
        )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('userid', 'username', 'email', 'role','password','image','first_name','last_name','is_active','Phone')


class user_search_form(forms.Form):
    Field_Name = forms.ChoiceField()
    Value = forms.CharField(max_length=50, required=False)
    CHOICES = (
        ('User', '--------SELECT--------'),
        ('Username', 'Username'),
        ('EmailID', 'EmailID'),
    )
    Field_Name = forms.ChoiceField(label="Field Name", choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)
    Upload = forms.FileField(max_length=1000 ,required=False)


class RoleMasterForm(forms.ModelForm):
    class Meta:
        model = RoleMaster
        fields = ('id', 'name', 'description', 'roletype',)


class role_search_form(forms.Form):
    CHOICES = (
        ('RoleMaster', '-----SELECT-----'),
        ('Role', 'Role'),
        ('Description', 'Description'),
    )
    Field_Name = forms.ChoiceField(label="Field Name", choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)


class customer_search_form(forms.Form):
    CHOICES = (('Customer', '-----SELECT-----'), ('Retailer Code', 'Retailer Code'),
               ('Retailer Name', 'Retailer Name'),
               ('city', 'city'),
               ('state', 'state'),
               ('Address', 'Address'),
               ('EmailID', 'EmailID'),
               ('ZIN NO', 'ZIN NO'),
               ('Pincode', 'Pincode'),
               ('Contact person name', 'Contact person name'),
               ('gstin', 'gstin'),
               ('pan', 'pan'),
               )
    Field_name = forms.ChoiceField(label="Field Name", choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)

CHOICES = [ (supervisor.Distributor_Name, supervisor.get_name())
            for supervisor in Distributor.objects.all() ]

class CustomerForm(forms.ModelForm):  
    Distributor = forms.ModelChoiceField(queryset = Distributor.objects.all())
    class Meta:
        model = Customer
        fields = ('Customer_Code', 'Customer_Name', 'Customer_Group','zone','region','state', 'city', 'Address', 'Pincode',
                  'Contact_person_name', 'Email_ID', 'gstin', 'Contact_Number', 'pan','Distributor',)

        widgets = {
            'Address': forms.Textarea(attrs={'rows': 1, 'cols': 15}),
        } 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].queryset = RegionMaster.objects.none()
        self.fields['state'].queryset = StateMaster.objects.none()
        self.fields['city'].queryset = CityMaster.objects.none()
        
        if 'zone' in self.data:
            try:
                zone_id = int(self.data.get('zone'))
                self.fields['region'].queryset = RegionMaster.objects.filter(zone_id=zone_id).order_by('Region_Name')
        
            except (ValueError, TypeError):
                pass
        
        elif self.instance.pk:
            self.fields['region'].queryset = self.instance.region.regionmaster_set.order_by('Region_Name')
            
        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['state'].queryset = StateMaster.objects.filter(region_id=region_id).order_by('State_Name')
            
            except (ValueError, TypeError):
                pass
        
        elif self.instance.pk:
            self.fields['state'].queryset = self.instance.state.statemaster_set.order_by('State_Name')
            
        
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = CityMaster.objects.filter(State_id=state_id).order_by('City_Name')
            
            except (ValueError, TypeError):
                pass
        
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.city.citymaster_set.order_by('City_Name')          
                              

        


class ZoneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "item_name"})
    class Meta:
        model = Zone
        fields = ('name', 'isactive',)


class zone_search_form(forms.Form):
    CHOICES = (('Zone', '-------SELECT-------'),
               ('Zone', 'Zone'),
               )
    Field_Name = forms.ChoiceField(label="Field Name", choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)


class RegionForm(forms.ModelForm):
    class Meta:
        model = RegionMaster
        fields = ('zone','Region_Name')
        


class region_search_form(forms.Form):
    CHOICES = (('Region', '-------SELECT-------'),
               ('Region', 'Region'),
               )
    Field_Name = forms.ChoiceField(label="Field Name", choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)        

class StateForm(forms.ModelForm):
    class Meta:
        model = StateMaster
        fields = ('zone','region','State_Name','isactive',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].queryset = RegionMaster.objects.none()
        
        if 'zone' in self.data:
            try:
                zone_id = int(self.data.get('zone'))
                self.fields['region'].queryset = RegionMaster.objects.filter(zone_id=zone_id).order_by('Region_Name')

            except (ValueError, TypeError):
                pass
            
        elif self.instance.pk:
            self.fields['region'].queryset = self.instance.region.regionmaster_set.order_by('Region_Name')    

            

    

class state_search_form(forms.Form):
    CHOICES = (('State', '-------SELECT-------'),
               ('State', 'State'),
               )
    Field_Name = forms.ChoiceField(label="Field Name", choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False) 

class CityForm(forms.ModelForm):
    class Meta:
        model = CityMaster
        fields = ('zone','region','State','City_Name','isactive',)
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].queryset = RegionMaster.objects.none()
        self.fields['State'].queryset = StateMaster.objects.none()

        if 'zone' in self.data:
            try:
                zone_id = int(self.data.get('zone'))
                self.fields['region'].queryset = RegionMaster.objects.filter(zone_id=zone_id).order_by('Region_Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['region'].queryset = self.instance.zone.regionmaster_set.order_by('Region_Name')
                
        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['State'].queryset = StateMaster.objects.filter(region_id=region_id).order_by('State_Name')
            except (ValueError, TypeError):
                pass
            
        elif self.instance.pk:
            self.fields['State'].queryset = self.instance.region.statemaster_set.order_by('State_Name')    
                
            

class city_search_form(forms.Form):
    CHOICES = (('City', '-------SELECT-------'),
               ('City', 'City'),
               )
    Field_Name = forms.ChoiceField(label="Field Name", choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)           

class DistributorForm(forms.ModelForm):
    DL_NO_Valid_UPTO = forms.DateField(label='DL NO Valid UPTO',
                                           widget=forms.TextInput(
                                               attrs={'type': 'date'}
                                           ),required=False)

    class Meta:
        model = Distributor
        fields = ('Distributor_Code', 'Distributor_Name','zones','region','State', 'City', 'PinCode',
                  'Email_ID','Address', 'gstin', 'DL_NO', 'DL_NO_Valid_UPTO', 'pan',
                   'Contact_Person_Name', 'Contact_Number',)
        
        widgets = {
            'Address': forms.Textarea(attrs={'rows': 2, 'cols': 15}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].queryset = RegionMaster.objects.none()
        self.fields['State'].queryset = StateMaster.objects.none()
        self.fields['City'].queryset = CityMaster.objects.none()


        if 'zones' in self.data:
            try:
                zone_id = int(self.data.get('zones'))
                self.fields['region'].queryset = RegionMaster.objects.filter(zone_id=zone_id).order_by('Region_Name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['region'].queryset = self.instance.zones.regionmaster_set.order_by('Region_Name')

        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['State'].queryset = StateMaster.objects.filter(region_id=region_id).order_by('State_Name')
            
            except (ValueError, TypeError):
                pass
            
        elif self.instance.pk:
            self.fields['State'].queryset = self.instance.State.statemaster_set.order_by('State_Name')    
            
            
        if 'State' in self.data:
            try:
                state_id =  int(self.data.get('State'))
                self.fields['City'].queryset = CityMaster.objects.filter(State_id=state_id).order_by('City_Name')
                
            except (ValueError, TypeError):
                pass
            
        elif self.instance.pk:
            self.fields['City'].queryset = self.instance.City.citymaster_set.order_by('City_Name')        
                       

      
      
          
         
           

class distributor_search_form(forms.Form):
    CHOICES = (('Distributor', '-----SELECT-----'),
               ('Distributor_Name', 'Distributor_Name'),
               ('Distributor_Code', 'Distributor_Code'),
               ('Contact_Number', 'Contact_Number'),
               ('City', 'City'),
               ('State', 'State'),
               ('Address', 'Address'),
               ('EmailID', 'EmailID'),
               ('Pincode', 'Pincode'),
               ('gstin', 'gstin'),
               ('pan', 'pan'),
               )
    Field_Name = forms.ChoiceField(label="Field Name", choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)


class dbprice_master_searchform(forms.Form):
    CHOICES = (('DBPriceMaster', '-----SELECT-----'),
               ('Distributor Code', 'Distributor Code'),
               ('Item Code', 'Item Code'),
               ('Rate', 'Rate'),
               )
    Field_Name = forms.ChoiceField(label="Field Name", choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)


class DBPriceMasterForm(forms.ModelForm):
    class Meta:
        model = DBPriceMaster
        fields = ('distributor','item','Rate',)



class ItemForm(forms.ModelForm):
    GST_Applicable_From = forms.DateField(label="GST Applicable From",
                                          widget=forms.TextInput(
                                              attrs={'type': 'date'}
                                          )
                                          )

    class Meta:
        model = Item
        exclude = ('distributor','isactive',)
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Hierarchy2'].queryset = Hierarchy2.objects.none()
        self.fields['Hierarchy3'].queryset = Hierarchy3.objects.none()
        self.fields['Hier4'].queryset = Hier4.objects.none()
        self.fields['Hier5'].queryset = Hier5.objects.none()
        
        
        if 'Hierarchy1' in self.data:
            try:
                hier_i = int(self.data.get('Hierarchy1'))
                self.fields['Hierarchy2'].queryset = Hierarchy2.objects.filter(hierarchy1_id=hier_i).order_by('Name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['Hierarchy2'].queryset = self.instance.Hierarchy1.hierarchy2_set.order_by('Name')


        if 'Hierarchy2' in self.data:
            try:
                hier_2 = int(self.data.get('Hierarchy2'))
                self.fields['Hierarchy3'].queryset = Hierarchy3.objects.filter(hierarchy2_id=hier_2).order_by('Name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['Hierarchy3'].queryset = self.instance.Hierarchy2.hierarchy3_set.order_by('Name')
            
        
        if 'Hierarchy3' in self.data:
            try:
                hier3_id = int(self.data.get('Hierarchy3'))
                self.fields['Hier4'].queryset = Hierarchy4.objects.filter(hierarchy3_id=hier3_id).order_by('Name')
            
            except (ValueError, TypeError):
                pass
        
        elif self.instance.pk:
            self.fields['Hier4'].queryset = self.instance.Hier4.hierarchy4_set.order_by('name')
        
                    

        if 'Hier4' in self.data:
            try:
                hier4_id = int(self.data.get('Hier4'))
                self.fields['Hier5'].queryset = Hierarchy5.objects.filter(hierarchy4_id=hier4_id).order('Name')
            
            except (ValueError, TypeError):
                pass
            
        elif self.instance.pk:
            self.fields['Hier5'].queryset = self.data.instance.Hier5.hierarchy5_set.order_by('Name')        
        
        
        
        
        
class item_search_form(forms.Form):
    CHOICES = (
        ('Item', '-----SELECT-----'),
        ('Item Name', 'Item Name'),
        ('Item Code', 'Item Code'),
        ('Batch Enabled', 'Batch Enabled'),
        ('Principal Company', 'Principal Company'),
        ('MRP', 'MRP'),
        ('Hierarchy1', 'Hierarchy1'),
        ('Hierarchy2', 'Hierarchy2'),
        ('Hierarchy3', 'Hierarchy3'),
        ('HSN Code', 'HSN Code'),
        # ('GST Rate', 'GST Rate'),
        ('GST Applicable From', 'GST Applicable From'),

    )
    Field_Name = forms.ChoiceField(choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)


class HierarchyForm1(forms.ModelForm):
    Name = forms.CharField(max_length=50, required=True)
    class Meta:
        model = Hierarchy1
        fields = ['Name']


class hierarchy1_search_form(forms.Form):
    CHOICES = (
        ('Hierarchy1', '-----SELECT-----'),
        ('Hierarchy 1', 'Hierarchy 1')
    )
    Field_Name = forms.ChoiceField(choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)


class HierarchyForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HierarchyForm2, self).__init__(*args, **kwargs)
        self.fields['Name'].required = True 
    class Meta:
        model = Hierarchy2
        exclude = ('isacitve',)


class hierarchy2_search_form(forms.Form):
    CHOICES = (
        ('Hierarchy2', '-----SELECT-----'),
        ('Hierarchy 1', 'Hierarchy 1'),
        ('Hierarchy 2', 'Hierarchy 2'),
    )
    Field_Name = forms.ChoiceField(choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)


class HierarchyForm3(forms.ModelForm):
    class Meta:
        model = Hierarchy3
        exclude = ('isacitve',)
      
    def __init__(self, *args, **kwargs):
        super(HierarchyForm3,self).__init__(*args, **kwargs)
        self.fields['hierarchy2'].queryset = Hierarchy2.objects.none()
        
        if 'hierarchy1' in self.data:
            try:
                hier1_id = int(self.data.get('hierarchy1'))
                self.fields['hierarchy2'].queryset = Hierarchy2.objects.filter(hierarchy1_id=hier1_id).order_by('Name')
            
            except (ValueError, TypeError):
                pass
            
        elif self.instance.id:
            self.fields['hierarchy2'].queryset = self.instance.hierarchy2.hierarchy2_set.order_by('Name')      
    

class hierarchy3_search_form(forms.Form):
    CHOICES = (
        ('Hierarchy3', '-----SELECT-----'),
        ('Hierarchy 1', 'Hierarchy 1'),
        ('Hierarchy 2', 'Hierarchy 2'),
        ('Hierarchy 3', 'Hierarchy 3'),
    )
    Field_Name = forms.ChoiceField(choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)


class HierarchyForm4(forms.ModelForm):
    class Meta:
        model = Hierarchy4
        exclude = ('isacitve',)
        
    def __init__(self, *args, **kwargs):
        super(HierarchyForm4, self).__init__(*args, **kwargs)
        
        self.fields['hierarchy2'].queryset = Hierarchy2.objects.none()
        self.fields['hierarchy3'].queryset = Hierarchy3.objects.none()
        
        if 'hierarchy1' in self.data:
            try:
                hier1_id = int(self.data.get('hierarchy1'))
                self.fields['hierarchy2'].queryset = Hierarchy2.objects.filter(hierarchy1_id=hier1_id).order_by('Name')
                
            except (ValueError, TypeError):
                pass
        
        elif self.instance.id:
            self.fields['hierarchy2'].queryset = self.instance.hierarchy2.hierarchy2_set.order_by('Name')
        
        if 'hierarchy2' in self.data:
            try:
                hier2_id = int(self.data.get('hierarchy2'))
                self.fields['hierarchy3'].queryset = Hierarchy3.objects.filter(hierarchy2_id=hier2_id).order_by('Name')
            
            except (ValueError, TypeError):
                pass
        
        elif self.instance.id:
            self.fields['hierarchy3'].queryset =  self.instance.hierarchy3.hierarchy3_set.order_by('Name')      
    

class hierarchy4_search_form(forms.Form):
    CHOICES = (
        ('Hierarchy4', '-----SELECT-----'),
        ('Hierarchy 1', 'Hierarchy 1'),
        ('Hierarchy 2', 'Hierarchy 2'),
        ('Hierarchy 3', 'Hierarchy 3'),
        ('Hierarchy 4', 'Hierarchy 4'),
    )
    Field_Name = forms.ChoiceField(choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)


class HierarchyForm5(forms.ModelForm):
    class Meta:
        model = Hierarchy5
        exclude = ('isacitve',)
        
    
    def __init__(self, *args, **kwargs):
        super(HierarchyForm5, self).__init__(*args, **kwargs)
        self.fields['hierarchy2'].queryset = Hierarchy2.objects.none()
        self.fields['hierarchy3'].queryset = Hierarchy3.objects.none()
        self.fields['hierarchy4'].queryset = Hierarchy4.objects.none()
        
        if 'hierarchy1' in self.data:
            try:
                hier1_id = int(self.data.get('hierarchy1'))
                self.fields['hierarchy2'].queryset = Hierarchy2.objects.filter(hierarchy1_id=hier1_id).order_by('Name')
            
            except (ValueError, TypeError):
                pass
            
        elif self.instance.id:
            self.fields['hierarchy2'].queryset = self.instance.hierarchy2.hierarchy2_set.order_by('Name')
        
        if 'hierarchy2' in self.data:
            try:
                hier2_id = int(self.data.get('hierarchy2'))
                self.fields['hierarchy3'].queryset = Hierarchy3.objects.filter(hierarchy2_id=hier2_id).order_by('Name')
            
            except (ValueError, TypeError):
                pass
            
        elif self.instance.id:
            self.fields['hierarchy3'].queryset = self.instance.hierarchy3.hierarchy3_set.order_by('Name')
        
        if 'hierarchy3' in self.data:
            try:
                hier3_id = int(self.data.get('hierarchy3'))
                self.fields['hierarchy4'].queryset = Hierarchy4.objects.filter(hierarchy3_id=hier3_id).order_by('Name')
            
            except (ValueError, TypeError):
                pass
        
        elif self.instance.id:
            self.fields['hierarchy4'].queryset = self.instance.hierarchy4.hierarchy4_set.order_by('Name')
                                      
                
        
        


class hierarchy5_search_form(forms.Form):
    CHOICES = (
        ('Hierarchy5', '-----SELECT-----'),
        ('Hierarchy 1', 'Hierarchy 1'),
        ('Hierarchy 2', 'Hierarchy 2'),
        ('Hierarchy 3', 'Hierarchy 3'),
        ('Hierarchy 4', 'Hierarchy 4'),
        ('Hierarchy 5', 'Hierarchy 5'),
    )
    Field_Name = forms.ChoiceField(choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)



class SalesForm(forms.ModelForm):
    Customer_Name = forms.CharField(disabled=True, required=False)
    Bill_Date = forms.DateField(label="Sales Order Date", initial=today_ymd,widget=forms.TextInput(attrs={'type': 'date'}))
    cust_po_date = forms.DateField(label="Customer PO Date", widget=forms.TextInput(attrs={'type':'date'}))
    
    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args, **kwargs)
        self.fields['sales_order_no'].widget.attrs.update({'readonly':'readonly'})
        self.fields['Bill_Date'].widget.attrs.update({'readonly':'readonly'})
        self.fields['Customer_Name'].widget.attrs.update({'readonly':'readonly'})
        
    class Meta:
        model = Sales
        fields = ('Customers', 'Customer_Name','sales_order_no','Bill_Date', 'Invoice_No','cust_po_no','cust_po_date',
                  'Tally_MasterID', 'Total_Inventory_Amount','gst_type', 'Total_GST', 'CGST_AMOUNT', 'SGST_AMOUNT',
                  'Cash_Discount_Amount',
                   'Total_Invoice_Amount',)
        

    def get_initial_for_field(self, field, field_name):
        if field_name == 'sales_order_no' and not self.instance.pk:
            # Check if the field is 'order_number' and if it's a new instance (no primary key)
            last_order = Sales.objects.last()
            if last_order:
                last_order_number = last_order.id
                # Increment the last order number and set it as the initial value
                order_patt = OrderGenerator.objects.get(documentType="Sales")
                new_order_number = str(order_patt.prfx) +str(order_patt.seprator_choice) + str(int(last_order_number) + 1).zfill(len(order_patt.seqnum))
                return new_order_number
            return 'SO/001'  # Default initial value if there are no existing orders
        return super().get_initial_for_field(field, field_name)   
        

class DetailSaleForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs): 
        super(DetailSaleForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''
        #self.fields['Sales_Item_Code'].widget.attrs.update({'class':'Item_Code'})
        self.fields['Sales_Item_Name'].widget.attrs.update({'class':'ItemName','readonly':'readonly'})
        self.fields['Sales_Quantity'].widget.attrs.update({'class': 'textinput form-control setprice Quantity', 'min': '0', 'required': 'true'})
        self.fields['sale_uom'].widget.attrs.update({'class':'UOM', 'readonly':'readonly'})
        self.fields['Sales_Rate'].widget.attrs.update({'class':"Rate"})
        self.fields['Sales_Discount'].widget.attrs.update({'class':'Discount'})
        self.fields['Total_Amount'].widget.attrs.update({'class': 'textinput form-control setprice Amount', 'min': '0', 'required': 'true'})

    class Meta:
        model = Sales_Detail
        fields = ('Sales_Item_Code', 'Sales_Item_Name','Sales_Quantity','sale_uom', 'Sales_Rate','Sales_Discount','Total_Amount',)



    def clean(self):
        cleaned_data = super().clean()
        Quantity = cleaned_data.get('Sales_Quantity')
        if Quantity is not None and Quantity <= 0:
            self.add_error('Sales_Quantity', 'Quantity cannot be less than equal to 0.')

        return cleaned_data  

LineItemFormset = formset_factory(DetailSaleForm,extra=1)




class DeliveryNoteForm(forms.ModelForm):
    delivery_note_date = forms.DateField(label="Delivery Note Date", initial=today_ymd, widget=forms.TextInput(attrs={'type':'date'}))
    sales_order_date = forms.DateField(label="Sales Order Date", widget=forms.TextInput(attrs={'type':'date'}))
    cust_po_date = forms.DateField(label="Customer PO Date", widget=forms.TextInput(attrs={'type':'Date'}))
     
    def __init__(self, *args, **kwargs):
        super(DeliveryNoteForm, self).__init__(*args, **kwargs)
        self.fields['Customer_Name'].widget.attrs.update({'readonly':'readonly'})
        self.fields['delivery_note_date'].widget.attrs.update({'readonly':'readonly'})
        self.fields['delivery_note_no'].widget.attrs.update({'readonly':'readonly'})
    

    class Meta:
        model = Delivery_Note
        fields = ('delivery_note_no', 'delivery_note_date','cust_po_no','cust_po_date', 'Customers', 'Customer_Name','sales_order_no','sales_order_date','Bill_Date',
                  'Total_Inventory_Amount','gst_type', 'Total_GST', 'SGST_AMOUNT', 'CGST_AMOUNT', 
                  'Cash_Discount_Amount',
                 'Total_Amount','warehouse',
                  )
    
    
    def get_initial_for_field(self, field, field_name):
        if field_name == 'delivery_note_no' and not self.instance.pk:
            # Check if the field is 'order_number' and if it's a new instance (no primary key)
            last_order = Delivery_Note.objects.last()
            if last_order:
                last_order_number = last_order.id
                # Increment the last order number and set it as the initial value
                order_patt = OrderGenerator.objects.get(documentType="Delivery_Note")
                new_order_number = str(order_patt.prfx) +str(order_patt.seprator_choice) + str(int(last_order_number) + 1).zfill(len(order_patt.seqnum))
                return new_order_number
            return 'DN/001'  # Default initial value if there are no existing orders
        return super().get_initial_for_field(field, field_name)       


class DeliveryNoteDetailForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''
        self.fields['items'].widget.attrs.update({'class':'Item_Code'})
        self.fields['Item_Name'].widget.attrs.update({'class':'ItemName','readonly':'readonly'})
        self.fields['Quantity'].widget.attrs.update({'class': 'textinput form-control setprice Quantity', 'min': '0', 'required': 'true'})
        self.fields['bal_qty'].widget.attrs.update({'class': 'textinput form-control setprice bal_qty', 'min': '0', 'required': 'true','readonly':'readonly'})
        self.fields['uom'].widget.attrs.update({'class':'UOM', 'readonly':'readonly'})
        self.fields['Rate'].widget.attrs.update({'class':"Rate"})
        self.fields['Discount'].widget.attrs.update({'class':'Discount'})
        self.fields['Serial_No'].widget.attrs.update({'class':"SNo"})
        self.fields['Amount'].widget.attrs.update({'class': 'textinput form-control setprice Amount', 'min': '0', 'required': 'true'})

    class Meta:
        model = Delivery_Note_Details
        fields = ('items', 'Item_Name', 'Quantity','bal_qty', 'Rate', 'Discount', 'Serial_No','uom','Amount',)


    
    def clean(self):
        cleaned_data = super().clean()
        Quantity = cleaned_data.get('Quantity')
        if Quantity is not None and Quantity <= 0:
            self.add_error('Quantity', 'Quantity cannot be less than equal to 0.')

        return cleaned_data  

deliveryNoteLineItem = formset_factory(DeliveryNoteDetailForm, extra=1)





class UploadFileForm(forms.Form):
    file = forms.FileField()


    

class PurchaseDocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PurchaseDocumentForm, self).__init__(*args, **kwargs)
        self.fields['Bill_Date'].initial = today_ymd
        self.fields['Distributor_Name'].widget.attrs.update({'readonly':'readonly'})
        self.fields['Bill_Date'].widget.attrs.update({'readonly':'readonly'})
        self.fields['SAP_Order_No'].widget.attrs.update({'readonly':'readonly'})
    class Meta:
        model = PurchaseDocument
        fields = (
            'Distributors', 'Distributor_Name', 'Bill_Date', 'SAP_Order_No',
            'Total_Inventory_Amount', 'Total_GST','gst_type' ,'SGST_AMOUNT', 'CGST_AMOUNT',
            'Vendor_Name','total_discount_amount','Total_Invoice_Amount'
        )
  
    def get_initial_for_field(self, field, field_name):
        if field_name == 'SAP_Order_No' and not self.instance.pk:
            # Check if the field is 'order_number' and if it's a new instance (no primary key)
            last_order = PurchaseDocument.objects.last()
            if last_order:
                last_order_number = last_order.id
                # Increment the last order number and set it as the initial value
                order_patt = OrderGenerator.objects.get(documentType="PurchaseDocument")
                new_order_number = str(order_patt.prfx) +str(order_patt.seprator_choice) + str(int(last_order_number) + 1).zfill(len(order_patt.seqnum))
                return new_order_number
            return 'PO/001'  # Default initial value if there are no existing orders
        return super().get_initial_for_field(field, field_name)   


class PurchaseChildForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PurchaseChildForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''
        self.fields['items'].widget.attrs.update({'class':'Item_Code', 'readonly':'readonly'})
        self.fields['item_name'].widget.attrs.update({'class':'ItemName','readonly':'readonly'})
        self.fields['purchase_uom'].widget.attrs.update({'class':'UOM', 'readonly':'readonly'})
        self.fields['Purchases_Quantity'].widget.attrs.update({'class': 'textinput form-control setprice Quantity', 'min': '0', 'required': 'true'})
        self.fields['Purchase_Rate'].widget.attrs.update({'class':"Rate"})
        self.fields['Purchase_Product_Discount'].widget.attrs.update({'class':'Discount'})
        self.fields['Purchases_Serial_No'].widget.attrs.update({'class':"SNO"})
        self.fields['Total_Amount'].widget.attrs.update({'class': 'textinput form-control setprice Amount', 'min': '0', 'required': 'true'})

    class Meta:
        model = DetailOfPurchase

        fields = ('items', 'item_name', 'Purchases_Quantity','purchase_uom','Purchase_Rate', 'Purchase_Product_Discount','Purchases_Serial_No',
            'Total_Amount',)
        
    
    def clean(self):
        cleaned_data = super().clean()
        Quantity = cleaned_data.get('Purchases_Quantity')
        if Quantity is not None and Quantity <= 0:
            self.add_error('Purchases_Quantity', 'Quantity cannot be less than equal to 0.')

        return cleaned_data    

PurchaseLineItemFormset = formset_factory(PurchaseChildForm, extra=1)





class ReceiptNoteForm(forms.ModelForm):
    Bill_Date = forms.DateField(label='Purchase Order Date',widget=forms.TextInput(attrs={'type': 'date'}))
    receipt_note_date = forms.DateField(label="MRN Date", initial=today_ymd, widget=forms.TextInput(attrs={'type':'date'}))
    supplier_invoice_date = forms.DateField(label="Supplier Invoice Date", widget=forms.TimeInput(attrs={'type':'date'})) 
    def __init__(self, *args, **kwargs):
        super(ReceiptNoteForm, self).__init__(*args, **kwargs)
        self.fields['Invoice_No'].widget.attrs.update({'required':'required'})
        self.fields['Distributor_Name'].widget.attrs.update({'readonly':'readonly'})
        self.fields['recipt_no'].widget.attrs.update({'readonly':'readonly'})
        
        
    class Meta:
        model = Receipt_Note
        fields = ('billing_entity','recipt_no','receipt_note_date','Distributors','Distributor_Name','p_order_no','Bill_Date',
                  'Invoice_No','supplier_invoice_date',
                   'Total_GST', 'SGST_AMOUNT', 'CGST_AMOUNT', 'IGST_AMOUNT',
                  'Cash_Discount_Amount','gst_type',
                  'R_O_Amount','Total_Inventory_Amount', 'Total_Amount','warehouse',
                  )
        
    def get_initial_for_field(self, field, field_name):
        if field_name == 'recipt_no' and not self.instance.pk:
            # Check if the field is 'order_number' and if it's a new instance (no primary key)
            last_order = Receipt_Note.objects.last()
            if last_order:
                last_order_number = last_order.id
                # Increment the last order number and set it as the initial value
                order_patt = OrderGenerator.objects.get(documentType="Receipt_Note")
                new_order_number = str(order_patt.prfx) +str(order_patt.seprator_choice) + str(int(last_order_number) + 1).zfill(len(order_patt.seqnum))
                return new_order_number
            return 'MRN/001'  # Default initial value if there are no existing orders
        return super().get_initial_for_field(field, field_name)    
    


class ReceiptNoteDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReceiptNoteDetailForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''
        self.fields['items'].widget.attrs.update({'class':'Item_Code'})
        self.fields['Item_Name'].widget.attrs.update({'class':'ItemName','readonly':'readonly'})
        self.fields['Quantity'].widget.attrs.update({'class': 'textinput form-control setprice Quantity', 'min': '0', 'required': 'true'})
        self.fields['bal_qty'].widget.attrs.update({'class': 'textinput form-control setprice bal_qty', 'readonly':'readonly'})
        self.fields['uom'].widget.attrs.update({'class':"UOM", 'readonly':'readonly'})
        self.fields['Rate'].widget.attrs.update({'class':"Rate"})
        self.fields['Discount'].widget.attrs.update({'class':'Discount'})
        self.fields['Serial_No'].widget.attrs.update({'class':"SNO"})
        self.fields['Total_Amount'].widget.attrs.update({'class': 'textinput form-control setprice Amount', 'min': '0', 'required': 'true'})
                         

    class Meta:
        model = Receipt_Note_Detail
        fields = ('items', 'Item_Name', 'Quantity', 'bal_qty','uom','Rate', 'Discount', 'Serial_No', 'Total_Amount',)


    def clean(self):
        cleaned_data = super().clean()
        Quantity = cleaned_data.get('Quantity')
        if Quantity is not None and Quantity <= 0:
            self.add_error('Quantity', 'Quantity cannot be less than equal to 0.')

        return cleaned_data 


ReceiptNoteLineItem = formset_factory(ReceiptNoteDetailForm, extra=1)


class Password_Policy_Form(forms.ModelForm):
    other_choices = (
        (1, 'User ID'),
        (2, 'Distributor Name'),
        (3, 'Distributor Code'),
    )
    others = forms.ChoiceField(choices=other_choices)

    class Meta:
        model = Entity
        fields = ('MinChar', 'MaxChar', 'PassType', 'Passexpdays', 'PassexpMsgDays', 'Autounlockhour', 'minPassAttempt',
                  'others',)


class StockForm(forms.Form):
    item_name = forms.CharField(max_length=50)
    start_date = forms.DateField(label='Start Date',widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date',widget=forms.TextInput(attrs={'type': 'date'}))





class TaxForm(forms.ModelForm):
    class Meta:
        model = TaxMaster
        fields = ('Tax_Type','name','value','CGST','SGST','taxinputrecoverable',)
        
class tax_search_form(forms.Form):
    CHOICES = (('name', '-----SELECT-----'),
               ('name', 'name'),
               ('value', 'value'),

               )
    Field_Name = forms.ChoiceField(label="Field Name", choices=CHOICES, required=False)
    Value = forms.CharField(widget=forms.TextInput(), required=False)

class UomForm(forms.ModelForm):
    class Meta:
        model = UOM
        fields = ('UNT','unit_notation','unit_name','conversion_factor','status','base_unit',)            
        
class warehouseForm(forms.ModelForm):
    
    class Meta:
        model = Warehouse
        fields = ('wcode','wname',)     
        
 
 
class warehouseItemForm(forms.ModelForm):       
    Date = forms.DateField(label='Date',initial=today_ymd,widget=forms.TextInput(attrs={'type': 'date'}),required=False)
    def __init__(self, *args, **kwargs):
        super(warehouseItemForm, self).__init__(*args, **kwargs)
        self.fields['warehouseName'].widget.attrs.update({'class': 'textinput form-control','readonly':'readonly','required':'required'})
        self.fields['w_order_no'].widget.attrs.update({'readonly':'readonly'})
        
    class Meta:
        model = warehouseStock
        fields = ('warehouseCode','warehouseName','w_order_no','Date',) 
        
    def get_initial_for_field(self, field, field_name):
        if field_name == 'w_order_no' and not self.instance.pk:
            # Check if the field is 'order_number' and if it's a new instance (no primary key)
            last_order = warehouseStock.objects.last()
            if last_order:
                last_order_number = last_order.id
                # Increment the last order number and set it as the initial value
                order_patt = OrderGenerator.objects.get(documentType="openingbalance")
                new_order_number = str(order_patt.prfx) +str(order_patt.seprator_choice) + str(int(last_order_number) + 1).zfill(len(order_patt.seqnum))
                return new_order_number
            return 'OB/001'  # Default initial value if there are no existing orders
        return super().get_initial_for_field(field, field_name)    
       
class warehouseItemChildForm(forms.ModelForm):   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''
        self.fields['Item_Code'].widget.attrs.update(({'class':"Item_Code",'required': 'true'}))
        self.fields['Item_Name'].widget.attrs.update({'class': 'ItemName','required': 'true','readonly':'readonly'})
        self.fields['Quantity'].widget.attrs.update({'class': 'textinput form-control setprice Quantity', 'min': '0', 'required': 'true'})
        self.fields['base_uom'].widget.attrs.update({'class':"UOM", 'readonly':'readonly'})
        self.fields['Rate'].widget.attrs.update({'class':"Rate"})
        self.fields['Discount'].widget.attrs.update({'class':'Discount'})
        self.fields['SNo'].widget.attrs.update({'class':"SNO"})
        self.fields['Total_Amount'].widget.attrs.update({'class': 'textinput form-control setprice Amount', 'min': '0', 'required': 'true'}) 
                       
    class Meta:
        model = warehouseItemChild
        fields = ['Item_Code','Item_Name','Quantity','base_uom','Rate','SNo','Discount','Total_Amount']

    def clean(self):
        cleaned_data = super().clean()
        Quantity = cleaned_data.get('Quantity')
        if Quantity is not None and Quantity <= 0:
            self.add_error('Quantity', 'Quantity cannot be less than equal to 0.')

        return cleaned_data
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     item = cleaned_data.get('Item_Code')

    #     # Check if an object with the same name already exists
    #     if warehouseItemChild.objects.filter(Item_Code=item).exists():
    #         raise ValidationError("An object with this name already exists.")
            
        
        # return cleaned_data
    
        
    
    
    
warehouselineItemformset = formset_factory(warehouseItemChildForm, extra=1)        



class purchaseinoviceForm(forms.ModelForm):
    purchase_invoice_date = forms.DateField(label="Purchase Invoice Date", initial=today_ymd, widget=forms.TextInput(attrs={'type':'date'}))
    Bill_Date = forms.DateField(label='Purchase Order Date', widget=forms.TextInput(attrs={'type':'date'}))
    SAP_Order_Date = forms.DateField(label='Supplier Invoice Date', widget=forms.TextInput(attrs={'type':'date'}))
    mrn_date = forms.DateField(label="MRN Date", widget=forms.TextInput(attrs={'type':'date'}))
    
    def __init__(self, *args, **kwargs):
        super(purchaseinoviceForm, self).__init__(*args, **kwargs)
        self.fields['Distributor_Name'].widget.attrs.update({'readonly':'readonly'})
        self.fields['purchase_invoice_no'].widget.attrs.update({'readonly':'readonly'})
        self.fields['purchase_invoice_date'].widget.attrs.update({'readonly':'readonly'})
        self.fields['total_discount_amount'].widget.attrs.update({'readonly':'readonly'})
        
    class Meta:
        model=PurchaseInvoice
        fields = ('Distributors','Distributor_Name','mrn_no','mrn_date','Bill_Date','Supplier_Invoice_No','purchase_invoice','SAP_Order_Date','gst_type','Total_Inventory_Amount','Total_GST','SGST_AMOUNT','CGST_AMOUNT','Vendor_Name','PO_No','Total_Invoice_Amount','total_discount_amount','purchase_invoice_no','purchase_invoice_date',)


    def get_initial_for_field(self, field, field_name):
        if field_name == 'purchase_invoice_no' and not self.instance.pk:
            # Check if the field is 'order_number' and if it's a new instance (no primary key)
            last_order = PurchaseInvoice.objects.last()
            if last_order:
                last_order_number = last_order.id
                # Increment the last order number and set it as the initial value
                order_patt = OrderGenerator.objects.get(documentType="PurchaseInvoice")
                new_order_number = str(order_patt.prfx) +str(order_patt.seprator_choice) + str(int(last_order_number) + 1).zfill(len(order_patt.seqnum))
                return new_order_number
            return 'PI/001'  # Default initial value if there are no existing orders
        return super().get_initial_for_field(field, field_name)  
    
    
class purchaseinvoicelineitemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''
        self.fields['items'].widget.attrs.update(({'class':"Item_Code",'required': 'true'}))
        self.fields['item_name'].widget.attrs.update({'class': 'ItemName','required': 'true','readonly':'readonly'})
        self.fields['Quantity'].widget.attrs.update({'class': 'textinput form-control setprice Quantity', 'min': '0', 'required': 'true'})
        self.fields['bal_qty'].widget.attrs.update({'class': 'textinput form-control setprice bal_qty', 'min': '0' ,'readonly':'readonly'})
        self.fields['UOM'].widget.attrs.update({'class':"UOM", 'readonly':'readonly'})
        self.fields['Rate'].widget.attrs.update({'class':"Rate"})
        self.fields['Discount'].widget.attrs.update({'class':'Discount'})
        self.fields['Serial_No'].widget.attrs.update({'class':"SNO"})
        self.fields['Total_Amount'].widget.attrs.update({'class': 'textinput form-control setprice Amount', 'min': '0', 'required': 'true'})
                       
    class Meta:
        model = PurchaseinvoicelineItem
        fields = ('items','item_name','Quantity','bal_qty','UOM','Rate','Discount','Serial_No','Total_Amount')
    
    def clean(self):
        cleaned_data = super().clean()
        Quantity = cleaned_data.get('Quantity')
        if Quantity is not None and Quantity <= 0:
            self.add_error('Quantity', 'Quantity cannot be less than equal to 0.')

        return cleaned_data 
        
purchaseinvoicelineitem = formset_factory(purchaseinvoicelineitemForm, extra=1)



class PurchaseReturnDocumentForm(forms.ModelForm):
    Total_GST = forms.FloatField(required=False, label='Total GST Amount', initial=0, disabled=True)
    Bill_Date = forms.DateField(label='PR Date',initial=today_ymd,widget=forms.TextInput(attrs={'type': 'date'}))
    SAP_Order_Date = forms.DateField(label='Supplier Invoice Date',widget=forms.TextInput(attrs={'type': 'date'}))
    pi_date = forms.DateField(label="PI Date", widget=forms.TextInput(attrs={'type':'date'}))
      
    def __init__(self, *args, **kwargs):
        super(PurchaseReturnDocumentForm, self).__init__(*args, **kwargs)
        self.fields['Bill_Date'].widget.attrs.update({'readonly':'readonly'})
        self.fields['pi_date'].widget.attrs.update({'readonly':'readonly'})
        self.fields['Supplier_Invoice_No'].widget.attrs.update({'readonly':'readonly'})
        self.fields['SAP_Order_Date'].widget.attrs.update({'readonly':'readonly'})
        self.fields['distributor_name'].widget.attrs.update({'readonly':'readonly'})
        self.fields['SAP_Order_No'].widget.attrs.update({'readonly':'readonly'})

        
    
    class Meta:
        model = PurchaseReturnDocument
        fields = ('Distributors','distributor_name','Bill_Date', 'Supplier_Invoice_No','pi_no','pi_date',
                  'SAP_Order_No', 'SAP_Order_Date', 'Total_Inventory_Amount', 'Total_GST',
                  'SGST_AMOUNT', 'CGST_AMOUNT','gst_type','total_discount_amount',
                  'Vendor_Name','Total_Invoice_Amount','warehouse'
                  )

    
    def get_initial_for_field(self, field, field_name):
        if field_name == 'SAP_Order_No' and not self.instance.pk:
            # Check if the field is 'order_number' and if it's a new instance (no primary key)
            last_order = PurchaseReturnDocument.objects.last()
            if last_order:
                last_order_number = last_order.id
                # Increment the last order number and set it as the initial value
                order_patt = OrderGenerator.objects.get(documentType="PurchaseReturnDocument")
                new_order_number = str(order_patt.prfx) +str(order_patt.seprator_choice) + str(int(last_order_number) + 1).zfill(len(order_patt.seqnum))
                return new_order_number
            return 'PR/001'  # Default initial value if there are no existing orders
        return super().get_initial_for_field(field, field_name)  

class DetailOfPurchaseReturnForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = ''
        self.fields['items'].widget.attrs.update(({'class':"Item_Code",'required': 'true'}))
        self.fields['Item_Name'].widget.attrs.update({'class': 'ItemName','required': 'true','readonly':'readonly'})
        self.fields['Purchases_Return_Quantity'].widget.attrs.update({'class': 'textinput form-control setprice Quantity', 'min': '0', 'required': 'true'})
        self.fields['purchase_uom'].widget.attrs.update({'class':"UOM", 'readonly':'readonly'})
        self.fields['Purchase_Rate'].widget.attrs.update({'class':"Rate"})
        self.fields['Purchase_Product_Discount'].widget.attrs.update({'class':'Discount'})
        self.fields['Total_Amount'].widget.attrs.update({'class': 'textinput form-control setprice Amount', 'min': '0', 'required': 'true'})
                       
    
    class Meta:
        model = DetailsOfPurchaseReturn
        fields = ('items', 'Item_Name', 'Purchases_Return_Quantity','purchase_uom', 'Purchase_Rate',
                  'Purchase_Product_Discount','Total_Amount',)

    def clean(self):
        cleaned_data = super().clean()
        Quantity = cleaned_data.get('Purchases_Return_Quantity')
        if Quantity is not None and Quantity <= 0:
            self.add_error('Purchases_Return_Quantity', 'Quantity cannot be less than equal to 0.')

        return cleaned_data 
    
PurchaseReturnLineItem = formset_factory(DetailOfPurchaseReturnForm, extra=1)



class saleinvoiceform(forms.ModelForm):
    sale_order_date = forms.DateField(label="Sales Order Date", widget=forms.TextInput(attrs={'type': 'date'}))
    Bill_Date = forms.DateField(label='Sales Invoice Date', initial=today_ymd ,widget=forms.TextInput(attrs={'type':'date'}))
    dl_note_date = forms.DateField(label="Delivery Note Date", widget=forms.TextInput(attrs={'type':'date'}))
 
    def __init__(self, *args, **kwargs):
        super(saleinvoiceform, self).__init__(*args, **kwargs)
        self.fields['Bill_Date'].widget.attrs.update({"readonly":'readonly'})
        self.fields['Customer_Name'].widget.attrs.update({"readonly":'readonly'})
        self.fields['dl_note_date'].widget.attrs.update({"readonly":'readonly'})
        self.fields['Invoice_No'].widget.attrs.update({"readonly":'readonly'})
        
    

    class Meta:
        model = salesInvoice
        fields = ('Customers','Customer_Name','dl_note_no','dl_note_date','sale_order','sale_order_date','Bill_Date','Invoice_No','gst_type','Total_Inventory_Amount','SGST_AMOUNT','CGST_AMOUNT','Total_GST','Cash_Discount_Amount','Total_Invoice_Amount',)



    def get_initial_for_field(self, field, field_name):
        if field_name == 'Invoice_No' and not self.instance.pk:
            # Check if the field is 'order_number' and if it's a new instance (no primary key)
            last_order = salesInvoice.objects.last()
            if last_order:
                last_order_number = last_order.id
                # Increment the last order number and set it as the initial value
                order_patt = OrderGenerator.objects.get(documentType="salesInvoice")
                new_order_number = str(order_patt.prfx) +str(order_patt.seprator_choice) + str(int(last_order_number) + 1).zfill(len(order_patt.seqnum))
                return new_order_number
            return 'SI/001'  # Default initial value if there are no existing orders
        return super().get_initial_for_field(field, field_name) 

class saleinvoiceItem(forms.ModelForm):
    
    def __init__(self, *args, **kwargs): 
        super(saleinvoiceItem, self).__init__(*args, **kwargs)
        
        for field_name in self.fields:
            self.fields[field_name].label = ''
            
        self.fields['Item_Code'].widget.attrs.update({'class':'Item_Code'})
        self.fields['Item_Name'].widget.attrs.update({'class':'ItemName','readonly':'readonly'})
        self.fields['Quantity'].widget.attrs.update({'class': 'textinput form-control setprice Quantity', 'min': '0', 'required': 'true'})
        self.fields['bal_qty'].widget.attrs.update({'class': 'textinput form-control setprice bal_qty', 'min': '0','readonly':'readonly','required': 'true'})
        self.fields['uom'].widget.attrs.update({'class':'UOM', 'readonly':'readonly'})
        self.fields['Rate'].widget.attrs.update({'class':"Rate"})
        self.fields['Serial_No'].widget.attrs.update({'class':'SNO'})
        self.fields['Discount'].widget.attrs.update({'class':'Discount'})
        self.fields['Amount'].widget.attrs.update({'class': 'textinput form-control setprice Amount', 'min': '0', 'required': 'true'})
        
    class Meta:
        model = saleinvoicelineItem
        fields = ('Item_Code','Item_Name','Quantity','bal_qty','uom','Rate','Serial_No','Discount','Amount',)    


    def clean(self):
        cleaned_data = super().clean()
        Quantity = cleaned_data.get('Quantity')
        if Quantity is not None and Quantity <= 0:
            self.add_error('Quantity', 'Quantity cannot be less than equal to 0.')

        return cleaned_data 
    

saleinvoicelineitemForm = formset_factory(saleinvoiceItem, extra=1)



class SaleReturnForm(forms.ModelForm):
    Bill_Date = forms.DateField(label="Sales Invoice Date",widget=forms.TextInput(attrs={'type': 'date'}))
    sales_return_date = forms.DateField(label="Sales Return Date",initial=today_ymd, widget=forms.TextInput(attrs={'type':'date'}))
  
    def __init__(self, *args, **kwargs):
        super(SaleReturnForm, self).__init__(*args, **kwargs)
        self.fields['Customer_Name'].widget.attrs.update({'readonly':'readonly'})
        self.fields['sales_return_date'].widget.attrs.update({'readonly':'readonly'})
        self.fields['sales_return_no'].widget.attrs.update({'readonly':'readonly'})
    
    class Meta:
        model = SalesReturn
        fields = ('Customers', 'Customer_Name','sales_return_no','sales_return_date','sale_invoice_no','Bill_Date',
                  'Total_Inventory_Amount','gst_type','Total_GST', 'CGST_AMOUNT', 'SGST_AMOUNT',
                  'Cash_Discount_Amount',
                  'Total_Invoice_Amount','warehouse')


    def get_initial_for_field(self, field, field_name):
        if field_name == 'sales_return_no' and not self.instance.pk:
            # Check if the field is 'order_number' and if it's a new instance (no primary key)
            last_order = SalesReturn.objects.last()
            if last_order:
                last_order_number = last_order.id
                # Increment the last order number and set it as the initial value
                order_patt = OrderGenerator.objects.get(documentType="SalesReturn")
                new_order_number = str(order_patt.prfx) +str(order_patt.seprator_choice) + str(int(last_order_number) + 1).zfill(len(order_patt.seqnum))
                return new_order_number
            return 'SR/001'  # Default initial value if there are no existing orders
        return super().get_initial_for_field(field, field_name) 
    
    

class salereturnLineItem(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        
        for field_name in self.fields:
            self.fields[field_name].label = ''
            
        self.fields['Sales_Item_Code'].widget.attrs.update({'class':'Item_Code'})
        self.fields['Sales_Item_Name'].widget.attrs.update({'class':'ItemName','readonly':'readonly'})
        self.fields['Sales_Quantity'].widget.attrs.update({'class': 'textinput form-control setprice Quantity', 'min': '0', 'required': 'true'})
        self.fields['sale_uom'].widget.attrs.update({'class':'UOM', 'readonly':'readonly'})
        self.fields['Sales_Rate'].widget.attrs.update({'class':"Rate"})
        self.fields['Sales_Serial_No'].widget.attrs.update({'class':'SNO'})
        self.fields['Sales_Discount'].widget.attrs.update({'class':'Discount'})
        self.fields['Total_Amount'].widget.attrs.update({'class': 'textinput form-control setprice Amount', 'min': '0', 'required': 'true'})
        
    class Meta:
        model = Sales_Return_Detail
        fields = ('Sales_Item_Code','Sales_Item_Name','Sales_Quantity','sale_uom','Sales_Rate','Sales_Serial_No','Sales_Discount','Total_Amount',)

    def clean(self):
        cleaned_data = super().clean()
        Quantity = cleaned_data.get('Sales_Quantity')
        if Quantity is not None and Quantity <= 0:
            self.add_error('Sales_Quantity', 'Quantity cannot be less than equal to 0.')

        return cleaned_data 
    


SaleReturnLineItem = formset_factory(salereturnLineItem, extra=1)



        
class orderGeneratorForm(forms.ModelForm):
    Field_selection=forms.CharField(label='Field Selection', widget=forms.RadioSelect(choices=TYPE_SELECT))
    class Meta:
        model = OrderGenerator
        fields = ('documentType','seprator_choice','prfx','sufx','Field_selection','seqnum','use_FY_as_prfx','use_FY_as_sufx','use_month_as_prfx','use_month_as_sufx','Document_for_prefix',)
        
        
        

class warehouseclosingBalance(forms.Form):
    w_name=forms.ModelChoiceField(queryset=Warehouse.objects.all(), label="Warehouse Name", required=False)
    items = forms.ModelChoiceField(queryset=Item.objects.all(), label="Select Item", required=False)
    date = forms.DateField(label='Date',widget=forms.TextInput(attrs={'type': 'date'}))
    



class ExcelImportForm(forms.Form):
    excel_file = forms.FileField()        