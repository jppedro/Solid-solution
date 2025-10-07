from enum import Enum

class OrderStatus(Enum):
    PENDING = 'pendente'
    APPROVED = 'aprovado'
    SHIPPED = 'enviado'
    DELIVERED = 'entregue'
    CANCELED = 'cancelado'

class PaymentMethod(Enum):
    CARD = 'cartao'
    PIX = 'pix'
    BOLETO = 'boleto'

class CustomerType(Enum):
    NORMAL = 'normal'
    VIP = 'vip'
    SPECIAL = 'especial'

class ItemType(Enum):
    NORMAL = 'normal'
    DESC10 = 'desc10'
    DESC20 = 'desc20'

class ReportType(Enum):
    SALES = 'vendas'
    CLIENTS = 'clientes'