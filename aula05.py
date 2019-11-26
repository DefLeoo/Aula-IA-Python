# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/home/alunos/IA-PYTHON/questionario.csv')

"""
Criando um histograma para com os pesos dos alunos
"""
peso = df['Peso']

plt.figure(figsize=(8, 6))
plt.hist(peso, bins=range(40, 110,10))
plt.title('Distribuicao de Pesos')
plt.xlabel('Peso')
plt.ylabel('Alunos')
plt.show()
plt.close()