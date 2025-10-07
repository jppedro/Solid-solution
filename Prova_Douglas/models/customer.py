from dataclasses import dataclass
from .enums import CustomerType

@dataclass
class Customer:
    """Representa um cliente do sistema."""
    name: str
    customer_type: CustomerType