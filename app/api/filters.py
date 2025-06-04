from decimal import Decimal
from ninja import FilterSchema, Field
from typing import Optional


class ProductFilterSchema(FilterSchema):
    name: Optional[str] = None
    name__icontains: Optional[str] = None
    price: Optional[Decimal] = None
    price__lt: Optional[Decimal] = None
    price__gte: Optional[Decimal] = None
    price__lte: Optional[Decimal] = None
    tags__icontains: Optional[str] = None
    stock: Optional[int] = None
    stock__lt: Optional[int] = None
    stock__gt: Optional[int] = None
    description__icontains: Optional[str] = None