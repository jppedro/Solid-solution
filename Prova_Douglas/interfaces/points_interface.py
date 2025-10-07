from abc import ABC, abstractmethod


class IPointsStrategy(ABC):
    
    @abstractmethod
    def calculate_points(self, order_total: float) -> int:
        pass
    
    @abstractmethod
    def get_points_multiplier(self) -> float:
        pass
    
    @abstractmethod
    def get_customer_type(self) -> str:
        pass


