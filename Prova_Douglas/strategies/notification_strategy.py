from interfaces.notification_interface import INotificationStrategy
from models.order import Order
from models.enums import OrderStatus


class EmailNotificationStrategy(INotificationStrategy):
    
    def send_notification(self, order: Order, status: OrderStatus) -> bool:
        customer_name = order.customer.name
        message = self._get_message_by_status(status)
        
        print(f"Email enviado para {customer_name}: {message}")
        
        # Para pedidos especiais, envia email especial também
        if hasattr(order, 'is_special') and order.is_special and status == OrderStatus.PENDING:
            print(f"Email especial enviado para {customer_name}: Pedido especial recebido!")
        
        return True
    
    def get_notification_method(self) -> str:
        return "email"
    
    def _get_message_by_status(self, status: OrderStatus) -> str:
        messages = {
            OrderStatus.PENDING: "Pedido recebido!",
            OrderStatus.APPROVED: "Pedido aprovado!",
            OrderStatus.SHIPPED: "Pedido enviado!",
            OrderStatus.DELIVERED: "Pedido entregue!"
        }
        return messages.get(status, "Status atualizado!")


class SMSNotificationStrategy(INotificationStrategy):
    def send_notification(self, order: Order, status: OrderStatus) -> bool:
        """
        Envia notificação por SMS baseada no status do pedido.
        Replica a funcionalidade original usando print.
        """
        customer_name = order.customer.name
        message = self._get_message_by_status(status)
        
        # SMS é enviado apenas para pedidos aprovados (como na prova original)
        if status == OrderStatus.APPROVED:
            print(f"SMS enviado para {customer_name}: {message}")
        
        return True
    
    def get_notification_method(self) -> str:
        return "sms"
    
    def _get_message_by_status(self, status: OrderStatus) -> str:
        """Retorna a mensagem apropriada baseada no status."""
        messages = {
            OrderStatus.PENDING: "Pedido recebido!",
            OrderStatus.APPROVED: "Pedido aprovado!",
            OrderStatus.SHIPPED: "Pedido enviado!",
            OrderStatus.DELIVERED: "Pedido entregue!"
        }
        return messages.get(status, "Status atualizado!")


class PushNotificationStrategy(INotificationStrategy):
    def send_notification(self, order: Order, status: OrderStatus) -> bool:
        customer_name = order.customer.name
        message = self._get_message_by_status(status)
        
        print(f"Push notification enviada para {customer_name}: {message}")
        return True
    
    def get_notification_method(self) -> str:
        return "push"
    
    def _get_message_by_status(self, status: OrderStatus) -> str:
        """Retorna a mensagem apropriada baseada no status."""
        messages = {
            OrderStatus.PENDING: "Pedido recebido!",
            OrderStatus.APPROVED: "Pedido aprovado!",
            OrderStatus.SHIPPED: "Pedido enviado!",
            OrderStatus.DELIVERED: "Pedido entregue!"
        }
        return messages.get(status, "Status atualizado!")


class WhatsAppNotificationStrategy(INotificationStrategy):
    def send_notification(self, order: Order, status: OrderStatus) -> bool:
        customer_name = order.customer.name
        message = self._get_message_by_status(status)
        
        print(f"WhatsApp enviado para {customer_name}: {message}")
        return True
    
    def get_notification_method(self) -> str:
        return "whatsapp"
    
    def _get_message_by_status(self, status: OrderStatus) -> str:
        """Retorna a mensagem apropriada baseada no status."""
        messages = {
            OrderStatus.PENDING: "Pedido recebido!",
            OrderStatus.APPROVED: "Pedido aprovado!",
            OrderStatus.SHIPPED: "Pedido enviado!",
            OrderStatus.DELIVERED: "Pedido entregue!"
        }
        return messages.get(status, "Status atualizado!")
