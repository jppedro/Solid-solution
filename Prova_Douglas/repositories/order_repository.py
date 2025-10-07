# projeto/repositories/order_repository.py
import json
from typing import List, Optional
from models.order import Order
from models.customer import Customer
from models.order_item import OrderItem
from models.enums import OrderStatus
from config.database import DatabaseManager

class OrderRepository:
    """Responsável pela persistência dos dados de pedidos."""
    def __init__(self, db_manager: DatabaseManager):
        self._db_manager = db_manager

    def add(self, order: Order) -> int:
        """Adiciona um novo pedido ao banco de dados."""
        # Converte os itens para um formato serializável
        items_data = []
        for item in order.items:
            item_dict = {
                'name': item.name,
                'price': item.price,
                'quantity': item.quantity,
                'item_type': item.item_type.value  # Converte enum para string
            }
            items_data.append(item_dict)
        
        items_str = json.dumps(items_data)
        
        with self._db_manager as cursor:
            cursor.execute(
                "INSERT INTO orders (customer_name, customer_type, items, total_price, status, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                (order.customer.name, order.customer.customer_type.value, items_str, order.total_price, order.status.value, order.created_at)
            )
            return cursor.lastrowid

    def get_by_id(self, order_id: int) -> Optional[Order]:
        """Busca um pedido pelo seu ID."""
        with self._db_manager as cursor:
            cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
            row = cursor.fetchone()
            return self._row_to_order(row) if row else None

    def update_status(self, order_id: int, status: OrderStatus):
        """Atualiza o status de um pedido."""
        with self._db_manager as cursor:
            cursor.execute("UPDATE orders SET status=? WHERE id=?", (status.value, order_id))

    def get_all(self) -> List[Order]:
        """Retorna todos os pedidos."""
        with self._db_manager as cursor:
            cursor.execute("SELECT * FROM orders")
            rows = cursor.fetchall()
            return [self._row_to_order(row) for row in rows]

    def get_by_customer(self, customer_name: str) -> List[Order]:
        """Retorna todos os pedidos de um cliente específico."""
        with self._db_manager as cursor:
            cursor.execute("SELECT * FROM orders WHERE customer_name=?", (customer_name,))
            rows = cursor.fetchall()
            return [self._row_to_order(row) for row in rows]
    
    def get_all_by_customer(self, customer_name: str) -> List[Order]:
        """Retorna todos os pedidos de um cliente específico (alias para get_by_customer)."""
        return self.get_by_customer(customer_name)
    
    def get_distinct_customers(self) -> List[Customer]:
        """Retorna todos os clientes únicos."""
        from models.enums import CustomerType
        
        with self._db_manager as cursor:
            cursor.execute("SELECT DISTINCT customer_name, customer_type FROM orders")
            rows = cursor.fetchall()
            customers = []
            for row in rows:
                customer = Customer(name=row[0], customer_type=CustomerType(row[1]))
                customers.append(customer)
            return customers

    def _row_to_order(self, row: tuple) -> Order:
        """Converte uma linha do banco de dados em um objeto Order."""
        from models.enums import CustomerType, ItemType
        
        customer = Customer(name=row[1], customer_type=CustomerType(row[2]))
        items_list = json.loads(row[3])
        
        # Converte os itens de volta para objetos OrderItem
        items = []
        for item_data in items_list:
            item = OrderItem(
                name=item_data['name'],
                price=item_data['price'],
                quantity=item_data['quantity'],
                item_type=ItemType(item_data['item_type'])
            )
            items.append(item)
        
        return Order(
            id=row[0],
            customer=customer,
            items=items,
            total_price=row[4],
            status=OrderStatus(row[5]),
            created_at=row[6]
        )