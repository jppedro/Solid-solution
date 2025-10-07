from dataclasses import dataclass
from .enums import ItemType

@dataclass
class OrderItem:
    """Representa um item dentro de um pedido."""
    name: str
    price: float
    quantity: int
    item_type: ItemType