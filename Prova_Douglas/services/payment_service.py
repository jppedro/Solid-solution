# services/payment_service.py

from typing import Dict, Optional
from models.order import Order
from strategies.payment_strategy import IPaymentStrategy
from services.order_service import OrderService
from interfaces.repository_interface import IOrderRepository
from models.enums import OrderStatus, PaymentMethod

class PaymentService:
    def __init__(
        self,
        payment_strategies: Dict[PaymentMethod, IPaymentStrategy],
        order_repository: IOrderRepository,
        order_service: OrderService
    ):
        self._strategies = payment_strategies
        self._order_repo = order_repository  
        self._order_service = order_service

    def _get_and_validate_order(self, order_id: int, amount_paid: float) -> Optional[Order]:
        """
        Método auxiliar para encapsular a busca do pedido e validações básicas.
        Isso melhora o SRP (Responsabilidade Única) do método principal 'process_payment'.
        """
        order = self._order_repo.get_by_id(order_id)
        
        if not order:
            print("Pedido não encontrado!")
            return None
        
        if amount_paid < order.total_price:
            print("Valor pago é insuficiente!")
            return None
            
        return order

    def process_payment(self, order_id: int, method: PaymentMethod, amount_paid: float) -> bool:
        """
        Coordena o processo de pagamento.
        """
        
        order = self._get_and_validate_order(order_id, amount_paid)
        if not order:
            return False

        strategy = self._strategies.get(method)
        if not strategy:
            print("Método de pagamento inválido!")
            return False
            
        payment_approved = strategy.process_payment(order, amount_paid)
        
        if payment_approved:
            self._order_service.update_order_status(order_id, OrderStatus.APPROVED)
            
        return True