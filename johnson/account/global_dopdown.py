from account.models import PurchaseDocument, Distributor, TaxMaster, DetailOfPurchase, Item, Receipt_Note,Receipt_Note_Detail,PurchaseInvoice,PurchaseinvoicelineItem,Sales, Delivery_Note, Delivery_Note_Details,Sales_Detail, salesInvoice,saleinvoicelineItem
from datetime import datetime  
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format 
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

import json
from decimal import Decimal

from datetime import datetime  
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format 

#Does quasi the same things as json.loads from here: https://pypi.org/project/dynamodb-json/
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


def load_MRN_field(request):
    orderid = request.GET.get('orderid')
    try:
        order_obj = PurchaseDocument.objects.get(id=orderid)    
        disid = order_obj.Distributors.id
        disobj = Distributor.objects.filter(id=disid)
        context = {
            'orders':disobj
        }
        return render(request, 'account/Receiptnote/dis_dropdown.html', context)
    
    except ValueError:
        context = {
            'orders':None
        }
        return render(request, 'account/Receiptnote/dis_dropdown.html', context)
     

def load_gst_field(request): 
    orderid = request.GET.get('orderid') 
    try:
        order_obj = PurchaseDocument.objects.get(id=orderid)
        gstid = order_obj.gst_type.id  
        taxobjs = TaxMaster.objects.filter(id=gstid)
        context = {
            'taxobjs':taxobjs
        }
        return render(request, 'account/Receiptnote/gst_dropdown.html', context)
    
    except ValueError:
        context = {
             'taxobjs':None
        }
        return render(request, 'account/Receiptnote/gst_dropdown.html', context)
    

def load_order_id(request):
    try:
        orderid = request.GET.get('orderid')
        orderdate = PurchaseDocument.objects.get(id=orderid) 
        ordis = orderdate.Distributors.Distributor_Name
        dt = orderdate.Bill_Date
        df=DateFormat(dt)
        odate = df.format('Y-m-d')
        context = {
            'ordis':ordis,
            'odate':odate,
            
        }
        return HttpResponse(json.dumps(context,cls=JSONEncoder), content_type="application/json")   
    except ValueError:
        context = {
            '':''
        }
        return HttpResponse(json.dumps(context,cls=JSONEncoder), content_type="application/json") 


def mrn_vendor_load(request):
    mrn_obj = request.GET.get('orderid')
    try:
        p_object = PurchaseDocument.objects.filter(id=mrn_obj)
        context = {
            'p_order':p_object
        }
        return render(request, 'account/Receiptnote/vendor_dropdown.html', context)
    
    except ValueError:
        context = {
            'p_order':''
        }
        return render(request, 'account/Receiptnote/vendor_dropdown.html', context)
    
        
##################### line item dropdown ##########

def load_line_item_purchase(request):
    try:      
        orderid = request.GET.get('orderid' or None)
        p_id = PurchaseDocument.objects.get(id=orderid)
        obj=DetailOfPurchase.objects.filter(entity_id=p_id.id)
        context = {
            'obj':obj
        }
        return render(request, 'account/Receiptnote/lineitem_dropdown.html', context)
    except ValueError:
        context = {
            'obj':None
        }
        return render(request, 'account/Receiptnote/lineitem_dropdown.html', context)
        
    

# PurchaseInvoice
    
def load_piorder_id(request):
    orderid = request.GET.get('orderid')
    orderdate = PurchaseDocument.objects.get(id=orderid) 
    mrn_no = Receipt_Note.objects.filter(p_order_no_id=orderdate).order_by('p_order_no')
    return render(request, 'account/Purchaseinvoice/mrn_dropdown.html',{'mrn':mrn_no})

           

def load_pi_date(request):
    orderid = request.GET.get('orderid')
    orderdate = PurchaseDocument.objects.get(id=orderid) 
    d = orderdate.Bill_Date
    dformmat = DateFormat(d)
    final_date = dformmat.format('Y-m-d')
    context = {
        'final_date':final_date,
    }
    return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")


