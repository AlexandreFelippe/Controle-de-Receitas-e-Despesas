from tkinter import Frame, Label, RAISED, LEFT, NW
from PIL import Image, ImageTk
from model import ControleFinanceiroModel

fundo_tela = "#1e3743"
frame_bg = "#dfe3ee"
fonte = "#38576B"
colors = ["#5588bb", "#66bbbb", "#99bb55", "#ee9944", "#444466", "#bb5555"]


class ControleFinanceiroView:
    def __init__(self, master):
        self.root = master
        self.criar_tela()
        self.criar_frames()
        self.model = ControleFinanceiroModel()
        self.frame1 = Frame1(self)

    def criar_tela(self):
        self.root.title("Controle Financeiro")
        self.root.geometry("1100x670")
        self.root.configure(bg=fundo_tela)
        self.root.resizable(True, True)
        self.root.maxsize(width=1380, height=800)
        self.root.minsize(width=1100, height=670)

    def criar_frames(self):
        self.frame1 = Frame(
            self.root, width=1350, height=50, bg=frame_bg, relief="flat", bd=4
        )
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.08)

        self.frame2 = Frame(
            self.root, width=1350, height=370,
            bg=frame_bg, pady=5, relief="raised"
        )
        self.frame2.place(relx=0.02, rely=0.12, relwidth=0.96, relheight=0.42)

        self.frame3 = Frame(
            self.root, width=1350, height=360, bg=frame_bg, relief="flat", bd=4
        )
        self.frame3.place(relx=0.02, rely=0.56, relwidth=0.96, relheight=0.42)


class Frame1(Frame):
    def __init__(self, controle_financeiro_view):
        super().__init__(controle_financeiro_view.root)
        self.root = controle_financeiro_view.root
        self.frame1 = controle_financeiro_view.frame1
        self.img = Image.open("cofrinho.jpg")
        self.img = self.img.resize((45, 45))
        self.img = ImageTk.PhotoImage(self.img)

        self.img_logo = Label(
            self.frame1,
            image=self.img,
            text=" Bem-vindo(a) ao seu controle financeiro",
            font=("Arial", 16),
            width=1350,
            compound=LEFT,
            padx=5,
            relief=RAISED,
            anchor=NW,
            bg=frame_bg,
        )
        self.img_logo.place(relx=0.02, rely=0.02, relwidth=0.95, relheight=1)
