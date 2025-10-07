from interfaces.stock_interface import IStockValidationStrategy
from typing import List, Dict, Any


class SimpleStockValidationStrategy(IStockValidationStrategy):
    """
    Estratégia para validação simples de estoque.
    Baseada na funcionalidade original da prova_douglas.py.
    """
    
    def __init__(self):
        # Estoque simplificado como na prova original
        self.stock = {
            'produto1': 100,
            'produto2': 50,
            'produto3': 75
        }
    
    def validate_stock(self, items: List[Dict[str, Any]]) -> bool:
        """
        Valida se há estoque suficiente para os itens.
        Replica a lógica original: for i in its: if i['nome'] not in est...
        """
        for item in items:
            product_name = item.get('nome', '').strip()
            quantity = item.get('q', 0)
            
            # Verifica se produto existe no estoque
            if product_name not in self.stock:
                print(f"Produto {product_name} não encontrado!")
                return False
            
            # Verifica se há quantidade suficiente
            if self.stock[product_name] < quantity:
                print(f"Estoque insuficiente para {product_name}!")
                return False
        
        return True
    
    def get_available_quantity(self, product_name: str) -> int:
        """
        Retorna a quantidade disponível de um produto.
        """
        return self.stock.get(product_name.strip(), 0)
    
    def get_stock_source(self) -> str:
        return "simple_memory"


class DatabaseStockValidationStrategy(IStockValidationStrategy):
    """
    Estratégia para validação de estoque usando banco de dados.
    Exemplo de extensibilidade - nova strategy sem modificar código existente.
    """
    
    def __init__(self, db_connection=None):
        self.db_connection = db_connection
        # Em uma implementação real, isso seria uma conexão com banco de dados
    
    def validate_stock(self, items: List[Dict[str, Any]]) -> bool:
        """
        Valida estoque usando banco de dados.
        Nova funcionalidade que pode ser adicionada sem modificar código existente.
        """
        for item in items:
            product_name = item.get('nome', '').strip()
            quantity = item.get('q', 0)
            
            # Simula consulta ao banco de dados
            available = self.get_available_quantity(product_name)
            
            if available < quantity:
                print(f"Estoque insuficiente para {product_name}! Disponível: {available}")
                return False
        
        return True
    
    def get_available_quantity(self, product_name: str) -> int:
        """
        Simula consulta ao banco de dados para obter quantidade disponível.
        """
        # Em uma implementação real, isso seria uma query SQL
        # SELECT quantidade FROM estoque WHERE produto = ?
        return 50  # Valor simulado
    
    def get_stock_source(self) -> str:
        return "database"


class APIGetStockValidationStrategy(IStockValidationStrategy):
    """
    Estratégia para validação de estoque usando API externa.
    Exemplo de extensibilidade - nova strategy sem modificar código existente.
    """
    
    def __init__(self, api_endpoint: str = None):
        self.api_endpoint = api_endpoint
    
    def validate_stock(self, items: List[Dict[str, Any]]) -> bool:
        """
        Valida estoque usando API externa.
        Nova funcionalidade que pode ser adicionada sem modificar código existente.
        """
        for item in items:
            product_name = item.get('nome', '').strip()
            quantity = item.get('q', 0)
            
            # Simula chamada para API externa
            available = self.get_available_quantity(product_name)
            
            if available < quantity:
                print(f"Estoque insuficiente para {product_name}! Disponível: {available}")
                return False
        
        return True
    
    def get_available_quantity(self, product_name: str) -> int:
        """
        Simula chamada para API externa para obter quantidade disponível.
        """
        # Em uma implementação real, isso seria uma chamada HTTP
        # GET /api/stock/{product_name}
        return 25  # Valor simulado
    
    def get_stock_source(self) -> str:
        return "external_api"
