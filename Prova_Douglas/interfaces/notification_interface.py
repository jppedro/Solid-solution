from abc import ABC, abstractmethod
from models.order import Order
from models.enums import OrderStatus


class INotificationStrategy(ABC):
    """
    Interface para estratégias de notificação.
    Segue o princípio SRP - responsabilidade única para envio de notificações.
    """
    
    @abstractmethod
    def send_notification(self, order: Order, status: OrderStatus) -> bool:
        """
        Envia notificação para o cliente baseada no status do pedido.
        
        Args:
            order: Pedido relacionado à notificação
            status: Status atual do pedido
            
        Returns:
            True se a notificação foi enviada com sucesso, False caso contrário
        """
        pass
    
    @abstractmethod
    def get_notification_method(self) -> str:
        """
        Retorna o método de notificação.
        
        Returns:
            String identificando o método de notificação
        """
        pass


