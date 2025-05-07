import pandas as pd
from IPython.display import display
import seaborn as sns
import matplotlib.pyplot as plt

def analise_univariada_quali(data, variavel):
	"""
	Análise univaria para variáveis categóricas

	1. Retorna o describe transposto e formatado da tabela
	2. Retorna uma tabela com a frequência 
	3. Plota um gráfico com a frequência e exibe os valores
	
	parâmetros:
	data: dataframe com os dados
	variavel: varíável a ser analisada

	retun:
	none

	"""

	if variavel not in data.columns:
		print(f'A variável {variavel} não está no dataframe')

	# Describe
	describe = data[variavel].describe().to_frame()
	describe = describe.T
	describe.index = [variavel]

	print('Descrição da Variável categórica')
	display(describe)

	# Tabela de Frequencia

	tab_freq = data[variavel].value_counts().reset_index()
	tab_freq.columns = [variavel, 'Frequencia']
	tab_freq['Percentual %'] = (tab_freq['Frequencia']/ len(data) * 100).round(2)
	
	# Linha total
	df_total = pd.DataFrame({
		variavel: ['Total'],
		'Frequencia': [tab_freq['Frequencia'].sum()],
		'Percentual %' : [100.0]
	})

	tab_freq = pd.concat([tab_freq, df_total], ignore_index=True)

	print(f'Tabela de frequência dos níveis da variável: {variavel}')
	display(tab_freq)

	# Gráfico de barras com a frequência
	cores_genero = ['#6c35de', '#a364ff']
	plt.figure(figsize=(6,4))
	ax = sns.barplot(x=variavel, y='Frequencia', data=tab_freq[:-1], palette=cores_genero)

	for p in ax.patches:
		altura=p.get_height()
		ax.text(
			p.get_x() + p.get_width() / 2,   # centraliza horizontalmente
        	altura / 2,                      # coloca no meio da barra
        	int(altura),                     # valor exibido (convertido em int)
        	ha='center', va='center',       # alinhamento horizontal e vertical
        	color='#ffffff', fontsize=12, fontweight='bold'
		)
	

	for spine in ['top', 'right', 'left', 'bottom']:
		ax.spines[spine].set_visible(False)

	plt.title(f'Gráfico de Frequência: {variavel}', fontsize=12)
	plt.xlabel(variavel)
	plt.ylabel('Frequência')
	plt.xticks(rotation = 45)
	plt.tight_layout()
	plt.show()


def analise_univariada_quanti(data, variavel):
	"""
	
	"""

	# Estatísticas descritivas
	desc = data[variavel].describe().to_frame().T
	desc = desc.round(4)


	fig = plt.figure(figsize=(14,10))
	fig.suptitle(f'Análise da variável: {variavel}', fontsize=16, y=0.98)

	# adicionando tabela no topo
	ax_table = plt.subplot2grid((3,2),(0,0), colspan=2)
	ax_table.axis('off')

	table = ax_table.table(
		cellText=desc.values,
		colLabels=desc.columns,
		rowLabels=desc.index,
		cellLoc='center',
		loc='center'	
	)

	table.auto_set_font_size(False)
	table.set_fontsize(12)
	table.auto_set_column_width(col=list(range(len(desc.columns))))


	# Histograma -> posição [1,1]
	ax1 = plt.subplot2grid((3,2),(1,0))
	sns.histplot(data[variavel], kde=True, ax=ax1, color='skyblue')
	ax1.set_title('Histograma', fontsize=12)
	ax1.set_xlabel(variavel)

	# [1,2] Gráfico de violino
	ax2 = plt.subplot2grid((3,2),(1,1), sharex=ax1)
	sns.violinplot(x=data[variavel], ax=ax2, color='lightgreen')
	ax1.set_title('Gráfico de violino', fontsize=12)
	ax1.set_xlabel(variavel)

	 # [2,1] Box plot
	ax3 = plt.subplot2grid((3, 2), (2, 0), sharex=ax1)
	sns.boxplot(x=data[variavel], ax=ax3, color="orange")
	ax3.set_title("Box plot", fontsize=12)
	ax3.set_xlabel(variavel)

	 # [2,2] Box plot com pontos sobrepostos
	ax4 = plt.subplot2grid((3, 2), (2, 1), sharex=ax1)
	sns.boxplot(x=data[variavel], ax=ax4, color="lightcoral")
	sns.stripplot(x=data[variavel], ax=ax4, color="black", alpha=0.5, jitter=True)
	ax4.set_title("Box plot com pontos", fontsize=12)
	ax4.set_xlabel(variavel)

	plt.tight_layout(rect=[0,0,1,0.96])
	plt.show()

#df = pd.read_csv('data/segmentation_data.csv')

def df_processed(df):
	df.to_csv('./data/processed/segmentation_processed.csv', index=False, encoding='utf-8')

def analise_bivariada_dist(data, lista_variaveis):

	df_melt = pd.melt(data, value_vars= lista_variaveis, var_name='Variável', value_name='Valor')

	sns.boxplot(x='Variável', y='Valor', data=df_melt)

	plt.title('Distribuiçao de Idade e Renda')
	plt.xlabel('Variável')
	plt.ylabel('Valor')
	plt.grid(True)
	plt.show()