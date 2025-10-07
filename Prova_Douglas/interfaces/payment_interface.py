from abc import ABC, abstractmethod
from models.order import Order
from models.enums import PaymentMethod


class IPaymentStrategy(ABC):
    """
    Interface para estratégias de pagamento.
    Segue o princípio SRP - responsabilidade única para processamento de pagamentos.
    """
    
    @abstractmethod
    def process_payment(self, order: Order, amount: float) -> bool:
        """
        Processa o pagamento do pedido.
        
        Args:
            order: Pedido a ser pago
            amount: Valor a ser pago
            
        Returns:
            True se o pagamento foi processado com sucesso, False caso contrário
        """
        pass
    
    @abstractmethod
    def get_payment_method(self) -> PaymentMethod:
        """
        Retorna o método de pagamento.
        
        Returns:
            PaymentMethod suportado por esta strategy
        """
        pass
    
    @abstractmethod
    def requires_approval(self) -> bool:
        """
        Indica se o método de pagamento requer aprovação automática.
        
        Returns:
            True se requer aprovação automática, False caso contrário
        """
        pass
