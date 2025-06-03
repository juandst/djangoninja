import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...models import User, Product, Order, OrderItem
from .products import SeedProducts

class Command(BaseCommand):
    help = 'Seed database'

    def handle(self, *args, **kwargs):
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username='admin', password='admin')

        products = SeedProducts.PRODUCTS

        # create products & re-fetch from DB
        Product.objects.bulk_create(products)
        products = Product.objects.all()


        # create some dummy orders tied to the superuser
        for _ in range(3):
            # create an Order with 2 order items
            order = Order.objects.create(user=user)
            for product in random.sample(list(products), 2):
                OrderItem.objects.create(
                    order=order, product=product, quantity=random.randint(1,3)
                )