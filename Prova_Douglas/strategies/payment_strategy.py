from interfaces.payment_interface import IPaymentStrategy
from models.order import Order
from models.enums import PaymentMethod


class CardPaymentStrategy(IPaymentStrategy):
    """
    Estratégia para pagamento com cartão.
    Baseada na funcionalidade original: if m == 'cartao'
    """
    
    def process_payment(self, order: Order, amount: float) -> bool:
        """
        Processa pagamento com cartão.
        Replica a lógica original: valida cartão e aprova automaticamente.
        """
        print("Processando pagamento com cartão...")
        # valida cartão (simplificado) - como na prova original
        print("Cartão validado!")
        return True
    
    def get_payment_method(self) -> PaymentMethod:
        return PaymentMethod.CARD
    
    def requires_approval(self) -> bool:
        return True  # Cartão aprova automaticamente


class PIXPaymentStrategy(IPaymentStrategy):
    """
    Estratégia para pagamento com PIX.
    Baseada na funcionalidade original: elif m == 'pix'
    """
    
    def process_payment(self, order: Order, amount: float) -> bool:
        """
        Processa pagamento com PIX.
        Replica a lógica original: gera QR Code e aprova automaticamente.
        """
        print("Gerando QR Code PIX...")
        print("PIX recebido!")
        return True
    
    def get_payment_method(self) -> PaymentMethod:
        return PaymentMethod.PIX
    
    def requires_approval(self) -> bool:
        return True  # PIX aprova automaticamente


class BoletoPaymentStrategy(IPaymentStrategy):
    """
    Estratégia para pagamento com boleto.
    Baseada na funcionalidade original: elif m == 'boleto'
    """
    
    def process_payment(self, order: Order, amount: float) -> bool:
        """
        Processa pagamento com boleto.
        Replica a lógica original: gera boleto mas não aprova automaticamente.
        """
        print("Gerando boleto...")
        print("Boleto gerado!")
        return True
    
    def get_payment_method(self) -> PaymentMethod:
        return PaymentMethod.BOLETO
    
    def requires_approval(self) -> bool:
        return False  # Boleto não aprova automaticamente


