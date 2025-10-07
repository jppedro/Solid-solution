from interfaces.stock_interface import IStockValidationStrategy
from typing import List, Dict, Any


class SimpleStockValidationStrategy(IStockValidationStrategy):
    
    def __init__(self):
        # Estoque simplificado como na prova original
        self.stock = {
            'produto1': 100,
            'produto2': 50,
            'produto3': 75
        }
    
    def validate_stock(self, items: List[Dict[str, Any]]) -> bool:
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
        return self.stock.get(product_name.strip(), 0)
    
    def get_stock_source(self) -> str:
        return "simple_memory"


class DatabaseStockValidationStrategy(IStockValidationStrategy):
    def __init__(self, db_connection=None):
        self.db_connection = db_connection
        # Em uma implementação real, isso seria uma conexão com banco de dados
    
    def validate_stock(self, items: List[Dict[str, Any]]) -> bool:
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
        # Em uma implementação real, isso seria uma query SQL
        # SELECT quantidade FROM estoque WHERE produto = ?
        return 50  # Valor simulado
    
    def get_stock_source(self) -> str:
        return "database"


class APIGetStockValidationStrategy(IStockValidationStrategy):
    def __init__(self, api_endpoint: str = None):
        self.api_endpoint = api_endpoint
    
    def validate_stock(self, items: List[Dict[str, Any]]) -> bool:
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
        # Em uma implementação real, isso seria uma chamada HTTP
        # GET /api/stock/{product_name}
        return 25  # Valor simulado
    
    def get_stock_source(self) -> str:
        return "external_api"
