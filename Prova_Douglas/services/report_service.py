# services/report_service.py

from interfaces.repository_interface import IOrderRepository
from models.enums import ReportType

class ReportService:
    def __init__(self, order_repository: IOrderRepository):
        # Simplifica o nome da variável interna
        self._order_repo = order_repository
        
        # Cria um mapeamento de métodos no construtor.
        # Isso adere ao OCP ao eliminar a cadeia 'if/elif' no método principal.
        self._report_generators = {
            ReportType.SALES: self._generate_sales_report,
            ReportType.CLIENTS: self._generate_clients_report
        }

    def generate_report(self, report_type: ReportType):
        # 1. Obtém a função de geração a partir do mapeamento
        generator = self._report_generators.get(report_type)
        
        if generator:
            # 2. Executa a função encontrada (Polimorfismo)
            generator()
        else:
            # Caso o tipo de relatório não seja válido
            print("Tipo de relatório inválido.")

    def _generate_sales_report(self):
        orders = self._order_repo.get_all()
        print("=== RELATÓRIO DE VENDAS ===")
        total_sales = 0
        report_content = ""
        for order in orders:
            line = f"Pedido #{order.id} Cliente: {order.customer.name} Total: R${order.total_price:.2f} Status: {order.status.value}\n"
            print(line.strip())
            report_content += line
            total_sales += order.total_price
            
        summary_line = f"Total Geral: R${total_sales:.2f}\n"
        print(summary_line.strip())
        report_content += summary_line

        with open('rel_vendas.txt', 'w') as f:
            f.write(report_content)

    def _generate_clients_report(self):
        customers = self._order_repo.get_distinct_customers()
        print("=== RELATÓRIO DE CLIENTES ===")
        report_content = ""
        for customer in customers:
            # Assume que o repositório suporta esta busca
            orders = self._order_repo.get_all_by_customer(customer.name) 
            total_spent = sum(order.total_price for order in orders)
            line = f"Cliente: {customer.name} ({customer.customer_type.value}) - Total gasto: R${total_spent:.2f}\n"
            print(line.strip())
            report_content += f"{customer.name},{customer.customer_type.value}\n"
            
        with open('rel_clientes.txt', 'w') as f:
            f.write(report_content)