from abc import ABC, abstractmethod
from typing import Optional, List
from models.order import Order
from models.customer import Customer
from models.enums import OrderStatus


class IOrderRepository(ABC):
    """
    Interface para repositório de pedidos.
    Segue o princípio DIP - dependa de abstrações, não de implementações concretas.
    Segue o princípio SRP - responsabilidade única para persistência de pedidos.
    """
    
    @abstractmethod
    def add(self, order: Order) -> int:
        """
        Salva um novo pedido no banco de dados
        
        Args:
            order: Pedido a ser salvo
            
        Returns:
            ID do pedido criado
        """
        pass
    
    @abstractmethod
    def get_by_id(self, order_id: int) -> Optional[Order]:
        """
        Busca um pedido pelo ID
        
        Args:
            order_id: ID do pedido
            
        Returns:
            Pedido encontrado ou None se não encontrado
        """
        pass
    
    @abstractmethod
    def update_status(self, order_id: int, status: OrderStatus) -> bool:
        """
        Atualiza o status de um pedido
        
        Args:
            order_id: ID do pedido
            status: Novo status
            
        Returns:
            True se atualizado com sucesso, False caso contrário
        """
        pass
    
    @abstractmethod
    def get_all_by_customer(self, customer_name: str) -> List[Order]:
        """
        Busca todos os pedidos de um cliente
        
        Args:
            customer_name: Nome do cliente
            
        Returns:
            Lista de pedidos do cliente
        """
        pass
    
    @abstractmethod
    def get_all(self) -> List[Order]:
        """
        Busca todos os pedidos
        
        Returns:
            Lista com todos os pedidos
        """
        pass
    
    @abstractmethod
    def get_distinct_customers(self) -> List[Customer]:
        """
        Busca todos os clientes únicos
        
        Returns:
            Lista de clientes únicos
        """
        pass
    
    @abstractmethod
    def calculate_customer_total(self, customer_name: str) -> float:
        """
        Calcula o total gasto por um cliente
        
        Args:
            customer_name: Nome do cliente
            
        Returns:
            Total gasto pelo cliente
        """
        pass
