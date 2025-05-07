import pandas as pd
from load_data import df_custormers
from utils import df_processed
import warnings
warnings.filterwarnings("ignore")


# Removendo a coluna ID pois não será utilizada na análise
df_custormers.drop(columns='ID', inplace=True)

# Renomeando as colunas categóricas

df_custormers['Sex'].replace({0:'Male', 1: 'female'}, inplace=True)
df_custormers['Marital status'].replace({0:'single', 1: 'non-sngle'}, inplace=True)
df_custormers['Education'].replace({0:'other/unknown', 1: 'high school', 2: 'university', 3: 'graduate school'}, inplace=True)
df_custormers['Occupation'].replace({0:'unemployed/unskilled', 1: 'skilled employee/official', 2: 'management/highly qualified employee'}, inplace=True)
df_custormers['Settlement size'].replace({0:'small city', 1: 'mid-sized city', 2:'big city'}, inplace=True)



# Salvando o dataframe processado
df_processed(df_custormers)