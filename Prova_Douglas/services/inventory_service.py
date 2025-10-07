from typing import List
from models.order_item import OrderItem


class InventoryService:
    
    def __init__(self):
        # Estoque simplificado como na prova original
        self.stock = {
            'produto1': 100,
            'produto2': 50,
            'produto3': 75
        }
    
    def is_stock_sufficient(self, items: List[OrderItem]) -> bool:
        for item in items:
            product_name = item.name.strip()
            quantity = item.quantity
            
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
