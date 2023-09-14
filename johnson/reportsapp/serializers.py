from rest_framework import serializers
from .models import MenuMaster
from account.models import Sales


class MenuMasterSerializers(serializers.ModelSerializer):
    class Meta:
        model = MenuMaster
        fields = ['id','MenuName','Image','Dord','Is_View','Is_Create','is_Edit','is_Delete','usrole','pagelink']
        

class SubMasterSerializers(serializers.ModelSerializer):
    class Meta:
        model = MenuMaster
        fields = ['id','MenuName','pagelink','Pmenu','Dord','usrole']
        
        

class SaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'
