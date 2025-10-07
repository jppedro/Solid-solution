from typing import List
from models.order_item import OrderItem


class InventoryService:
    """
    Serviço responsável por gerenciar validações de estoque.
    Segue o princípio SRP - responsabilidade única para validação de estoque.
    """
    
    def __init__(self):
        # Estoque simplificado como na prova original
        self.stock = {
            'produto1': 100,
            'produto2': 50,
            'produto3': 75
        }
    
    def is_stock_sufficient(self, items: List[OrderItem]) -> bool:
        """
        Valida se há estoque suficiente para os itens.
        Replica a lógica original: for i in its: if i['nome'] not in est...
        
        Args:
            items: Lista de itens do pedido
            
        Returns:
            True se há estoque suficiente, False caso contrário
        """
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
        """
        Retorna a quantidade disponível de um produto.
        
        Args:
            product_name: Nome do produto
            
        Returns:
            Quantidade disponível em estoque
        """
        return self.stock.get(product_name.strip(), 0)
    
    def get_stock_source(self) -> str:
        return "simple_memory"
