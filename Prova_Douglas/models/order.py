from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from .customer import Customer
from .order_item import OrderItem
from .enums import OrderStatus

@dataclass
class Order:
    """Representa um pedido no sistema."""
    customer: Customer
    items: List[OrderItem]
    id: int = None
    total_price: float = 0.0
    status: OrderStatus = OrderStatus.PENDING
    created_at: str = field(default_factory=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    is_special: bool = False