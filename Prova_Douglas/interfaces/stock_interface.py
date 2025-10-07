from abc import ABC, abstractmethod
from typing import List, Dict, Any


class IStockValidationStrategy(ABC):
    """
    Interface para estratégias de validação de estoque.
    """
    
    @abstractmethod
    def validate_stock(self, items: List[Dict[str, Any]]) -> bool:
        """
        Valida se há estoque suficiente para os itens.
        
        Args:
            items: Lista de itens do pedido
            
        Returns:
            True se há estoque suficiente, False caso contrário
        """
        pass
    
    @abstractmethod
    def get_available_quantity(self, product_name: str) -> int:
        """
        Retorna a quantidade disponível de um produto.
        
        Args:
            product_name: Nome do produto
            
        Returns:
            Quantidade disponível em estoque
        """
        pass
    
    @abstractmethod
    def get_stock_source(self) -> str:
        """
        Retorna a fonte do estoque.
        
        Returns:
            String identificando a fonte do estoque
        """
        pass


