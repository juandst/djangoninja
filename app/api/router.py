from ninja import Router
from asgiref.sync import sync_to_async

from .schemas import ProductSchema, ProductSchemaCreate
from .models import Product

router = Router()

@router.get('/', response=list[ProductSchema])
async def get_products(request):
    qs = Product.objects.all()
    products = await sync_to_async(list)(qs)

    return products