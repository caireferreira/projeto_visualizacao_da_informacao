#carregar libs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#carregar dados para análise, processamento e visualização
df = pd.read_csv('console.csv')

#definindo o gráfico
console = df['ConsoleID']
indice = np.arange(len(console))
vendas = df['Sales']

#montagem do gráfico
plt.bar(indice, vendas, color=['black'])
plt.xticks(indice, console)
plt.tight_layout()
plt.ylabel('Vendas em Milhões')#, fontsize=50)
plt.xlabel('Consoles')#, fontsize=50)
plt.title('Top 10 - Consoles Mais Vendidos')#, fontsize=50)
plt.show()
