from abc import ABC, abstractmethod


class IPointsStrategy(ABC):
    """
    Interface para estratégias de sistema de pontos.
    """
    
    @abstractmethod
    def calculate_points(self, order_total: float) -> int:
        """
        Calcula pontos baseado no total do pedido.
        
        Args:
            order_total: Valor total do pedido
            
        Returns:
            Número de pontos calculados
        """
        pass
    
    @abstractmethod
    def get_points_multiplier(self) -> float:
        """
        Retorna o multiplicador de pontos.
        
        Returns:
            Multiplicador de pontos
        """
        pass
    
    @abstractmethod
    def get_customer_type(self) -> str:
        """
        Retorna o tipo de cliente.
        
        Returns:
            String identificando o tipo de cliente
        """
        pass


