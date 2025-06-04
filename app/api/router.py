from ninja import Router, Query
from ninja.pagination import paginate
from ninja.errors import HttpError
from .schemas import ProductSchema, ProductSchemaCreate
from .models import Product
from .filters import ProductFilterSchema

router = Router()

@router.get('/', response=list[ProductSchema], auth=None)
@paginate
async def get_products(request,  filters: ProductFilterSchema = Query(...)):
    qs = Product.objects.all()
    products = filters.filter(qs)
    
    return products

@router.get('/{product_id}', response=ProductSchema)
async def get_product_by_id(request, product_id: int):
    try:
        product = await Product.objects.aget(pk=product_id)
        return product
    except Product.DoesNotExist:
        raise HttpError(404, "Product not found")