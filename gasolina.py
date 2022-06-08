import seaborn as sns
import pandas as pd

data = pd.read_csv('gasolina.csv', sep=',')
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=data, x="dia", y="venda")
  grafico.set(title='Preço médio da gasolina', xlabel='Dia', ylabel='Preço');

grafico.get_figure().savefig("gasolina.png")