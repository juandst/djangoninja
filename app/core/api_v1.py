from ninja import NinjaAPI
from api.router import router

api = NinjaAPI(version='1.0.0')

api.add_router("/products/", router)