import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_excel('dados_temperatura_umidade.xlsx')

plt.figure(figsize=(10,5))
plt.plot(dados['Data'], dados['Temperatura'], label='Temperatura (°C)', color='red')
plt.plot(dados['Data'], dados['Umidade'], label='Umidade (%)', color='blue')
plt.xlabel('Data e Hora')
plt.ylabel('Valores')
plt.title('Variação de Temperatura e Umidade')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
