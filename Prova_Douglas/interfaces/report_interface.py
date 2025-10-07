from abc import ABC, abstractmethod
from typing import List, Dict, Any


class IReportStrategy(ABC):
    """
    Interface para estratégias de geração de relatórios.
    """
    
    @abstractmethod
    def generate_report(self, data: List[Dict[str, Any]]) -> str:
        """
        Gera relatório baseado nos dados fornecidos.
        
        Args:
            data: Dados para gerar o relatório
            
        Returns:
            Conteúdo do relatório em string
        """
        pass
    
    @abstractmethod
    def save_report(self, content: str, filename: str) -> bool:
        """
        Salva o relatório em arquivo.
        
        Args:
            content: Conteúdo do relatório
            filename: Nome do arquivo
            
        Returns:
            True se salvo com sucesso, False caso contrário
        """
        pass
    
    @abstractmethod
    def get_report_type(self) -> str:
        """
        Retorna o tipo de relatório.
        
        Returns:
            String identificando o tipo de relatório
        """
        pass


