from abc import ABC, abstractmethod
from models.order import Order
from models.enums import PaymentMethod


class IPaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, order: Order, amount: float) -> bool:
        pass
    
    @abstractmethod
    def get_payment_method(self) -> PaymentMethod:
        pass
    
    @abstractmethod
    def requires_approval(self) -> bool:
        pass
