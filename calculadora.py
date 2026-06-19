import tkinter as tk

def clicar(valor):
    entrada.set(entrada.get() + str(valor))

def limpar():
    entrada.set("")

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.set(str(resultado))
    except:
        entrada.set("Erro")

# Janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.resizable(False, False)
anela.attributes("-alpha", 0.5)  

# Variável
entrada = tk.StringVar()

# Visor
visor = tk.Entry(
    janela,
    textvariable=entrada,
    font=("Arial", 20),
    bd=10,
    relief=tk.RIDGE,
    justify="right"
)
visor.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Botões organizados
botoes = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Criando os botões com grid
for i, linha in enumerate(botoes):
    for j, valor in enumerate(linha):
        if valor == "=":
            botao = tk.Button(janela, text=valor, font=("Arial", 15),
                              command=calcular)
        else:
            botao = tk.Button(janela, text=valor, font=("Arial", 15),
                              command=lambda v=valor: clicar(v))

        botao.grid(row=i+1, column=j, sticky="nsew", padx=2, pady=2)

# Botão limpar (ocupa largura)
botao_limpar = tk.Button(janela, text="C", font=("Arial", 15), command=limpar)
botao_limpar.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

# Ajuste de tamanho automático
for i in range(6):
    janela.rowconfigure(i, weight=1)

for j in range(4):
    janela.columnconfigure(j, weight=1)

# Rodar
janela.mainloop()