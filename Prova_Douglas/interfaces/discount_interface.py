from abc import ABC, abstractmethod
from typing import List
from models.order_item import OrderItem
from models.customer import Customer
from models.enums import CustomerType


class IDiscountStrategy(ABC):
    """
    Interface para estratégias de desconto de itens.
    Segue o princípio SRP - responsabilidade única para cálculo de descontos.
    """
    
    @abstractmethod
    def calculate_discount(self, items: List[OrderItem]) -> float:
        """
        Calcula o desconto aplicado aos itens do pedido.
        
        Args:
            items: Lista de itens do pedido
            
        Returns:
            Valor total após aplicação dos descontos dos itens
        """
        pass
    
    @abstractmethod
    def get_discount_type(self) -> str:
        """
        Retorna o tipo de desconto.
        
        Returns:
            String identificando o tipo de desconto
        """
        pass


class ICustomerDiscountStrategy(ABC):
    """
    Interface para estratégias de desconto por tipo de cliente.
    Segue o princípio SRP - responsabilidade única para descontos de cliente.
    """
    
    @abstractmethod
    def apply_customer_discount(self, total: float, customer: Customer) -> float:
        """
        Aplica desconto baseado no tipo de cliente.
        
        Args:
            total: Valor total do pedido
            customer: Cliente do pedido
            
        Returns:
            Valor final após aplicação do desconto do cliente
        """
        pass
    
    @abstractmethod
    def get_customer_type(self) -> CustomerType:
        """
        Retorna o tipo de cliente suportado.
        
        Returns:
            CustomerType suportado por esta strategy
        """
        pass


class ISpecialOrderFeeStrategy(ABC):
    """
    Interface para estratégias de taxa de pedidos especiais.
    Segue o princípio SRP - responsabilidade única para taxas especiais.
    """
    
    @abstractmethod
    def apply_special_fee(self, total: float, is_special: bool) -> float:
        """
        Aplica taxa especial se o pedido for especial.
        
        Args:
            total: Valor total do pedido
            is_special: Se o pedido é especial
            
        Returns:
            Valor final após aplicação da taxa especial
        """
        pass