def load_dis_field(request):
    orderid = request.GET.get('orderid')
    order_obj = Receipt_Note.objects.get(id=orderid)
    disid = order_obj.Distributors.id
    disobj = Distributor.objects.filter(id=disid)
    context = {
        'orders':disobj
    }
    return render(request, 'account/Purchaseinvoice/dis_dropdown.html', context)

def load_gst_type(request):
    orderid = request.GET.get('orderid')
    order_obj = Receipt_Note.objects.get(id=orderid)
    disid = order_obj.gst_type.id
    disobj = TaxMaster.objects.filter(id=disid)
    context = {
        'gsttype':disobj
    }
    return render(request, 'account/Purchaseinvoice/gst_dropdown.html', context)
    
def load_mrn_no(request):
    mrnid=request.GET.get('mrnid')
    mrn_object = Receipt_Note.objects.get(id=mrnid)
    #bill_ent = mrn_object.billing_entity
    dis_code = mrn_object.Distributors.Distributor_Code
    dis_name=mrn_object.Distributor_Name
    sup_no = mrn_object.Invoice_No
    sup_date = mrn_object.supplier_invoice_date
    dt = mrn_object.receipt_note_date
    gtype = mrn_object.gst_type.name
    t_inv = mrn_object.Total_Inventory_Amount
    tgst = mrn_object.Total_GST
    msgst=mrn_object.SGST_AMOUNT
    mcgst=mrn_object.CGST_AMOUNT
    mcdis = mrn_object.Cash_Discount_Amount
    mtamount = mrn_object.Total_Amount
    sdate = DateFormat(sup_date)
    spdate = sdate.format('Y-m-d')
    df=DateFormat(dt)
    mrndate = df.format('Y-m-d')
    
    context = {
        #'bill_ent':bill_ent,
        'dis_code':dis_code,
        'dis_name':dis_name,
        'sup_no':sup_no,
        'sup_date':spdate,
        'gtype':gtype,
        't_inv':t_inv,
        'tgst':tgst,
        'msgst':msgst,
        'mcgst':mcgst,
        'mcdis':mcdis,
        'mtamount':mtamount,
        'mrndate':mrndate,
    }
    return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")


def load_mrn_object(request):
    try:
        mrnid=request.GET.get('mrn_id')
        mrns = Receipt_Note.objects.filter(id=mrnid)
        context = {
            'mrns':mrns,
        }
        return render(request,'account/Purchaseinvoice/vendor_dropdown.html', context)
    
    except ValueError:
        mrns=None
        context = {
            'mrns':'',
        }
        return render(request,'account/Purchaseinvoice/vendor_dropdown.html', context)


def load_item_drop(request):
    try:
        orderid = request.GET.get('orderid')
        itm_id = Receipt_Note.objects.get(id=orderid)
        itms = Receipt_Note_Detail.objects.filter(entity_id=itm_id.id)
        context = {
            'items':itms
        }
        return render(request, 'account/Purchaseinvoice/itm_dropdown.html', context)
    
    except ValueError:
        items=None
        return render(request, 'account/Purchaseinvoice/itm_dropdown.html', context)
        

def load_vendor_pr(request):
    pr_id = request.GET.get('pid')
    try:
        obj = PurchaseInvoice.objects.filter(id=pr_id)
        context = {
            'obj':obj
        }
        return render(request, 'account/Purchasereturn/vendor_dropdown.html',context)
    
    except ValueError:
        context = {
            'obj':''
        }
        return render(request, 'account/Purchasereturn/vendor_dropdown.html',context)
 


def load_popup(request):
    pid=request.GET.get('pid')
    pidate_object = PurchaseInvoice.objects.get(id=pid)
    disid = pidate_object.Distributors.id
    gsttax = pidate_object.gst_type.id
    gsttype=TaxMaster.objects.filter(id=gsttax)
    dis = Distributor.objects.filter(id=disid)
    context = {
        'dis':dis,
    }
    return render(request, 'account/Purchasereturn/dropdown_fields.html', context)


