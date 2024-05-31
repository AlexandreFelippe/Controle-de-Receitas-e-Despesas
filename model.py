class FinanceModel:
    def __init__(self):
        self.despesas = []
        self.rendas = []

    def adicionar_despesa(self, categoria, data, valor):
        self.despesas.append(
            {"categoria": categoria, "data": data, "valor": float(valor)}
        )

    def adicionar_renda(self, categoria, data, valor):
        self.rendas.append(
            {"categoria": categoria, "data": data, "valor": float(valor)}
        )

    def obter_dados(self):
        total_renda = sum(renda["valor"] for renda in self.rendas)
        total_despesas = sum(despesa["valor"] for despesa in self.despesas)
        saldo = total_renda - total_despesas
        return {
            "total_renda": total_renda,
            "total_despesas": total_despesas,
            "saldo": saldo,
            "detalhes_despesas": self.despesas,
            "detalhes_rendas": self.rendas,
        }
