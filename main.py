from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Método Babilônico para encontrar raizes quadradas')


framemain = ttk.Frame(root, padding=50,
                      borderwidth=5, relief='flat')
framemain.grid()


Label_informacao = ttk.Label(framemain, text="Quantas casas decimais terá a precisão desejada para o método?").grid(
    column=0, row=0)
entrada1 = StringVar()
caixadeentrada1 = ttk.Entry(
    framemain, textvariable=entrada1).grid(column=0, row=1)


Label_informacao2 = ttk.Label(framemain, text="Digite o numero que deseja descobrir a raiz quadrada").grid(
    column=0, row=2)
entrada2 = StringVar()
caixadeentrada2 = ttk.Entry(
    framemain, textvariable=entrada2).grid(column=0, row=3)


def calculadora(entrada1=entrada1, entrada2=entrada2):

    precisao = int(entrada1.get())
    numero_aleatorio = int(entrada2.get())
    erro_de_aproximacao = (10**(-precisao))

    intervalo_de_aproximacao = []

    for c in range(1, numero_aleatorio):
        intervalo_de_aproximacao.append(c)

    aproximacaoinicial = sum(intervalo_de_aproximacao)/(numero_aleatorio-1)
    aproximacaoreal = numero_aleatorio/aproximacaoinicial
    i = abs((aproximacaoreal**2) - numero_aleatorio)

    while (i > erro_de_aproximacao):
        aproximacaoinicial = aproximacaoinicial/2 + aproximacaoreal/2
        aproximacaoreal = numero_aleatorio/aproximacaoinicial
        i = abs((aproximacaoreal**2) - numero_aleatorio)

    label_resultadofinal['text'] = aproximacaoreal


botaocalcular = ttk.Button(framemain, text="Calcular", command=calculadora)
botaocalcular.grid(column=0, row=8)


frameresultado = ttk.Frame(root, padding=15, borderwidth=5, relief='solid')
frameresultado.grid(column=0, row=3)

label_resultado = ttk.Label(
    frameresultado, text='O número aproximado para raiz é:').grid(column=0, row=0)

label_resultadofinal = ttk.Label(
    frameresultado, text='')
label_resultadofinal.grid(column=0, row=1)


ttk.Button(root, text="Quit",
           command=root.destroy).grid(column=0, row=5)
root.mainloop()
