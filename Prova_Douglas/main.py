# main.py - Refatorado seguindo princípios SOLID
# Replica exatamente as funcionalidades da main original do prova_douglas.py

# Importações das classes refatoradas
from models.customer import Customer
from models.order_item import OrderItem
from models.enums import OrderStatus, CustomerType, ItemType, PaymentMethod, ReportType
from repositories.order_repository import OrderRepository
from services.order_service import OrderService
from services.notification_service import NotificationService
from services.loyalty_service import LoyaltyService
from services.inventory_service import InventoryService
from services.report_service import ReportService
from services.payment_service import PaymentService
from interfaces.repository_interface import IOrderRepository
from strategies.discount_strategy import ItemDiscountStrategy, VIPCustomerStrategy, NormalCustomerStrategy, SpecialOrderFeeStrategy
from strategies.payment_strategy import CardPaymentStrategy, PIXPaymentStrategy, BoletoPaymentStrategy
from config.database import DatabaseManager
from typing import Dict

def main():
    """
    Função principal que executa o exemplo de uso.
    Replica exatamente as funcionalidades da main original do prova_douglas.py
    usando a nova arquitetura refatorada seguindo princípios SOLID.
    """
    
    # --- 1. Configuração da Injeção de Dependência ---
    # Criando instâncias das strategies
    item_discount_strategy = ItemDiscountStrategy()
    normal_customer_strategy = NormalCustomerStrategy()
    vip_customer_strategy = VIPCustomerStrategy()
    special_fee_strategy = SpecialOrderFeeStrategy()
    
    # Criando strategies de pagamento
    card_payment_strategy = CardPaymentStrategy()
    pix_payment_strategy = PIXPaymentStrategy()
    boleto_payment_strategy = BoletoPaymentStrategy()
    
    # Mapeamento de strategies de pagamento
    payment_strategies = {
        PaymentMethod.CARD: card_payment_strategy,
        PaymentMethod.PIX: pix_payment_strategy,
        PaymentMethod.BOLETO: boleto_payment_strategy
    }
    
    # Criando serviços
    db_manager = DatabaseManager('loja.db')
    order_repository = OrderRepository(db_manager)
    notification_service = NotificationService()
    loyalty_service = LoyaltyService()
    inventory_service = InventoryService()
    report_service = ReportService(order_repository)
    
    # Criando OrderService com injeção de dependências
    order_service = OrderService(
        order_repository=order_repository,
        notification_service=notification_service,
        loyalty_service=loyalty_service,
        inventory_service=inventory_service,
        discount_strategy=item_discount_strategy,
        customer_discount_strategy=normal_customer_strategy,  # Será alterado para VIP quando necessário
        special_fee_strategy=special_fee_strategy
    )
    
    # Criando PaymentService
    payment_service = PaymentService(
        payment_strategies=payment_strategies,
        order_repository=order_repository,
        order_service=order_service
    )

    # --- 2. Exemplo de Uso (replicando exatamente o fluxo original) ---
    
    print("=== SISTEMA DE LOJA REFATORADO ===")
    
    # --- Pedido 1: Cliente Normal ---
    print("--- Criando Pedido 1 (Cliente Normal) ---")
    
    # Criando itens como no original: produto1 (normal) e produto2 (desc10)
    items1 = [
        OrderItem(name='produto1', price=100, quantity=2, item_type=ItemType.NORMAL),
        OrderItem(name='produto2', price=50, quantity=1, item_type=ItemType.DESC10)
    ]
    
    # Validando estoque (como no original)
    if inventory_service.is_stock_sufficient(items1):
        # Criando cliente normal
        customer1 = Customer(name='João Silva', customer_type=CustomerType.NORMAL)
        
        try:
            # Criando pedido (equivalente ao add_ped original)
            id1 = order_service.create_order(customer1, items1, is_special=False)
            print(f"Pedido {id1} criado!")
            
            # Processando pagamento com cartão (equivalente ao proc_pag original)
            payment_service.process_payment(id1, PaymentMethod.CARD, 250.0)
            
            # Atualizando status para enviado (equivalente ao upd_st original)
            order_service.update_order_status(id1, OrderStatus.SHIPPED)
            
            # Atualizando status para entregue
            order_service.update_order_status(id1, OrderStatus.DELIVERED)
            
        except ValueError as e:
            print(f"Erro ao criar pedido: {e}")
    else:
        print("Estoque insuficiente para o pedido 1")
    
    print()
    
    print("Criando Pedido 2 (Cliente VIP)")
    
    items2 = [
        OrderItem(name='produto3', price=200, quantity=1, item_type=ItemType.DESC20)
    ]
    
    if inventory_service.is_stock_sufficient(items2):
        customer2 = Customer(name='Maria Santos', customer_type=CustomerType.VIP)
        
        try:
            # Alterando strategy para VIP customer
            order_service._customer_discount_strategy = vip_customer_strategy
            
            # Criando pedido VIP (equivalente ao add_ped original)
            id2 = order_service.create_order(customer2, items2, is_special=False)
            
            # Processando pagamento com PIX (equivalente ao proc_pag original)
            payment_service.process_payment(id2, PaymentMethod.PIX, 160.0)
            
        except ValueError as e:
            print(f"Erro ao criar pedido: {e}")
    else:
        print("Estoque insuficiente para o pedido 2")
    
    print()
    
    # --- 3. Geração de Relatórios (equivalente ao gerar_rel original) ---
    print("Gerando Relatórios")
    
    # Relatório de vendas (equivalente ao gerar_rel('vendas') original)
    report_service.generate_report(ReportType.SALES)
    print()
    
    # Relatório de clientes (equivalente ao gerar_rel('clientes') original)
    report_service.generate_report(ReportType.CLIENTS)
    


if __name__ == '__main__':
    main()