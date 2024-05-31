from model import FinanceModel


class FinanceController:
    def __init__(self, view):
        self.view = view
        self.model = FinanceModel()

    def inserir_despesas(self, categoria, data, valor):
        self.model.adicionar_despesa(categoria, data, valor)
        self.atualizar_interface()

    def inserir_renda(self, categoria, data, valor):
        self.model.adicionar_renda(categoria, data, valor)
        self.atualizar_interface()

    def atualizar_interface(self):
        dados = self.model.obter_dados()
        self.view.atualizar_graficos(dados)
