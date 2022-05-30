#carregamento de libs
import matplotlib.pyplot as plt
import pandas as pd

#importando dados para análise
dados = pd.read_csv ('console.csv')

#selecionando e somando os dados que serão analisados
pc = dados.loc[(dados['Manufacturer']=='Computer')]
vendas_pc = pc ['Sales'].sum ()

sony = dados.loc[(dados['Manufacturer']=='Sony')]
vendas_sony = sony ['Sales'].sum()

nintendo = dados.loc[(dados['Manufacturer']=='Nintendo')]
vendas_nintendo = nintendo ['Sales'].sum()

microsoft = dados.loc[(dados['Manufacturer']=='Microsoft')]
vendas_microsoft = microsoft ['Sales'].sum()

#juntando todos os resultados para montar o gráfico de pizza
venda = [vendas_pc, vendas_sony, vendas_nintendo, vendas_microsoft]

#separando as vendas por fabricante
fabricante = dados['Manufacturer']
fabricante = fabricante.unique()

#cores para o gráfico
colors = ['blue', 'black', 'red', 'green']

#montagem do gráfico
patches, texts, autotexts = plt.pie(venda, colors=colors, autopct="", startangle=90, explode=(0.1,0.1,0.2,0.3))
plt.title ('Vendas Por Fabricante')
plt.legend (patches, fabricante, loc='lower right')
plt.axis('equal')
plt.tight_layout()
plt.show()
