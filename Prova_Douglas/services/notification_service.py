# services/notification_service.py

from models.order import Order
from models.enums import OrderStatus

class NotificationService:
    
    def send_notification(self, order: Order, status: OrderStatus):
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


