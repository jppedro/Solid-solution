from abc import ABC, abstractmethod
from typing import Optional, List
from models.order import Order
from models.customer import Customer
from models.enums import OrderStatus


class IOrderRepository(ABC):
    @abstractmethod
    def add(self, order: Order) -> int:
        pass
    
    @abstractmethod
    def get_by_id(self, order_id: int) -> Optional[Order]:
        pass
    
    @abstractmethod
    def update_status(self, order_id: int, status: OrderStatus) -> bool:
        pass
    
    @abstractmethod
    def get_all_by_customer(self, customer_name: str) -> List[Order]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Order]:
        pass
    
    @abstractmethod
    def get_distinct_customers(self) -> List[Customer]:
        pass
    
    @abstractmethod
    def calculate_customer_total(self, customer_name: str) -> float:
        pass
