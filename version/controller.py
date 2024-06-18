from tkinter import Tk
from model import ControleFinanceiroModel
from view import ControleFinanceiroView, Frame1, Frame2, Frame3
import db_setup

if __name__ == "__main__":
    # Ensure the database is set up
    db_setup.create_db()

    # Initialize the main application
    root = Tk()
    model = ControleFinanceiroModel()
    controle_financeiro = ControleFinanceiroView(root)
    frame1 = Frame1(controle_financeiro)
    frame2 = Frame2(controle_financeiro)
    frame3 = Frame3(controle_financeiro)
    root.mainloop()
