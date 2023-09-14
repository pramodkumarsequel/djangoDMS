from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django import forms
from .models import Event, MenuMaster, RoleMaster, RoleAssignment
from account.models import Distributor, Sales, FieldMaster, RoleMaster, User, Item
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Fieldset, Div
from django.forms import formset_factory, modelformset_factory
from django.contrib.auth.models import User
from django.db import transaction





class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


from .models import ReportsMaster
from reportsapp.Choices import choice_Date_Type

class DocumentMasterForm(forms.ModelForm):
    Date_Type = forms.ChoiceField(choices=choice_Date_Type,label="Date Type", required=False)
    value = forms.CharField(max_length=50, label='Manual field', required=False)
    From_Date = forms.DateField(label="From Date",
                                widget=forms.TextInput(
                                    attrs={'type': 'date'}
                                )
                                )
    To_Date = forms.DateField(label="To Date",
                              widget=forms.TextInput(
                                  attrs={'type': 'date'}
                              )
                              )

    class Meta:
        model = ReportsMaster
        fields = [

            'Document_Type',
            'fields',
            'value',
            'Date_Type',
            'From_Date',
            'To_Date',

        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fields'].queryset = FieldMaster.objects.none()

        if 'Document_Type' in self.data:
            try:
                doc_id = int(self.data.get('Document_Type'))
                self.fields['fields'].queryset = FieldMaster.objects.filter(
                    id=doc_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['fields'].queryset = self.instance.fields.FieldMaster.Field_Name_set.order_by('Field_Name')


class MenuMasterForm(forms.ModelForm):
    MTYPE = forms.CharField(max_length=20, initial="New",required=False, disabled=True, label="Menu Type")
    class Meta:
        model = MenuMaster
        fields = ('MTYPE','MenuName','Dord','Image','IsMobile','usrole','Is_View','Is_Create','is_Edit','is_Delete',)
        widgets = {
            'usrole':forms.CheckboxSelectMultiple,
        }        
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Row(
                    Column('MTYPE', css_class='form-group col-md-6')
                ),  
            )          
           
CHOICES = [ (supervisor.id, supervisor.get_pagelink())
            for supervisor in MenuMaster.objects.all() ]  
   
class SubMenuForm(forms.Form):
    PAGELINKTYPE =(
    ( "Select","---Select---"),
    ( "Static","Static"),
    ( "Master", "Master"),
    ( "Document","Document"),
    ("Reports","Reports"), 
    ( "DReport", "DReport"),
    ( "Calender", "Calender"),  
)
    Pmenu = forms.ModelChoiceField(queryset=MenuMaster.objects.all(), label="Select Parent Menu")    
    pagelinktype = forms.ChoiceField(choices=PAGELINKTYPE, label="Page Link Type")   
    pagelink = forms.ChoiceField(choices=CHOICES, label="Page Link") 
    MenuName = forms.CharField(max_length=50, required=True, label="Menu Name")
    Dord = forms.IntegerField(label="Display Order")
    IsMobile = forms.BooleanField(initial=False,label="Is Mobile", required=False)
    Image = forms.ImageField(required=False)



SubmenuFormset = formset_factory(SubMenuForm, extra=1)

from .Choices import PERM_CHOICES
class EditMenuForm(forms.ModelForm):
    permchoices = forms.MultipleChoiceField(choices=PERM_CHOICES)
    PAGELINKTYPE =(
    ( "Select","---Select---"),
    ( "Static","Static"),
    ( "Master", "Master"),
    ( "Document","Document"),
    ("Reports","Reports"), 
    ( "DReport", "DReport"),
    ( "Calender", "Calender"),  
)
    Pmenu = forms.ModelChoiceField(queryset=MenuMaster.objects.all(), label="Select Parent Menu")    
    pagelinktype = forms.ChoiceField(choices=PAGELINKTYPE, label="Page Link Type")   
    pagelink = forms.ChoiceField(choices=CHOICES, label="Page Link") 
    MenuName = forms.CharField(max_length=50, required=True, label="Menu Name")
    Dord = forms.IntegerField(label="Display Order")
    IsMobile = forms.BooleanField(initial=False,label="Is Mobile")
    Image = forms.ImageField()
    class Meta:
        model = MenuMaster
        fields = ['Pmenu','pagelink','MenuName','Dord','IsMobile','Image', 'usrole','Is_Create','Is_View','is_Edit','is_Delete']
        
class MenuChkLineItem(forms.Form):
    Is_View = forms.BooleanField(label='', required=False)
    Is_Create = forms.BooleanField(label='', required=False)
    is_Edit = forms.BooleanField(label='',required=False)
    is_Delete = forms.BooleanField(label='',required=False)
    
editMenuFormsetFactory = formset_factory(MenuChkLineItem,
                                            extra=1)

class checkboxform(forms.ModelForm):
    Is_View = forms.BooleanField(label='', required=False)
    Is_Create = forms.BooleanField(label='', required=False)
    is_Edit = forms.BooleanField(label='',required=False)
    is_Delete = forms.BooleanField(label='',required=False)
    class Meta:
        model = MenuMaster
        fields = ['Is_View', 'Is_Create','is_Edit','is_Delete']
        
        
    
checkboxformset = modelformset_factory(MenuMaster,
                                       fields=('Is_View','Is_Create','is_Edit','is_Delete')
                                       )        


# UserName = [(us.id, us.get_username()) for us in User.objects.all()]
# class roleAssignmentForm(forms.Form):
#     doc_choices = (
#         ('New','New'),
#         ('Doc Type','Doc Type'),
#     )
#     ROLE = forms.ModelChoiceField(queryset=RoleMaster.objects.all(), label="SELECT ROLE", required=True)
#     User = forms.ModelChoiceField(queryset=User.objects.all(), label="SELECT USER", required=True)
#     doc_type = forms.ChoiceField(choices=doc_choices,label="DOCUMENT TYPE",required=True)
    

class RoleAssignmentFilterForm(forms.Form):
        Source_page_choose = (
            ('Distributor','Distributor'),
            ('Claim Type','Claim Type'),
            ('Zone','Zone')
        )
        target_page=(
            ('Claim Type','Claim Type'),
            ('Zone','Zone')
        )
        Source_Page = forms.ChoiceField(choices=Source_page_choose, label="Source Page")
        Target_Page = forms.ChoiceField(choices=target_page, label="Target Page")
        

class DistributorMultiChoiceForm(forms.Form):
    Distributors = forms.ModelMultipleChoiceField(
                       widget = forms.CheckboxSelectMultiple,
                       queryset = Distributor.objects.all()
               )




from django import forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import default
from account.models import Distributor, Zone
from .models import ReportsMaster
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, ButtonHolder, Field, Reset
from crispy_forms.bootstrap import InlineCheckboxes

class SearchFilterForm(forms.ModelForm):
    """ Form For Advance Search of Quotes. """
    search_text = forms.CharField(
        widget=forms.TextInput,
        required=False
    )
    iscreate = forms.BooleanField(label="Can_Create",)
    isview = forms.BooleanField(label="Can_View")
    isedit = forms.BooleanField(label="Can_Edit")
    
    # distributors = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=[('','All'),] + [(distributor.id, distributor.Distributor_Name) for distributor in Distributor.objects.all()],
    #     required=False,
    # )

    # zones = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=[('','All'),] + [(zone.id, zone) for zone in Zone.objects.all()],
    #     required=False,
    # )
    
    documents = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[('','All')] + [(doc.id, doc) for doc in ReportsMaster.objects.all()],
        required=False,
        
    )
    class Meta:
        model = RoleAssignment
        fields = ['distributors', 'zones', 'documents','iscreate','isview','isedit','search_text']
    

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id="search-form"
        self.helper.form_class = 'search-filter-form mb-4'
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'GET'
        self.helper.use_custom_control=True
        self.helper.label_class='font-weight-bold'
        
        self.helper.add_input(Submit('submit','Save', css_class='btn btn-wide btn-dark-custom mr-3'))
        self.helper.add_input(Reset('clear-search','Clear Filters', css_class='btn btn-wide btn-light'))
        
        self.helper.layout = Layout(
            Row(
                Column('distributors', css_class="distributor-checkboxes col-md-4 mb-0"),
                Column('zones', css_class="zone-checkboxes col-md-4 mb-0"),
                Column('documents', css_class ="doctype-checkboxes col-md-3 mb-0"),

               
            ),
            Row(
                Column("iscreate", css_class="checkbox-inline"),
                Column("isview", css_class="checkbox-inline"),
                Column("isedit", css_class="checkbox-inline")
            ),

            
        )
    



