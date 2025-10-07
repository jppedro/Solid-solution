from interfaces.report_interface import IReportStrategy
from typing import List, Dict, Any


class SalesReportStrategy(IReportStrategy):
    """
    Estratégia para geração de relatório de vendas.
    Baseada na funcionalidade original: if tipo == 'vendas'
    """
    
    def generate_report(self, data: List[Dict[str, Any]]) -> str:
        """
        Gera relatório de vendas.
        Replica a lógica original da prova_douglas.py.
        """
        report_lines = ["=== RELATÓRIO DE VENDAS ==="]
        total_general = 0
        
        for order in data:
            order_id = order.get('id', 0)
            customer = order.get('cli', 'N/A')
            total = order.get('tot', 0.0)
            status = order.get('st', 'N/A')
            
            report_lines.append(f"Pedido #{order_id} - Cliente: {customer} - Total: R${total:.2f} - Status: {status}")
            total_general += total
        
        report_lines.append(f"Total Geral: R${total_general:.2f}")
        
        return "\n".join(report_lines)
    
    def save_report(self, content: str, filename: str) -> bool:
        """
        Salva relatório de vendas em arquivo.
        Replica a funcionalidade original: with open('rel_vendas.txt', 'w') as f
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # Extrai apenas o total geral para salvar (como na prova original)
                lines = content.split('\n')
                total_line = [line for line in lines if 'Total Geral' in line]
                if total_line:
                    f.write(f"Total de vendas: {total_line[0].split('R$')[1].strip()}")
                else:
                    f.write("Total de vendas: 0")
            return True
        except Exception as e:
            print(f"Erro ao salvar relatório: {e}")
            return False
    
    def get_report_type(self) -> str:
        return "vendas"


class CustomerReportStrategy(IReportStrategy):
    """
    Estratégia para geração de relatório de clientes.
    Baseada na funcionalidade original: elif tipo == 'clientes'
    """
    
    def generate_report(self, data: List[Dict[str, Any]]) -> str:
        """
        Gera relatório de clientes.
        Replica a lógica original da prova_douglas.py.
        """
        report_lines = ["=== RELATÓRIO DE CLIENTES ==="]
        
        for customer in data:
            name = customer.get('name', 'N/A')
            customer_type = customer.get('type', 'N/A')
            total_spent = customer.get('total_spent', 0.0)
            
            report_lines.append(f"Cliente: {name} ({customer_type}) - Total gasto: R${total_spent:.2f}")
        
        return "\n".join(report_lines)
    
    def save_report(self, content: str, filename: str) -> bool:
        """
        Salva relatório de clientes em arquivo.
        Replica a funcionalidade original: with open('rel_clientes.txt', 'w') as f
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # Salva dados dos clientes (como na prova original)
                lines = content.split('\n')[1:]  # Remove o cabeçalho
                for line in lines:
                    if line.strip():
                        # Extrai nome e tipo do cliente
                        if 'Cliente:' in line:
                            parts = line.split('Cliente:')[1].split('(')
                            if len(parts) >= 2:
                                name = parts[0].strip()
                                customer_type = parts[1].split(')')[0].strip()
                                f.write(f"{name},{customer_type}\n")
            return True
        except Exception as e:
            print(f"Erro ao salvar relatório: {e}")
            return False
    
    def get_report_type(self) -> str:
        return "clientes"


class JSONReportStrategy(IReportStrategy):
    """
    Estratégia para geração de relatório em formato JSON.
    Exemplo de extensibilidade - nova strategy sem modificar código existente.
    """
    
    def generate_report(self, data: List[Dict[str, Any]]) -> str:
        """
        Gera relatório em formato JSON.
        Nova funcionalidade que pode ser adicionada sem modificar código existente.
        """
        import json
        
        report_data = {
            "report_type": "json",
            "generated_at": "2024-01-01T00:00:00Z",
            "data": data
        }
        
        return json.dumps(report_data, indent=2, ensure_ascii=False)
    
    def save_report(self, content: str, filename: str) -> bool:
        """
        Salva relatório JSON em arquivo.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Erro ao salvar relatório JSON: {e}")
            return False
    
    def get_report_type(self) -> str:
        return "json"


class CSVReportStrategy(IReportStrategy):
    """
    Estratégia para geração de relatório em formato CSV.
    Exemplo de extensibilidade - nova strategy sem modificar código existente.
    """
    
    def generate_report(self, data: List[Dict[str, Any]]) -> str:
        """
        Gera relatório em formato CSV.
        Nova funcionalidade que pode ser adicionada sem modificar código existente.
        """
        if not data:
            return ""
        
        # Cabeçalho CSV
        headers = list(data[0].keys())
        csv_lines = [",".join(headers)]
        
        # Dados CSV
        for item in data:
            values = [str(item.get(header, "")) for header in headers]
            csv_lines.append(",".join(values))
        
        return "\n".join(csv_lines)
    
    def save_report(self, content: str, filename: str) -> bool:
        """
        Salva relatório CSV em arquivo.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Erro ao salvar relatório CSV: {e}")
            return False
    
    def get_report_type(self) -> str:
        return "csv"
