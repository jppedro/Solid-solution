from abc import ABC, abstractmethod
from models.order import Order
from models.enums import OrderStatus


class INotificationStrategy(ABC):
    
    @abstractmethod
    def send_notification(self, order: Order, status: OrderStatus) -> bool:
        pass
    
    @abstractmethod
    def get_notification_method(self) -> str:
        pass


