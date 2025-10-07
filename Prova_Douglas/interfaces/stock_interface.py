from abc import ABC, abstractmethod
from typing import List, Dict, Any


class IStockValidationStrategy(ABC):
    
    @abstractmethod
    def validate_stock(self, items: List[Dict[str, Any]]) -> bool:
        pass
    
    @abstractmethod
    def get_available_quantity(self, product_name: str) -> int:
        pass
    
    @abstractmethod
    def get_stock_source(self) -> str:
        pass


