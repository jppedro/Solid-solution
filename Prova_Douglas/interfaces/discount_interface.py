from abc import ABC, abstractmethod
from typing import List
from models.order_item import OrderItem
from models.customer import Customer
from models.enums import CustomerType


class IDiscountStrategy(ABC):
    
    @abstractmethod
    def calculate_discount(self, items: List[OrderItem]) -> float:
        pass
    
    @abstractmethod
    def get_discount_type(self) -> str:
        pass


class ICustomerDiscountStrategy(ABC):
    @abstractmethod
    def apply_customer_discount(self, total: float, customer: Customer) -> float:
        pass
    
    @abstractmethod
    def get_customer_type(self) -> CustomerType:
        pass


class ISpecialOrderFeeStrategy(ABC):
    
    @abstractmethod
    def apply_special_fee(self, total: float, is_special: bool) -> float:
        pass