class SearchFilterUpdateForm(forms.ModelForm):
    """ Form For Advance Search of Quotes. """

    search_text = forms.CharField(
        widget=forms.TextInput,
        required=False
    )
    role = forms.ModelChoiceField(queryset=RoleMaster.objects.all())
    iscreate = forms.BooleanField(label="Can_Create")
    isedit = forms.BooleanField(label="Can_View")
    isview = forms.BooleanField(label="Can_Edit")
    
    # distributors = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=[('','All'),] + [(distributor.id, distributor.Distributor_Name) for distributor in Distributor.objects.all()],
    #     required=False,
    # )

    zones = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[('','All'),] + [(zone.name, zone) for zone in Zone.objects.all()],
        required=False,
    )
    
    documents = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[('','All')] + [(doc.Document_Type, doc) for doc in ReportsMaster.objects.all()],
        required=False,
        
        
    )
    class Meta:
        model = RoleAssignment
        fields = ['distributors', 'zones', 'documents','iscreate','isview','isedit','search_text']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id="search-form"
        self.helper.form_class = 'search-filter-form mb-4'
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'POST'
        self.helper.use_custom_control=True
        self.helper.label_class='font-weight-bold'
        self.helper.add_input(Submit('submit','Update', css_class='btn btn-wide btn-dark-custom mr-3'))
        self.helper.add_input(Reset('clear-search','Clear Filters', css_class='btn btn-wide btn-light'))
        self.helper.layout = Layout(
            Row(
                Column('distributors', css_class="distributor-checkboxes col-md-4 mb-0"),
                Column('zones', css_class="zone-checkboxes col-md-4 mb-0"),
                Column('Documents', css_class ="doctype-checkboxes col-md-3 mb-0"),             
            ),
            Row(
                Column("Can_Create", css_class="checkbox-inline"),
                Column("Can_View", css_class="checkbox-inline"),
                Column("Can_Edit", css_class="checkbox-inline")
            ),            
        )
        
        @transaction.atomic
        def save(self):
            roleassignupdate = super().save(commit=False)
            roleassignupdate.save()
            d1 = RoleAssignment.objects.create(distributors=roleassignupdate)
            d2 = RoleAssignment.objects.create(zones=roleassignupdate)
            d3 = RoleAssignment.objects.create(documents=roleassignupdate)
            roleassignupdate.d1
            roleassignupdate.d2
            roleassignupdate.d3
            roleassignupdate.save()
            
            
class itemstockform(forms.Form):  
    # def __init__(self, *args, **kwargs):
    #     super(itemstockform, self).__init__(*args, **kwargs)
    
    itemcode=forms.ModelChoiceField(queryset=Item.objects.all(), required=False)
    itemname=forms.CharField(max_length=50)
    date = forms.DateField(label='Date',required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    
    
    
from reportsapp.Choices import choice_chart_Type ,doc_choice
    
class dashboardchartForm(forms.Form):
    from_date = forms.DateField(label='From Date',required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    to_date = forms.DateField(label='To Date',required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    chart_type=forms.ChoiceField(choices=choice_chart_Type, label="Select Chart Type")
    document_type=forms.ChoiceField(choices=doc_choice,label="Select Document Type")
    
    

        
               