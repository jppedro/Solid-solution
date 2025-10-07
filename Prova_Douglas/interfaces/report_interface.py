from abc import ABC, abstractmethod
from typing import List, Dict, Any


class IReportStrategy(ABC):
    
    @abstractmethod
    def generate_report(self, data: List[Dict[str, Any]]) -> str:
        pass
    
    @abstractmethod
    def save_report(self, content: str, filename: str) -> bool:
        pass
    
    @abstractmethod
    def get_report_type(self) -> str:
        pass


