from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.reports_list, name="report_list"),
    path('Secondary_Sale/', views.secondary_sale, name='secondary_sale'),
    path('search_report/', views.search_report, name='search_report'),
    path('ajax/load-fields/', views.load_fields, name='ajax_load_fields'),
    path('ajax/load/document_field/', views.load_document_fields, name='load_document_fields'),
    path(r'^export/reports/$', views.export_sales_to_xlsx, name='export_reports_data'),
    path(r'dashboard/$', views.dashboard, name='dashboard'),
    path(r'Menu/',views.dynamicmenu, name="menu_list"),
    path('menumaster/', views.menumaster, name='menu_master'),
    path('menumaster1/', views.menumaster1, name='menu_master1'),
    path('menumaster/checkbox/', views.checkbox, name='checkbox'),
    path('role_assignment/', views.role_assignment_create, name='role_assignment'),
    path('load_ajax_role_role/',views.RoleAssignUser, name="load_ajax_role"),
    path('load_ajax_role_user/',views.AssignUser, name="load_ajax_user"),
    path('role_assignment/filtet', views.RoleAssignmentFilter, name="roleAssignment_filter"),
    path('role_assignment_update/<int:pk>/', views.roleassignment_update, name='roleassignment_update'),
    path('base1/', views.base1 ,name='base1'),
    
    
    
    re_path(r'^searchReport/$', views.searchReport, name='search_report'),
    re_path(r'^load_date_fields/$', views.load_date_fields, name='load_date_fields'),
    re_path(r'^transaction/$', views.transaction, name='transaction'),
    re_path(r'^client_data/$', views.clientData, name='client_data'),
    re_path(r'^stock_statement/$', views.closingbalanceReport, name="closingbalanceReport"),
    re_path(r'^saleDashboard/$', views.saleDashboard, name='saleDashboard'),
    re_path(r'^itemwiseStock/$', views.itemwiseStock, name='itemwiseStock'),
    
    re_path(r'^load_itemname_stock/$', views.load_itemname_stock, name='load_itemname_stock'),
    re_path(r'load_stock_wiseitem/$', views.load_stock_wiseitem, name='load_stock_wiseitem'),
    re_path(r'load_warehousewise_item/$', views.load_warehousewise_item, name='load_warehousewise_item'),
    
    re_path('^dashboardChart/$', views.dashboardChart, name='dashboardChart'),
    path('stocksummaryReport/', views.stocksummaryReport, name='stocksummaryReport'),





]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
