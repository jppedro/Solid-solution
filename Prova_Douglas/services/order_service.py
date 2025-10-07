# services/order_service.py (CORRIGIDO E ATUALIZADO)

from datetime import datetime
from typing import List
from models.customer import Customer
from models.order import Order
from models.order_item import OrderItem
from interfaces.repository_interface import IOrderRepository
from services.notification_service import NotificationService
from services.loyalty_service import LoyaltyService
from services.inventory_service import InventoryService
from interfaces.discount_interface import IDiscountStrategy, ICustomerDiscountStrategy, ISpecialOrderFeeStrategy
from models.enums import OrderStatus
import random

class OrderService:
    
    def __init__(
        self,
        order_repository: IOrderRepository,
        notification_service: NotificationService,
        loyalty_service: LoyaltyService,
        inventory_service: InventoryService,
        discount_strategy: IDiscountStrategy,
        customer_discount_strategy: ICustomerDiscountStrategy,
        special_fee_strategy: ISpecialOrderFeeStrategy
    ):
        self._order_repository = order_repository
        self._notification_service = notification_service
        self._loyalty_service = loyalty_service
        self._inventory_service = inventory_service
        self._discount_strategy = discount_strategy
        self._customer_discount_strategy = customer_discount_strategy
        self._special_fee_strategy = special_fee_strategy

    def create_order(self, customer: Customer, items: List[OrderItem], is_special: bool = False) -> int:
        # A validação de estoque agora é delegada a outro serviço (DIP)
        if not self._inventory_service.is_stock_sufficient(items):
            raise ValueError("Estoque insuficiente para um ou mais itens.")

        # Lógica de cálculo de total usando strategies
        total = self._discount_strategy.calculate_discount(items)
        total = self._customer_discount_strategy.apply_customer_discount(total, customer)
        total = self._special_fee_strategy.apply_special_fee(total, is_special)

        order = Order(
            id=random.randint(1, 1000000), 
            customer=customer, 
            items=items,
            total_price=total, 
            status=OrderStatus.PENDING,
            created_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            is_special=is_special
        )
        
        order_id = self._order_repository.add(order)
        order.id = order_id
        
        self._notification_service.send_notification(order, OrderStatus.PENDING)
        
        return order_id

    def update_order_status(self, order_id: int, new_status: OrderStatus):
        order = self._order_repository.get_by_id(order_id)
        if order:
            self._order_repository.update_status(order_id, new_status)
            self._notification_service.send_notification(order, new_status)
            
            # Orquestra a chamada para o serviço de pontos (SRP)
            if new_status == OrderStatus.DELIVERED:
                self._loyalty_service.register_points_for_order(order)
        else:
            print(f"Pedido com ID {order_id} não encontrado.")

