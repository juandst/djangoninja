import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel

class User(AbstractUser):
    pass

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    tags = models.CharField(max_length=255)

    @property
    def in_stock(self):
        return self.stock > 0
    
    def __str__(self):
        return self.name
    
class Order(BaseModel):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    status = models.CharField(max_length=10, choices=StatusChoices.choices)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    products = models.ManyToManyField(Product, through="OrderItem", related_name='orders')

    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def item_subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in order {self.order.order_id}"