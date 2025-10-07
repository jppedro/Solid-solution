from dataclasses import dataclass
from .enums import CustomerType

@dataclass
class Customer:
    name: str
    customer_type: CustomerType