from interfaces.payment_interface import IPaymentStrategy
from models.order import Order
from models.enums import PaymentMethod


class CardPaymentStrategy(IPaymentStrategy):
    
    def process_payment(self, order: Order, amount: float) -> bool:
        print("Processando pagamento com cartão...")
        # valida cartão (simplificado) - como na prova original
        print("Cartão validado!")
        return True
    
    def get_payment_method(self) -> PaymentMethod:
        return PaymentMethod.CARD
    
    def requires_approval(self) -> bool:
        return True  # Cartão aprova automaticamente


class PIXPaymentStrategy(IPaymentStrategy):
    def process_payment(self, order: Order, amount: float) -> bool:
        print("Gerando QR Code PIX...")
        print("PIX recebido!")
        return True
    
    def get_payment_method(self) -> PaymentMethod:
        return PaymentMethod.PIX
    
    def requires_approval(self) -> bool:
        return True  # PIX aprova automaticamente


class BoletoPaymentStrategy(IPaymentStrategy):
    def process_payment(self, order: Order, amount: float) -> bool:
        print("Gerando boleto...")
        print("Boleto gerado!")
        return True
    
    def get_payment_method(self) -> PaymentMethod:
        return PaymentMethod.BOLETO
    
    def requires_approval(self) -> bool:
        return False  # Boleto não aprova automaticamente


