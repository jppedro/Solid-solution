from typing import List
from interfaces.discount_interface import IDiscountStrategy, ICustomerDiscountStrategy, ISpecialOrderFeeStrategy
from models.order_item import OrderItem
from models.customer import Customer
from models.enums import CustomerType, ItemType


class ItemDiscountStrategy(IDiscountStrategy):
    
    def calculate_discount(self, items: List[OrderItem]) -> float:
        total = 0
        for item in items:
            if item.item_type == ItemType.NORMAL:
                total += item.price * item.quantity
            elif item.item_type == ItemType.DESC10:
                total += item.price * item.quantity * 0.9  # 10% de desconto
            elif item.item_type == ItemType.DESC20:
                total += item.price * item.quantity * 0.8  # 20% de desconto
        
        return total
    
    def get_discount_type(self) -> str:
        return "item_discount"


class NormalCustomerStrategy(ICustomerDiscountStrategy):
    
    def apply_customer_discount(self, total: float, customer: Customer) -> float:
        if customer.customer_type == CustomerType.NORMAL:
            return total  # Sem desconto adicional
        return total  # Para outros tipos, não aplica desconto
    
    def get_customer_type(self) -> CustomerType:
        return CustomerType.NORMAL


class VIPCustomerStrategy(ICustomerDiscountStrategy):
    
    def apply_customer_discount(self, total: float, customer: Customer) -> float:
        if customer.customer_type == CustomerType.VIP:
            return total * 0.95  # 5% de desconto VIP
        return total  # Para outros tipos, não aplica desconto
    
    def get_customer_type(self) -> CustomerType:
        return CustomerType.VIP


class SpecialOrderFeeStrategy(ISpecialOrderFeeStrategy):
    
    def apply_special_fee(self, total: float, is_special: bool) -> float:
        if is_special:
            return total * 1.15  # 15% de taxa especial
        return total  # Sem taxa para pedidos normais


