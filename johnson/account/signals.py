from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import *
from reportsapp.models import *
from django.db.models import Sum
from django.db.models import DecimalField, IntegerField, ExpressionWrapper, Max , Sum , F
from django.db.models.functions import Coalesce        
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import redirect

from django.dispatch import Signal

# Define a custom signal
message_sent = Signal()

@receiver(post_save, sender=stockstatement)
def update_itemwise_closing(sender, instance, created, **kwargs):
    if created:
        warehouse=instance.w_house
        print(warehouse.id)
        item = instance.itm
        doc_type = instance.document_type
        qty = instance.Qty
        print(warehouse)
        print(warehouse.id)
        print(item)
        print(doc_type)
        print(qty)
        if doc_type == "Material Receipt Note":
            # if warehouse and item objects both are match query then data filter and add Qty
            try:
                stocks_summary = stockSummary.objects.filter(item=item.id, warehouse=warehouse.id).get()
                stocks_summary.Mrn_Qty +=qty
                stocks_summary.warehouse=warehouse.id
                stocks_summary.closing_balance =stocks_summary.OP + stocks_summary.Mrn_Qty+stocks_summary.sale_return_qty-stocks_summary.delivery_note_qty-stocks_summary.purchase_return_qty
                stocks_summary.save()
                    

                # If the object does not exist, create a new one with the provided stocksummary Object and quantity    
            except ObjectDoesNotExist:
                stock_summary = stockSummary.objects.create(warehouse=warehouse.id, 
                                              w_code=warehouse.wname,
                                              item=item.id, 
                                              itm_code=item.Item_Code,
                                              Mrn_Qty=qty, 
                                                )
                stock_summary.closing_balance = stock_summary.OP + stock_summary.Mrn_Qty + stock_summary.sale_return_qty - stock_summary.delivery_note_qty - stock_summary.purchase_return_qty
                stock_summary.save()
                
        elif doc_type == "Purchase Return":
            try:
                p_stock_obj = stockSummary.objects.filter(item=item.id, warehouse=warehouse.id).get()
                p_stock_obj.purchase_return_qty +=qty
                p_stock_obj.closing_balance=p_stock_obj.OP + p_stock_obj.Mrn_Qty+p_stock_obj.sale_return_qty-p_stock_obj.delivery_note_qty-p_stock_obj.purchase_return_qty
                p_stock_obj.save()
            except ObjectDoesNotExist:
                pr_stock_obj = stockSummary.objects.create(
                    warehouse=warehouse.id,
                    w_code = warehouse.wname,
                    item = item.id,
                    itm_code = item.Item_Name,
                    purchase_return_qty=qty,
                )
                pr_stock_obj.closing_balance=pr_stock_obj.OP + pr_stock_obj.Mrn_Qty + pr_stock_obj.sale_return_qty - pr_stock_obj.delivery_note_qty - pr_stock_obj.purchase_return_qty
                pr_stock_obj.save()
                    
        elif doc_type == "Delivery Note":
            try:
                d_stock_obj = stockSummary.objects.filter(item=item.id, warehouse=warehouse.id).get()
                d_stock_obj.delivery_note_qty +=qty
                d_stock_obj.closing_balance=d_stock_obj.OP + d_stock_obj.Mrn_Qty + d_stock_obj.sale_return_qty - d_stock_obj.delivery_note_qty - d_stock_obj.purchase_return_qty                   
                d_stock_obj.save()
            
            except ObjectDoesNotExist:
                    d_stocksummary = stockSummary.objects.create(
                        warehouse=warehouse.id,
                        w_code=warehouse.wname,
                        item=item.id,
                        itm_code = item.Item_Name,
                        delivery_note_qty=qty
                    )
                    
                    d_stocksummary.closing_balance =d_stocksummary.OP + d_stocksummary.Mrn_Qty + d_stocksummary.sale_return_qty - d_stocksummary.delivery_note_qty - d_stocksummary.purchase_return_qty
                    d_stocksummary.save()
                    
        elif doc_type == "Sales Return":
            try:
                s_stock_obj = stockSummary.objects.filter(item=item.id, warehouse=warehouse.id).get()
                s_stock_obj.sale_return_qty +=qty
                s_stock_obj.closing_balance=s_stock_obj.OP + s_stock_obj.Mrn_Qty + s_stock_obj.sale_return_qty - s_stock_obj.delivery_note_qty - s_stock_obj.purchase_return_qty   
                s_stock_obj.save()
            
            except ObjectDoesNotExist:
                s_stocksummary = stockSummary.objects.create(
                    warehouse=warehouse.id,
                    w_code=warehouse.wname,
                    item=item.id,
                    itm_code = item.Item_Name,
                    sale_return_qty=qty
                )
                s_stocksummary.closing_balance =s_stocksummary.OP + s_stocksummary.Mrn_Qty + s_stocksummary.sale_return_qty - s_stocksummary.delivery_note_qty - s_stocksummary.purchase_return_qty
                s_stocksummary.save()   
                  
        elif doc_type == "Opening Balance":
            try:
                o_stock_obj = stockSummary.objects.filter(item=item.id, warehouse=warehouse.id).get()
                if o_stock_obj:
                    pass
                
            except ObjectDoesNotExist:
                o_stock_object=stockSummary.objects.create(
                    warehouse=warehouse.id,
                    w_code=warehouse.wname,
                    item=item.id,
                    itm_code = item.Item_Name,
                    OP=qty,
                    closing_balance=qty
                    
                )    
                o_stock_object.save()
                              
                            
                      
                
                    
            
    
            
