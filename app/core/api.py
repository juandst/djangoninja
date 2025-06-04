from ninja import NinjaAPI
from api.router import router
from ninja.security import django_auth

# V1
api_v1 = NinjaAPI(auth=django_auth, version='1.0.0')

api_v1.add_router("/products/", router)