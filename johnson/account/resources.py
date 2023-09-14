from import_export import resources
from .models import Distributor, Sales_Detail

class MamberResource(resources.ModelResource):
    class Meta:
        model = Distributor




class SaleDetailResource(resources.ModelResource):
    class Meta:
        model = Sales_Detail
