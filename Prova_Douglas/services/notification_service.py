# services/notification_service.py

from models.order import Order
from models.enums import OrderStatus

class NotificationService:
    """
    Serviço com a responsabilidade ÚNICA de enviar notificações.
    Segue o princípio SRP - responsabilidade única para envio de notificações.
    """
    
    def send_notification(self, order: Order, status: OrderStatus):
        """
        Envia notificações baseadas no status do pedido.
        Replica a lógica original da prova_douglas.py.
        """
        customer_name = order.customer.name
        
        if status == OrderStatus.PENDING:
            print(f"Email enviado para {customer_name}: Pedido recebido!")
            if order.is_special:
                print(f"Email especial enviado para {customer_name}: Pedido especial recebido!")
        elif status == OrderStatus.APPROVED:
            print(f"Email enviado para {customer_name}: Pedido aprovado!")
            print(f"SMS enviado para {customer_name}: Pedido aprovado!")
        elif status == OrderStatus.SHIPPED:
            print(f"Email enviado para {customer_name}: Pedido enviado!")
        elif status == OrderStatus.DELIVERED:
            print(f"Email enviado para {customer_name}: Pedido entregue!")


