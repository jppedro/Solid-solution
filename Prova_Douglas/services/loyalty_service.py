# services/loyalty_service.py

from models.order import Order
from models.customer import Customer
from models.enums import CustomerType

class LoyaltyService:
    
    def register_points_for_order(self, order: Order):
        customer_name = order.customer.name
        if order.customer.customer_type == CustomerType.VIP:
            points = int(order.total_price * 2)  # VIP ganha 2x pontos
            print(f"Cliente VIP {customer_name} ganhou {points} pontos!")
        else:
            points = int(order.total_price)  # Cliente normal ganha 1x pontos
            print(f"Cliente {customer_name} ganhou {points} pontos!")