from dataclasses import dataclass
from .enums import ItemType

@dataclass
class OrderItem:
    name: str
    price: float
    quantity: int
    item_type: ItemType