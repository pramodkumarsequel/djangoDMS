from django.urls import path, include, re_path
from . import views

urlpatterns = [
    # path('home/', views.index, name='home'),
    # path('home1/', views.index1, name="home1"),
    path('/user/profile/', views.profile, name="user_profile"),
    path('', views.Login, name='login'),
    path(r'password_change/<token>/', views.password_change, name="password_change"),
    path('generate_link/$', views.password_reset, name='password_reset'),
    path('userlogout/', views.user_logout, name='user_logout'),
    re_path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

    re_path(r'^upload/$', views.upload_detailsale, name='upload_detailsale'),
    re_path(r'export/customer/', views.export_customer_excel, name='export_customer_excel'),
    re_path(r'^user_import_excel/', views.import_data, name='user_import_excel'),
    re_path(r'export/user', views.export_user_excel, name='export_user_excel'),
    re_path(r'export/distributor', views.export_distributor_excel, name='export_distributor_excel'),
    re_path(r'export/item/', views.export_item_excel, name='export_item_excel'),
    re_path(r'export/hierarchy/', views.export_hierarchy1_excel, name='export_hierarchy1_excel'),
    re_path(r'^export/h2/csv', views.export_hierarchy2_excel, name='export_h2_data'),
    re_path(r'export/h3/csv/', views.export_hierarchy3_excel, name='export_h3_data'),
    re_path(r'^export/h4/csv/', views.export_hierarchy4_excel, name='export_csv_data'),
    re_path(r'^export/h5/excel/', views.export_hierarchy5_excel, name='export_data'),
    re_path(r'^export/dbprice/', views.export_dbpricemaster_excel, name='export_db_data'),
    re_path(r'^export/role/', views.export_role_excel, name='export_role_data'),
    re_path(r'^export/zone/', views.export_zone_excel, name='export_zone_data'),
    re_path(r'export/tax/', views.export_tax_excel, name='export_tax_data'),
    re_path('export/uom/', views.export_uom_excel, name="export_uom_data"),
    re_path('export/region/', views.export_region_excel, name="export_region_data"),
    re_path('export/state/', views.export_state_excel, name="export_state_data"),
    re_path('export/city/', views.export_city_excel, name="export_city_data"),

    re_path(r'^ajax/load-disname/$', views.load_disname, name='ajax_load_disname'),
    re_path(r'^ajax/load-itemname/$', views.load_Sales_Item_Name, name='ajax_load_itemname'),
    path(r'password_policy/$', views.password_policy, name='password-policy'),
    path(r'stock/', views.stocklist, name='stock_list'),
        
    re_path(r'^load_zone/search/$', views.dependantfield,name='load_state'),
    re_path(r'^retailer/$', views.dependantfield),
    re_path(r'^load_regions/$', views.load_regions,name='load_region'),
    re_path(r'load_dis_region/$', views.load_distributor_regions,name="load_dis_region"),
    re_path(r'^load_state/$', views.load_states,name='load_state'),

    
    re_path(r'^load_uom/$', views.load_sale_uom,name='load_uom'),
    re_path(r'^load_base_uom/$', views.load_base_uom,name='load_base_uom'),
    re_path(r'load_hierarchy2/$', views.load_hierachy, name="load_hier2_ajax"),
    re_path(r'load_hierarchy5/$', views.load_hierarchy4, name="load_hier4_ajax"),
    re_path(r'^load_hierarchy4_ajax/$', views.load_hierarchy4_ajax, name='load_hierarchy4_ajax'),
    #re_path(r'load_hierarchy3/$',views.load_hierarchy3, name="load_hier3_ajax"),
    re_path(r'load_ajax_hierarchy3/$',views.load_hier3, name="load_hierarchy3_ajax"),
    re_path(r'^load_order_date/$', views.load_order_id, name='load_order_date'),
    re_path(r'^mrn_vendor_load/$', views.mrn_vendor_load, name='mrn_vendor_load'),
    re_path(r'load_mrn_date/$', views.load_mrn_no, name="load_mrn_date"),
    re_path(r'^load_mrn_object/$', views.load_mrn_object, name='load_mrn_object'),
    re_path(r'^load_hier5/$', views.load_hier5, name="load_hier5"),
    re_path(r'^load_pidate/$', views.load_pidate, name="load_pidate"),
    re_path(r'load_vendor_pr/$', views.load_vendor_pr, name='load_vendor_pr'),
    re_path(r'^load_popup/$',views.load_popup, name="load_popup"),
    re_path(r'^load_gst/$',views.load_gst, name="load_gst"),
    re_path(r'^load_MRN_field/',views.load_MRN_field, name="load_MRN_field"),
    re_path(r'^load_gst_field/$', views.load_gst_field, name="load_gst_field"),
    re_path(r'^load_line_item/$', views.load_line_item, name="load_line_item"),
    re_path(r'^get_item_code/$', views.get_item_code, name='get_item_code'),
    re_path(r'^load_piorder_id/$', views.load_piorder_id, name="load_piorder_id"),
    re_path(r'^load_pi_date/$', views.load_pi_date, name="load_pi_date"),
    re_path(r'^load_dis_field/$', views.load_dis_field, name='load_dis_field'),
    re_path(r'^load_gst_type/$', views.load_gst_type, name='load_gst_type'),
    re_path(r'^load_item_drop/$', views.load_item_drop, name='load_item_drop'),
    re_path(r'^pur_line_items/$', views.pur_line_items,name='pur_line_items'),
    re_path(r'^load_full_item/$', views.load_full_item, name="load_full_item"),
    re_path(r'^load_data_sorder_wise/$',views.load_data_sorder_wise, name='load_data_sorder_wise'),
    re_path(r'^/get_pur_order_id/$', views.get_pur_order_id, name='get_pur_order_id'),


#     path('<url_set>', views.dynamic_generate_url),


##########################################################################################

    
    re_path(r'^user-list/', views.userList, name="user-list"),
    re_path(r'^user-create/$',views.userCreate, name="user-create"),
    re_path(r'^user/update/(?P<pk>\d+)/$', views.userUpdate, name="user-update"),
    re_path(r'^user/delete/(?P<pk>\d+)/$', views.userDelete, name="user-delete"),
    
    
    re_path(r'^retailer-list/$', views.customerList, name='customer-list'),
    re_path(r'^retailer-create/$', views.customerCreate, name='customer-create'),
    re_path(r'^retailer/update/(?P<pk>\d+)/$', views.customerUpdate, name="customer-update"),
    re_path(r'^retailer-delete/(?P<pk>\d+)/delete/$', views.customerDelete, name="customer-delete"),

    re_path(r'^distributor-list/$', views.distributorList, name="distributor-list"),  
    re_path(r'^distributor-create/$', views.distributorCreate, name="distributor-create"), 
    re_path(r'^distributor-update/update/(?P<pk>\d+)/$', views.distributorUpdate, name="distributor-update"), 
    re_path(r'^distributor-delete/delete/(?P<pk>\d+)/$', views.distributorDelete, name="distributor-delete"),
    
    
    re_path(r'^item-list/$', views.itemList, name='item-list'),
    re_path(r'^item-create/$', views.itemCreate, name='item-create'),
    re_path(r'^item-update/update/(?P<pk>\d+)/$', views.itemUpdate, name='item-update'),
    re_path(r'^item-delete/delete/(?P<pk>\d+)/$', views.itemDelete, name='item-delete'),
    
    
    
    re_path(r'^hierarchy1-list/$', views.hierarchy1List, name='hierarchy1-list'),
    re_path(r'^hierarchy1-create/$', views.hierarchy1Create, name='hierarchy1-create'),
    re_path(r'^hierarchy1-update/update/(?P<pk>\d+)/$', views.hierarchy1Update, name='hierarchy1-update'),
    re_path(r'^hierarchy1-delete/delete/(?P<pk>\d+)/$', views.hierarchy1Delete, name='hierarchy1-delete'),
    
    re_path(r'^hierarchy2-list/$', views.hierarchy2List, name='hierarchy2-list'),
    re_path(r'^hierarchy2-create/$', views.hierarchy2Create, name='hierarchy2-create'),
    re_path(r'^hierarchy2-update/update/(?P<pk>\d+)/$', views.hierarchy2Update, name='hierarchy2-update'),
    re_path(r'^hierarchy2-delete/delete/(?P<pk>\d+)/$', views.hierarchy2Delete, name='hierarchy2-delete'),
    
    re_path(r'^hierarchy3-list/$', views.hierarchy3List, name='hierarchy3-list'),
    re_path(r'^hierarchy3-create/$', views.hierarchy3Create, name='hierarchy3-create'),
    re_path(r'^hierarchy3-update/update/(?P<pk>\d+)/$', views.hierarchy3Update, name='hierarchy3-update'),
    re_path(r'^hierarchy3-delete/delete/(?P<pk>\d+)/$', views.hierarchy3Delete, name='hierarchy3-delete'),
    
    re_path(r'^hierarchy4-list/$', views.hierarchy4List, name='hierarchy4-list'),
    re_path(r'^hierarchy4-create/$', views.hierarchy4Create, name='hierarchy4-create'),
    re_path(r'^hierarchy4-update/update/(?P<pk>\d+)/$', views.hierarchy4Update, name='hierarchy4-update'),
    re_path(r'^hierarchy4-delete/delete/(?P<pk>\d+)/$', views.hierarchy4Delete, name='hierarchy4-delete'),
    
    re_path(r'^hierarchy5-list/$', views.hierarchy5List, name='hierarchy5-list'),
    re_path(r'^hierarchy5-create/$', views.hierarchy5Create, name='hierarchy5-create'),
    re_path(r'^hierarchy5-update/update/(?P<pk>\d+)/$', views.hierarchy5Update, name='hierarchy5-update'),
    re_path(r'^hierarchy5-delete/delete/(?P<pk>\d+)/$', views.hierarchy5Delete, name='hierarchy5-delete'),
    
    re_path(r'^zone-list/$', views.zoneList, name='zone-list'),
    re_path(r'^zone-create/$', views.zoneCreate, name='zone-create'),
    re_path(r'^zone-update/update/(?P<pk>\d+)/$', views.zoneUpdate, name='zone-update'),
    re_path(r'^zone-delete/delete/(?P<pk>\d+)/$', views.zoneDelete, name='zone-delete'),
    
    re_path(r'^region-list/$', views.regionList, name='region-list'),
    re_path(r'^region-create/$', views.regionCreate, name='region-create'),
    re_path(r'^region-update/update/(?P<pk>\d+)/$', views.regionUpdate, name='region-update'),
    re_path(r'^region-delete/delete/(?P<pk>\d+)/$', views.regionDelete, name='region-delete'),
    
    re_path(r'^state-list/$', views.stateList, name='state-list'),
    re_path(r'^state-create/$', views.stateCreate, name='state-create'),
    re_path(r'^state-update/update/(?P<pk>\d+)/$', views.stateUpdate, name='state-update'),
    re_path(r'^state-delete/delete/(?P<pk>\d+)/$', views.stateDelete, name='state-delete'),
    
    
    re_path(r'^city-list/$', views.cityList, name='city-list'),
    re_path(r'^city-create/$', views.cityCreate, name='city-create'),
    re_path(r'^city-update/update/(?P<pk>\d+)/$', views.cityUpdate, name='city-update'),
    re_path(r'^city-delete/delete/(?P<pk>\d+)/$', views.cityDelete, name='city-delete'),
    
    re_path(r'^uom-list/$', views.uomList, name='uom-list'),
    re_path(r'^uom-create/$', views.uomCreate, name='uom-create'),
    re_path(r'^uom-update/update/(?P<pk>\d+)/$', views.uomUpdate, name='uom-update'),
    re_path(r'^uom-delete/delete/(?P<pk>\d+)/$', views.uomDelete, name='uom-delete'),
    
    re_path(r'^tax-list/$', views.taxList, name='tax-list'),
    re_path(r'^tax-create/$', views.taxCreate, name='tax-create'),
    re_path(r'^tax-update/update/(?P<pk>\d+)/$', views.taxUpdate, name='tax-update'),
    re_path(r'^tax-delete/delete/(?P<pk>\d+)/$', views.taxDelete, name='tax-delete'),
    
    re_path(r'^dbprice-list/$', views.dbpriceList, name='dbprice-list'),
    re_path(r'^dbprice-create/$', views.dbpriceCreate, name='dbprice-create'),
    re_path(r'^dbprice-update/update/(?P<pk>\d+)/$', views.dbpriceUpdate, name='dbprice-update'),
    re_path(r'^dbprice-delete/delete/(?P<pk>\d+)/$', views.dbpriceDelete, name='dbprice-delete'),
    
    re_path(r'^warehouse-list/$', views.warehouseList, name='warehouse-list'),
    re_path(r'^warehouse-create/$', views.warehouseCreate, name='warehouse-create'),
    re_path(r'^warehouse-update/update/(?P<pk>\d+)/$', views.warehouseUpdate, name='warehouse-update'),
    re_path(r'^warehouse-delete/delete/(?P<pk>\d+)/$', views.warehouseDelete, name='warehouse-delete'),
    
    re_path(r'^warehouseopeningstock-create/$', views.warehouseOpeningStock, name="wlineitem_create"),
    
    re_path(r'^purchase-create/$',views.purchaselineitemCreate, name="purchase-create"),
    re_path(r'^receiptnote-create/$', views.receiptynoteCreate, name='receiptnote-create'),
    re_path(r'^purchase-return-create/$', views.purchasereturnlineitemCreate, name="purchasereturn-create"),
    re_path(r'^purchaseinvoice-create/$', views.purchaseinvoiceCreate, name='purchaseinvoice-create'),
    
    re_path(r'^saleCreate/$', views.saleCreate, name="sale-create"),
    re_path(r'^deliverynote-create/$', views.deliverynoteCreate, name='deliverynote-create'),
    re_path(r'^sales-invoice-create/$', views.saleseinvoiceCreate, name='saleinvoice-create'),
    re_path(r'^salereturn-create/$', views.salereturnCreate, name='salereturn-create'),
    
   
    
    re_path(r'^number-series-generate/$', views.ordergenerateCreate, name='order-generate'),
    re_path(r'^number-series-update/(?P<pk>\d+)/$', views.ordergenerateUpdate, name='orderno-update'),
    
    re_path(r'^role-list/$', views.roleList, name='role-list'),
    re_path(r'^role-create/$', views.roleCreate, name='role-create'),
    re_path(r'^role-update/update/(?P<pk>\d+)/$', views.roleUpdate, name='role-update'),
    re_path(r'^role-delete/delete/(?P<pk>\d+)/$', views.roleDelete, name='role-delete'),
    
    re_path(r'^permission-list/$', views.permissionList, name="permission-list"),
    re_path(r'^permission-update/$', views.permissionUpdate, name="permission-update"),
    

#All ajax request here with poup data as per select dorpdown
    re_path(r'load_ajax_gsttype_data/$',views.get_cgst_sgst_amount, name="ajax_load_cgst_sgst"),
    re_path(r'load_ajax_wh_id/$',views.load_warehouseName, name="load_whname"),
    re_path(r'load_ajax_custname/$',views.load_customer, name="ajax_load_custname"),    
    re_path(r'load_model_fields/$', views.get_model_fields, name='get_model_fields'), 
    re_path(r'load_fields/$', views.get_fields, name='get_fields'), 
    re_path(r'^load_sodate/$', views.load_so_date, name="load_sodate"), 
    re_path(r'load_di_date/$', views.load_di_date,name="load_di_date"), 
    re_path(r'^load_si_date/$', views.load_si_date, name="load_si_date"), 
    re_path(r'^load_sales_line_items/$', views.load_sales_line_items, name='load_sales_line_items'),
    re_path(r'^load_all_items/$', views.load_all_items, name='load_all_items'),
    re_path(r'^sale_cust_dropdown/$', views.sale_cust_dropdown, name="sale_cust_dropdown"),
    re_path(r'^sale_gst_dropdown/$', views.sale_gst_dropdown, name='sale_gst_dropdown'),
    re_path(r'^load_dl_note_data/$', views.load_dl_note_data, name='load_dl_note_data'),
    re_path(r'^load_del_items/$', views.load_del_items, name="load_del_items"),
    re_path(r'^load_si_items/$', views.load_si_items, name='load_si_items'),
    re_path(r'^load_dl_gst_dropdown/$', views.load_dl_gst_dropdown, name="load_dl_gst_dropdown"),
    re_path(r'^load_dl_cust_dropdown/$', views.load_dl_cust_dropdown, name='load_dl_cust_dropdown'),
    re_path(r'^load_dl_so_dropdown/$', views.load_dl_so_dropdown, name='load_dl_so_dropdown'),
    re_path(r'^load_si_data/$', views.load_si_data, name='load_si_data'),
    re_path(r'^load_si_dropdown_item/$', views.load_si_dropdown_item, name='load_si_dropdown_item'),
    re_path(r'^item_data_dropdown/$', views.item_data_dropdown, name="item_data_dropdown"),
    re_path(r'^load_si_gst/$', views.load_si_gst, name='load_si_gst'),
    re_path(r'^load_cust_code/$', views.load_cust_code, name='load_cust_code'),
    re_path(r'^load_item_d/$', views.load_item_d, name='load_item_d'),
    re_path(r'^load_puchase_order_item/$', views.load_puchase_order_item, name='load_puchase_order_item'),
    re_path(r'^base_unit_class/$', views.base_unit_class, name='base_unit_class'),
    re_path(r'purchase_unit_class/$', views.purchase_unit_class, name='purchase_unit_class'),
    #re_path(r'^load_p_uom_data/$', views.load_p_uom_data, name='load_p_uom_data'),
    re_path(r'^zone_toggle_active/$', views.zone_toggle_active, name='zone_toggle_active'),
    re_path(r'^region_toggle_active/$', views.region_toggle_active, name='region_toggle_active'),
    re_path(r'^state_toggle_active/$', views.state_toggle_active, name='state_toggle_active'),
    re_path(r'^city_toggle_active/$', views.city_toggle_active, name='city_toggle_active'),
    re_path(r'^user_toggle_active/$', views.user_toggle_active, name='user_toggle_active'),
    re_path(r'^hier1_toggle_active/$', views.hier1_toggle_active, name='hier1_toggle_active'),
    re_path(r'^hier2_toggle_active/$', views.hier2_toggle_active, name='hier2_toggle_active'),
    re_path(r'^hier3_toggle_active/$', views.hier3_toggle_active, name='hier3_toggle_active'),
    re_path(r'^hier4_toggle_active/$', views.hier4_toggle_active, name='hier4_toggle_active'),
    re_path(r'^hier5_toggle_active/$', views.hier5_toggle_active, name='hier5_toggle_active'),
    re_path(r'^customer_toggle_active/$', views.customer_toggle_active, name='customer_toggle_active'),
    re_path(r'^distributor_toggle_active/$', views.distributor_toggle_active,name='distributor_toggle_active'),
    re_path(r'^uom_toggle_active/$', views.uom_toggle_active, name='uom_toggle_active'),
    re_path(r'^tax_toggle_active/$', views.tax_toggle_active, name='tax_toggle_active'),
    re_path(r'^dbprice_toggle_active/$', views.dbprice_toggle_active, name='dbprice_toggle_active'),
    re_path(r'^warehouse_toggle_active/$', views.warehouse_toggle_active, name='warehouse_toggle_active'),
    re_path(r'^item_toggle_active/$', views.item_toggle_active,name='item_toggle_active'),
    
    # path('export_sales_data/', views.export_sales_data, name='export_sales_data'),
    path('export_sales_data/', views.export_sales_data, name='export_sales_data'),
    

]
