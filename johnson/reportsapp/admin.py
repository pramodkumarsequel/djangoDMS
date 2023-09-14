from django.contrib import admin
from .models import ReportsMaster, FieldMaster, MenuMaster,RoleAssignment
from import_export.admin import ImportExportModelAdmin


@admin.register(RoleAssignment)
class RoleAssignmentAdmin(admin.ModelAdmin):
    list_display = ['id','EID','UID','ROLEID','fld1','fld2','rolename','documenttype','iscreate','isview','isedit','created_on']
# Register your models here.
# @admin.register(Fieldmaster)
# class FieldMasterAdmin(admin.ModelAdmin):
#     list_display = ['sales']

# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ('distributors','start_date',)

@admin.register(ReportsMaster)
class DocumentMasterAdmin(admin.ModelAdmin):
    list_display = ['id','Document_Type','fields','value','Date_Type','From_Date','To_Date',]


@admin.register(FieldMaster)
class DocumentMasterAdmin(admin.ModelAdmin):
    list_display = ['DocType','Field_Name',]
    
    
@admin.register(MenuMaster)
class MenuMasterAdmin(ImportExportModelAdmin):
    list_display = ['id','MenuName','Pmenu','pagelink','Dord','Image','Roles','IsMobile','MTYPE','Is_View','Is_Create','is_Edit','is_Delete','created_at','updated_at']    
    
    
from reportsapp.models import stockstatement
@admin.register(stockstatement)
class stockstatementadmin(ImportExportModelAdmin):
    list_display = ['document_type','docid','doc_date','warehouse_id','w_house','warehouse_name','items','itm','item_name','Qty','uom','amount']    