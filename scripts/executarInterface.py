import tkinter as tk
from executarAutomacao import executar_automacao

def configurar_interface():
    janela = tk.Tk()
    janela.title("Captura de Temperatura e Umidade")
    janela.geometry("500x300")  
    janela.config(bg="#FFFFFF")  

    titulo = tk.Label(janela, text="Monitoramento do Clima", font=("Helvetica", 18, "bold"), bg="#FFFFFF", fg="#333")
    titulo.pack(pady=20)

    descricao = tk.Label(janela, text="Clique abaixo para capturar os dados de temperatura e umidade.", 
                         font=("Arial", 12), bg="#FFFFFF", fg="#555")
    descricao.pack(pady=10)

    botao_executar = tk.Button(janela, text="Capturar Dados", font=("Arial", 14), 
                               command=lambda: executar_automacao(botao_executar, label_status),  
                               bg="#1abc9c", fg="white", relief="flat", padx=20, pady=10, bd=0)
    botao_executar.pack(pady=20)

    label_status = tk.Label(janela, text="", font=("Arial", 12), bg="#FFFFFF", fg="#333")
    label_status.pack(pady=15)

    def on_enter(e):
        botao_executar.config(bg="#45a049")

    def on_leave(e):
        botao_executar.config(bg="#1abc9c")

    botao_executar.bind("<Enter>", on_enter)
    botao_executar.bind("<Leave>", on_leave)

    janela.mainloop()

configurar_interface()
