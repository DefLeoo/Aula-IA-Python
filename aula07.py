# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/home/alunos/IA-PYTHON/questionario.csv')

idade = df['Idade']
idade_sum = idade.value_counts()
idade_sum = idade_sum.sort_index()

x = idade_sum.index
y = idade_sum

plt.figure(figsize=(8, 6))

plt.bar(x, y)

plt.title('Distribuicao de Pesos https://cadernoscicomp.com.br/tutorial/matplot-e-pandas/matplot-e-pandas-em-estatistica-basica-histograma-digrama-de-barras/')
plt.xlabel('Peso')
plt.ylabel('Alunos')
plt.xticks(x) 
plt.show()
plt.close()