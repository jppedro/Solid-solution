from interfaces.notification_interface import INotificationStrategy
from models.order import Order
from models.enums import OrderStatus


class EmailNotificationStrategy(INotificationStrategy):
    """
    Estratégia para envio de notificações por email.
    Baseada na funcionalidade original: print(f"Email enviado para {n}: ...")
    """
    
    def send_notification(self, order: Order, status: OrderStatus) -> bool:
        """
        Envia notificação por email baseada no status do pedido.
        Replica a funcionalidade original usando print.
        """
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
        """Retorna a mensagem apropriada baseada no status."""
        messages = {
            OrderStatus.PENDING: "Pedido recebido!",
            OrderStatus.APPROVED: "Pedido aprovado!",
            OrderStatus.SHIPPED: "Pedido enviado!",
            OrderStatus.DELIVERED: "Pedido entregue!"
        }
        return messages.get(status, "Status atualizado!")


class SMSNotificationStrategy(INotificationStrategy):
    """
    Estratégia para envio de notificações por SMS.
    Baseada na funcionalidade original: print(f"SMS enviado para {p['cli']}: ...")
    """
    
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
    """
    Estratégia para envio de notificações push.
    Exemplo de extensibilidade - nova strategy sem modificar código existente.
    """
    
    def send_notification(self, order: Order, status: OrderStatus) -> bool:
        """
        Envia notificação push baseada no status do pedido.
        Nova funcionalidade que pode ser adicionada sem modificar código existente.
        """
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
    """
    Estratégia para envio de notificações por WhatsApp.
    Exemplo de extensibilidade - nova strategy sem modificar código existente.
    """
    
    def send_notification(self, order: Order, status: OrderStatus) -> bool:
        """
        Envia notificação por WhatsApp baseada no status do pedido.
        Nova funcionalidade que pode ser adicionada sem modificar código existente.
        """
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
