from app import capturar_dados_clima
from salvarDados import salvar_dados
import tkinter as tk

def executar_automacao(botao_executar, label_status):
    botao_executar.config(state=tk.DISABLED) 
    label_status.config(text="Capturando dados...", fg="#FFA500") 

    temperatura, umidade = capturar_dados_clima()
    salvar_dados(temperatura, umidade)

    label_status.config(text=f"Dados capturados e salvos!\nTemperatura: {temperatura} | Umidade: {umidade}", fg="#32CD32")
    botao_executar.config(state=tk.NORMAL)

    print("Processo finalizado com sucesso! Dados capturados e armazenados.")