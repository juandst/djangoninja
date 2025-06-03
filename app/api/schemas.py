from ninja import ModelSchema
from .models import Product

class ProductSchema(ModelSchema):
    class Meta:
        model = Product
        fields = ('id','name','description','price','stock','tags','created_at', 'updated_at', 'active')

class ProductSchemaCreate(ModelSchema):
    class Meta:
        model = Product
        fields = ('name','description','price','stock','tags')