def load_gst(request):
    pid=request.GET.get('pid')
    pidate_object = PurchaseInvoice.objects.get(id=pid)
    gsttax = pidate_object.gst_type.id
    gsttype=TaxMaster.objects.filter(id=gsttax)
    context = {
        'gsttype':gsttype,
        
    }
    return render(request, 'account/Purchasereturn/gst_dropdown.html', context)


def pur_line_items(request):
    try:
        pid = request.GET.get('pid')
        p_inv = PurchaseInvoice.objects.get(id=pid)
        child_itm = PurchaseinvoicelineItem.objects.filter(parent_id=p_inv.id)
        context = {
            'itms':child_itm,
        }
        return render(request, 'account/Purchasereturn/item_dropdown.html', context)
    
    except Exception as e:
        context = {
            'itms':'',
        }
        return render(request, 'account/Purchasereturn/item_dropdown.html', context)

        


def load_full_item(request):
    try:
        items = request.GET.get('items')
        pid = request.GET.get('pid')
        child_itm = PurchaseinvoicelineItem.objects.filter(parent_id=pid).filter(items=items)
        for itm in child_itm:
            itmname = itm.item_name
            qyn = itm.PI_QTY
            rate = itm.Rate
            uom = itm.UOM
            dis = itm.Discount
            ser = itm.Serial_No
            tamunt=itm.Total_Amount
            
        context = {
            'itmname':itmname,
            'qyn':qyn,
            'rate':rate,
            'uom':uom,
            'dis':dis,
            'ser':ser,
            'tamunt':tamunt
            
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")

    except Exception as e:
        context = {
            'itmname':None,
            'qyn':None,
            'rate':None,
            'uom':None,
            'dis':None,
            'ser':None,
            'tamunt':None
            
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")

def load_data_sorder_wise(request):
    try:
        s_inv_id = request.GET.get('soid')
        s_inv = Sales.objects.get(id=s_inv_id)
        cust_code = s_inv.Customers.Customer_Code
        cust_name = s_inv.Customer_Name
        bill_date=s_inv.Bill_Date
        cust_po_no = s_inv.cust_po_no
        cust_po_date = s_inv.cust_po_date
        tgst=  s_inv.Total_GST
        inv_amount = s_inv.Total_Inventory_Amount
        sgst_amunt = s_inv.SGST_AMOUNT
        cgst_amunt = s_inv.CGST_AMOUNT
        c_dis = s_inv.Cash_Discount_Amount
        inv_mount = s_inv.Total_Invoice_Amount
        bill_date = DateFormat(bill_date)
        bill_date = bill_date.format('Y-m-d')
        cust_date = DateFormat(cust_po_date)
        cust_date = cust_date.format('Y-m-d')
        total_invent = s_inv.Total_Inventory_Amount
        
        
        
        context = {
            'cust_code':cust_code,
            'cust_name':cust_name,
            'bill_date':bill_date,
            'cust_po_no':cust_po_no,
            'cust_po_date':cust_date,
            'inv_no':inv_amount,
            'sgst_amunt':sgst_amunt,
            'cgst_amunt':cgst_amunt,
            'tgst':tgst,
            'c_dis':c_dis,
            'total_invent':total_invent,
            'inv_mount':inv_mount,        
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")
    
    except ValueError:
        s_inv_id=None
        context = {
            '':None
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")
        
        
        
     
from django.http import Http404
     
def load_sales_line_items(request):
    try:     
        order_id = request.GET.get('soid')
        sale_id = Sales.objects.get(id=order_id)
        sale_child_id = Sales_Detail.objects.filter(entity_id=sale_id.id)
        context = {
            'custs':sale_child_id
        }
        return render(request, 'account/Deliverynote/item_dropdown.html', context)
    except ValueError:
        context = {
            'custs':None
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")
        #return render(request, 'account/Deliverynote/item_dropdown.html', context)
  
            



def load_all_items(request):
    try:
        order_id = request.GET.get('soid')
        items = Item.objects.get(id=order_id)
        order2_id = request.GET.get('order_id')
        sale_child_id = Sales_Detail.objects.filter(entity_id=order2_id).filter(Sales_Item_Code_id=items)
        for itm_child in sale_child_id:
            sale_itm_nm = itm_child.Sales_Item_Name
            sale_qyn = itm_child.bal_qty
            sale_um = itm_child.sale_uom
            sale_rate=itm_child.Sales_Rate
            sale_serial=itm_child.Sales_Serial_No
            sale_dis = itm_child.Sales_Discount
            sale_total = itm_child.Total_Amount
            
        context = {
            'sale_itm_nm':sale_itm_nm,
            'sale_qyn':sale_qyn,
            'sale_um':sale_um,
            'sale_rate':sale_rate,
            'sale_serial':sale_serial,
            'sale_dis':sale_dis,
            'sale_total':sale_total,
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")
    except ValueError:
        context ={
            'order_id': None
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")

        
        
        

# def load_all_items(request):
#     sale_itm_nm  =None
#     sale_qyn=None
#     sale_um=None
#     sale_rate=None
#     sale_serial=None
#     sale_dis=None
#     sale_total=None
#     order_id = request.GET.get('soid')
#     print(order_id)
#     sale_id = Item.objects.get(id=order_id)
#     sale_child_id = Sales_Detail.objects.filter(Sales_Item_Code_id=sale_id.id)
#     for itm_child in sale_child_id:
#         sale_itm_nm = itm_child.Sales_Item_Name
#         sale_qyn = itm_child.Sales_Quantity
#         sale_um = itm_child.sale_uom
#         sale_rate=itm_child.Sales_Rate
#         sale_serial=itm_child.Sales_Serial_No
#         sale_dis = itm_child.Sales_Discount
#         sale_total = itm_child.Total_Amount
        
#     context = {
#         'sale_itm_nm':sale_itm_nm,
#         'sale_qyn':sale_qyn,
#         'sale_um':sale_um,
#         'sale_rate':sale_rate,
#         'sale_serial':sale_serial,
#         'sale_dis':sale_dis,
#         'sale_total':sale_total,
#     }
#     return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")


def sale_cust_dropdown(request):
    try:
        soid = request.GET.get('soid')
        cust_id = Sales.objects.filter(id=soid)
        context = {
            'cust_id':cust_id
        }
        return render(request, 'account/Deliverynote/cust_dropdown.html', context)
    except ValueError:
        context ={
            'cust_id':None
        }
        return render(request, 'account/Deliverynote/cust_dropdown.html', context)
        


def sale_gst_dropdown(request):
    try:   
        soid = request.GET.get('soid')
        sales = Sales.objects.filter(id=soid)
        context = {
            'gsts':sales
        }
        return render(request, 'account/Deliverynote/gst_dropdown.html', context)
    
    except ValueError:
        soid=None
        context = {
             'gsts':None
        }
        return render(request, 'account/Deliverynote/gst_dropdown.html', context)



# load delivery note data in sales Invoice 

def load_dl_note_data(request):
    try:
        dl_id=request.GET.get('dlid')
        itm = Delivery_Note.objects.get(id=dl_id)
        bill_date = itm.Bill_Date
        # bi = DateFormat(bill_date)
        # bi_format=bi.format('Y-m-d')
        total_inventory=itm.Total_Inventory_Amount
        sgst = itm.SGST_AMOUNT
        cgst = itm.CGST_AMOUNT
        total_gst=itm.Total_GST
        cash_dis = itm.Cash_Discount_Amount
        total_amount=itm.Total_Amount
        
        context = {
            # 'bill_date':bi_format,
            'total_inventory':total_inventory,
            'sgst':sgst,
            'cgst':cgst,
            'total_gst':total_gst,
            'cash_dis':cash_dis,
            'total_amount':total_amount,
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")

    except Exception as e:
        context = {
            'total_inventory':None,
            'sgst':None,
            'cgst':None,
            'total_gst':None,
            'cash_dis':None,
            'total_amount':None,
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")


def load_del_items(request):
    try:
        dl_id=request.GET.get('dlid')
        itm = Delivery_Note.objects.get(id=dl_id)
        dl_child_id = Delivery_Note_Details.objects.filter(entity_id=itm.id)
        context = {
            'items':dl_child_id
        }  
        return render(request, 'account/Saleinvoice/itm_dropdown.html', context)  
    
    except Exception as e:
        context = {
            'items': None
        }
        return render(request, 'account/Saleinvoice/itm_dropdown.html', context)  


def load_si_items(request):
    qyt=None
    rate=None
    discount=None
    srl=None
    amount=None
    uom=None
    try:
        dl_id=request.GET.get('dlid')
        delivery_order_id=request.GET.get('delivery_order')
        itm = Item.objects.get(id=dl_id)
        dl_child_obj = Delivery_Note_Details.objects.filter(entity_id=delivery_order_id).filter(items_id=itm.id)
        for dl in dl_child_obj:
            qyt = dl.DN_QTY
            rate=dl.Rate
            discount=dl.Discount
            srl=dl.Serial_No
            amount=dl.Amount 
            uom=dl.uom
            itm_name=dl.Item_Name
        context = {
            'qyt':qyt,
            'rate':rate,
            'discount':discount,
            'srl':srl,
            'amount':amount,
            'uom':uom,
            'itm_name':itm_name,
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")
    except ValueError:
        context = {
            'data':None
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")
        

def load_dl_gst_dropdown(request):
    try:
        dl_id = request.GET.get('dlid')
        dl_gst = Delivery_Note.objects.filter(id=dl_id)
        context = {
            'dl_gst':dl_gst
            
        }
        return render(request, 'account/Saleinvoice/gst_dropdown.html', context)
    
    except Exception as e:
        context = {
            'dl_gst':''
        }
        return render(request, 'account/Saleinvoice/gst_dropdown.html', context)


def load_dl_cust_dropdown(request):
    try:
        dl_id = request.GET.get('dlid')
        custs = Delivery_Note.objects.filter(id=dl_id)
        context = {
            'custs':custs
            
        }
        return render(request, 'account/Saleinvoice/cust_dropdown.html', context)
    
    except Exception as e:
        context = {
             'custs':''
        }
        return render(request, 'account/Saleinvoice/cust_dropdown.html', context)




def load_dl_so_dropdown(request):
    try:
        dl_id = request.GET.get('dlid')
        sorders = Delivery_Note.objects.filter(id=dl_id)
        context = {
            'sorders':sorders
            
        }
        return render(request, 'account/Saleinvoice/so_dropdown.html', context)
    
    except Exception as e:
        context = {
            'sorders':''
            
        }
        return render(request, 'account/Saleinvoice/so_dropdown.html', context)
        
        
    
def load_si_data(request):
    try:
        si_id = request.GET.get('si_id')
        si_id = salesInvoice.objects.get(id=si_id)
        sgst = si_id.SGST_AMOUNT
        cgst = si_id.CGST_AMOUNT
        t_gst = si_id.Total_GST
        cash_dis = si_id.Cash_Discount_Amount
        t_inventory = si_id.Total_Inventory_Amount
        t_invoice = si_id.Total_Invoice_Amount
        context = {
            'sgst':sgst,
            'cgst':cgst,
            't_gst':t_gst,
            'cash_dis':cash_dis,
            't_inventory':t_inventory,
            't_invoice':t_invoice
            
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")

    except Exception as e:
        context = {
            'sgst':sgst,
            'cgst':cgst,
            't_gst':t_gst,
            'cash_dis':cash_dis,
            't_inventory':t_inventory,
            't_invoice':t_invoice
            
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")


def load_si_dropdown_item(request):
    try:
        sale_inv = request.GET.get('si_id')
        child_sale_inv = saleinvoicelineItem.objects.filter(parent_id=sale_inv)
        context = {
            'itms':child_sale_inv
            }
        return render(request, 'account/Salereturn/itm_dropdown.html', context)    
    
    except Exception as esc:
        context = {
            'itms':''
        }
        return render(request, 'account/Salereturn/itm_dropdown.html', context)    

        

def item_data_dropdown(request):
    sale_inv = request.GET.get('si_id')
    sid=request.GET.get('sid')
    if sale_inv =='':
        context = {
            '':'',
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")
    sl_return_obj = saleinvoicelineItem.objects.filter(parent_id=sid).filter(Item_Code=sale_inv)
    itmname=None
    qyan=None
    uom=None
    rate=None
    srl=None
    dis=None
    amt=None
    for sale_obj in sl_return_obj:
        itmname=sale_obj.Item_Name
        qyan=sale_obj.SI_QTY
        uom=sale_obj.uom
        rate = sale_obj.Rate
        srl = sale_obj.Serial_No
        dis = sale_obj.Discount
        amt = sale_obj.Amount
    context = {
        'itmname':itmname,
        'qyan':qyan,
        'uom':uom,
        'rate':rate,
        'srl':srl,
        'dis':dis,
        'amt':amt,   
    }
    return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")



def load_si_gst(request):
    try:
        orderid = request.GET.get('si_id')
        gst_obj = salesInvoice.objects.filter(id=orderid)
        context = {
            'gst_obj':gst_obj,
        }
        return render(request, 'account/Salereturn/gst_dropdown.html', context)
    
    except Exception as e:
        context = {
            'gst_obj':'',
        }
        return render(request, 'account/Salereturn/gst_dropdown.html', context)
        

def load_cust_code(request):
    try:
        orderid = request.GET.get('si_id')
        cust_obj = salesInvoice.objects.filter(id=orderid)
        context = {
            'cust_obj':cust_obj
        }
        return render(request, 'account/Salereturn/cust_dropdown.html', context)    
    
    except Exception as e:
        context = {
            'cust_obj':''
        }
        return render(request, 'account/Salereturn/cust_dropdown.html', context)  
        





def load_itemname_stock(request):
    try:
        item_id=request.GET.get('items')
        items=Item.objects.get(id=item_id)
        context = {
            'item':items.Item_Name
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")
    
    except Exception as e:
        context = {
            'item':''
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")
        


from account.models import warehouseStock, Warehouse,warehouseItemChild

def load_stock_wiseitem(request):
    try:
        item_id=request.GET.get('items')
        items=Warehouse.objects.get(id=item_id)
        w_id = warehouseStock.objects.filter(warehouseCode_id=items.id)
        dm  = [d for f in list(w_id) for d in warehouseItemChild.objects.filter(warehouseID=f.id)[:1]]
        context = {
            'items':dm
        }
        return render(request, 'reportsapp/closingstock/item_dropdown.html', context)
    
    except Exception as e:
        context = {
            'items':dm
        }
        return render(request, 'reportsapp/closingstock/item_dropdown.html', context)
  

from django.db.models import Count
def load_warehousewise_item(request):
    try:
        w_id=request.GET.get('items')
        items=warehouseItemChild.objects.filter(w_house=w_id).annotate(distinct_w_house=Count('Item_Code')).filter(distinct_w_house=1)
        context = {
            'items':items
        }
        return render(request, 'reportsapp/stockSummary/item_dropdown.html', context)
    
    except Exception as e:
        context = {
            'items':''
        }
        return render(request, 'reportsapp/stockSummary/item_dropdown.html', context)
   
        

def get_item_code(request):
    try:
        orderid = request.GET.get('orderid')
        items = DetailOfPurchase.objects.filter(entity_id=orderid)
        context = {
            'items':items
        }
        return render(request, 'account/Receiptnote/itm_dropdown.html', context)
    
    except ValueError:
        items=None
        context = {
            'items':items
        }
        return render(request, 'account/Receiptnote/itm_dropdown.html', context)
        
        

def load_line_item(request):
    itmname=None
    qyan=None
    uom=None
    rate=None
    srl=None
    dis=None
    amt=None
    try:
        en_id = request.GET.get('orderid')
        items=request.GET.get('items')
        items_obj = Receipt_Note_Detail.objects.filter(entity_id=en_id).filter(items=items)
        for items in items_obj:
            itmname=items.Item_Name
            qyan=items.MRN_QTY
            uom=items.uom
            rate = items.Rate
            srl = items.Serial_No
            dis = items.Discount
            amt = items.Total_Amount
            
        context = {
            'itmname':itmname,
            'qyan':qyan,
            'uom':uom,
            'rate':rate,
            'srl':srl,
            'dis':dis,
            'amt':amt
            
        }    
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")

    except ValueError:      
        context = {
            'itmname':None,
            'qyan':None,
            'uom':None,
            'rate':None,
            'srl':None,
            'dis':None,
            'amt':None
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")

           

def load_item_d(request):
    try:
        item_id = request.GET.get('items')
        dms = Item.objects.filter(id=item_id)
        for d in dms:
            iname=d.Item_Name
            uom=d.purchase_uom.unit_name
            rate = d.purchase_price
            context = {
                'item_name':iname,
                'uom':uom,  
                'p_price':rate,   
            }
            return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")
    except ValueError:
        dms=None
        context = {
            '':''
        } 
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")  
    



def load_puchase_order_item(request):
    item=um=qty=rate=sr=dis=totl=None
    try:
        item_id = request.GET.get('items')
        purid=request.GET.get('purchase_order_id')
        purchase_order=DetailOfPurchase.objects.filter(entity_id=purid).filter(items=item_id)
        for itm in purchase_order:
            item=itm.item_name
            um=itm.purchase_uom
            qty=itm.bal_qty
            rate=itm.Purchase_Rate
            sr=itm.Purchases_Serial_No
            dis=itm.Purchase_Product_Discount
            totl=itm.Total_Amount
            
        context  = {
            'item':item,
            'um':um,
            'qty':qty,
            'rate':rate,
            'sr':sr,
            'dis':dis,
            'totl':totl,
        }    
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")
    
    except ValueError:
        context = {
            'd':''
        }
        return HttpResponse(json.dumps(context, cls=JSONEncoder), content_type="application/json")
    
    
from account.models import Unit, UOM 
def base_unit_class(request):
    base_unit_id = request.GET.get('base_unit_id')
    if not base_unit_id:
        context = {
        'un':None
        }
        return render(request, 'account/Item/sale_uom_dropdown.html', context)
    unt = UOM.objects.get(id=base_unit_id)
    un = Unit.objects.filter(id=unt.UNT_id)
    res=UOM.objects.filter(UNT_id__in=un)
    context = {
        'un':res
    }
    return render(request, 'account/Item/sale_uom_dropdown.html', context)


def purchase_unit_class(request):
    base_unit_id = request.GET.get('base_unit_id')
    if not base_unit_id:
        context = {
            'un':None
        }
        return render(request, 'account/Item/purchase_uom_dropdown.html', context)
    else:
        unt = UOM.objects.get(id=base_unit_id)
        un = Unit.objects.filter(id=unt.UNT_id)
        res=UOM.objects.filter(UNT_id__in=un)
        context = {
            'un':res
        }
        return render(request, 'account/Item/purchase_uom_dropdown.html', context)




from django.http import JsonResponse
from account.models import *

def zone_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    zone_obj = Zone.objects.get(id=r_id)
    if toggle_v == 'true':
        zone_obj.isactive=True
        zone_obj.save()
    if toggle_v == 'false':
        zone_obj.isactive=False  
        zone_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 


def region_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    region_obj = RegionMaster.objects.get(id=r_id)
    if toggle_v == 'true':
        region_obj.isactive=True
        region_obj.save()
    if toggle_v == 'false':
        region_obj.isactive=False  
        region_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 

def state_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    state_obj = StateMaster.objects.get(id=r_id)
    if toggle_v == 'true':
        state_obj.isactive=True
        state_obj.save()
    if toggle_v == 'false':
        state_obj.isactive=False  
        state_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 


def city_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    city_obj = CityMaster.objects.get(id=r_id)
    if toggle_v == 'true':
        city_obj.isactive=True
        city_obj.save()
    if toggle_v == 'false':
        city_obj.isactive=False  
        city_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 



def user_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    user_obj = User.objects.get(id=r_id)
    if toggle_v == 'true':
        user_obj.is_active=True
        user_obj.save()
    if toggle_v == 'false':
        user_obj.is_active=False  
        user_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 

def hier1_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    hier1_obj = Hierarchy1.objects.get(id=r_id)
    if toggle_v == 'true':
        hier1_obj.isactive=True
        hier1_obj.save()
    if toggle_v == 'false':
        hier1_obj.isactive=False  
        hier1_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 

def hier2_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    hier2_obj = Hierarchy2.objects.get(id=r_id)
    if toggle_v == 'true':
        hier2_obj.isactive=True
        hier2_obj.save()
    if toggle_v == 'false':
        hier2_obj.isactive=False  
        hier2_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 

def hier3_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    hier3_obj = Hierarchy3.objects.get(id=r_id)
    if toggle_v == 'true':
        hier3_obj.isactive=True
        hier3_obj.save()
    if toggle_v == 'false':
        hier3_obj.isactive=False  
        hier3_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 

def hier4_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    hier4_obj = Hierarchy4.objects.get(id=r_id)
    if toggle_v == 'true':
        hier4_obj.isactive=True
        hier4_obj.save()
    if toggle_v == 'false':
        hier4_obj.isactive=False  
        hier4_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 

def hier5_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    hier5_obj = Hierarchy5.objects.get(id=r_id)
    if toggle_v == 'true':
        hier5_obj.isactive=True
        hier5_obj.save()
    if toggle_v == 'false':
        hier5_obj.isactive=False  
        hier5_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 



def customer_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    customer_obj = Customer.objects.get(id=r_id)
    if toggle_v == 'true':
        customer_obj.isactive=True
        customer_obj.save()
    if toggle_v == 'false':
        customer_obj.isactive=False  
        customer_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 



def distributor_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    distributor_obj = Distributor.objects.get(id=r_id)
    if toggle_v == 'true':
        distributor_obj.isactive=True
        distributor_obj.save()
    if toggle_v == 'false':
        distributor_obj.isactive=False  
        distributor_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 


def uom_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    uom_obj = UOM.objects.get(id=r_id)
    if toggle_v == 'true':
        uom_obj.isactive=True
        uom_obj.save()
    if toggle_v == 'false':
        uom_obj.isactive=False  
        uom_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 


def tax_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    tax_obj = TaxMaster.objects.get(id=r_id)
    if toggle_v == 'true':
        tax_obj.isactive=True
        tax_obj.save()
    if toggle_v == 'false':
        tax_obj.isactive=False  
        tax_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 


def dbprice_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    dbprice_obj = DBPriceMaster.objects.get(id=r_id)
    if toggle_v == 'true':
        dbprice_obj.isactive=True
        dbprice_obj.save()
    if toggle_v == 'false':
        dbprice_obj.isactive=False  
        dbprice_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 


def warehouse_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    print(toggle_v)
    r_id=request.GET.get('row_id')
    warehouse_obj = Warehouse.objects.get(id=r_id)
    if toggle_v == 'true':
        warehouse_obj.isactive=True
        warehouse_obj.save()
    if toggle_v == 'false':
        warehouse_obj.isactive=False  
        warehouse_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 


def item_toggle_active(request):
    toggle_v=request.GET.get('toggle_value') 
    r_id=request.GET.get('row_id')
    item_obj = Item.objects.get(id=r_id)
    if toggle_v == 'true':
        item_obj.isactive=True
        item_obj.save()
    if toggle_v == 'false':
        item_obj.isactive=False  
        item_obj.save()
    return JsonResponse({'status': 'successfully Inactive'}) 




