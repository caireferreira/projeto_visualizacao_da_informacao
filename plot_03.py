#importando as libs
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

#carregamento de arquivo para analise
dados = pd.read_csv('console.csv')

#dividindo produtos por fabricantes
consoles = dados['ConsoleID']
produtos = dados['Manufacturer']
vendas = dados['Sales']

#montagem da treemap
df = pd.DataFrame(dict(consoles=consoles, produtos=produtos, vendas=vendas))
fig = px.treemap(df,path=[produtos,consoles], values=vendas)
fig.show()
