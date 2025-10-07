from interfaces.points_interface import IPointsStrategy


class NormalPointsStrategy(IPointsStrategy):
    """
    Estratégia para cálculo de pontos para clientes normais.
    Baseada na funcionalidade original: pts = int(p['tot'])
    """
    
    def calculate_points(self, order_total: float) -> int:
        """
        Calcula pontos para cliente normal.
        Replica a lógica original: pts = int(p['tot'])
        """
        return int(order_total)
    
    def get_points_multiplier(self) -> float:
        return 1.0
    
    def get_customer_type(self) -> str:
        return "normal"


class VIPPointsStrategy(IPointsStrategy):
    """
    Estratégia para cálculo de pontos para clientes VIP.
    Baseada na funcionalidade original: pts = int(p['tot'] * 2)
    """
    
    def calculate_points(self, order_total: float) -> int:
        """
        Calcula pontos para cliente VIP.
        Replica a lógica original: pts = int(p['tot'] * 2)
        """
        return int(order_total * 2)
    
    def get_points_multiplier(self) -> float:
        return 2.0
    
    def get_customer_type(self) -> str:
        return "vip"


class PremiumPointsStrategy(IPointsStrategy):
    """
    Estratégia para cálculo de pontos para clientes premium.
    Exemplo de extensibilidade - nova strategy sem modificar código existente.
    """
    
    def calculate_points(self, order_total: float) -> int:
        """
        Calcula pontos para cliente premium.
        Nova funcionalidade: 3x pontos para clientes premium.
        """
        return int(order_total * 3)
    
    def get_points_multiplier(self) -> float:
        return 3.0
    
    def get_customer_type(self) -> str:
        return "premium"


class CorporatePointsStrategy(IPointsStrategy):
    """
    Estratégia para cálculo de pontos para clientes corporativos.
    Exemplo de extensibilidade - nova strategy sem modificar código existente.
    """
    
    def calculate_points(self, order_total: float) -> int:
        """
        Calcula pontos para cliente corporativo.
        Nova funcionalidade: pontos baseados em faixas de valor.
        """
        if order_total >= 10000:
            return int(order_total * 2.5)  # 2.5x para pedidos grandes
        elif order_total >= 5000:
            return int(order_total * 2.0)  # 2.0x para pedidos médios
        else:
            return int(order_total * 1.5)  # 1.5x para pedidos pequenos
    
    def get_points_multiplier(self) -> float:
        return 2.0  # Multiplicador base
    
    def get_customer_type(self) -> str:
        return "corporate"
