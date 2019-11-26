# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/home/alunos/IA-PYTHON/questionario.csv')

fem = df[df.Sexo == 'F']
mas = df[df.Sexo == 'M']
peso_fem = fem['Peso']
peso_mas = mas['Peso']

plt.figure(figsize=(8, 6))
plt.title('Distribuicao de Pesos')
plt.xlabel('Peso')
plt.ylabel('Alunos')
plt.hist(peso_fem, bins=range(40, 110,10),
    alpha=0.5, label='feminino', color='#FF26E1')
plt.hist(peso_mas, bins=range(40, 110,10),
    alpha=0.5, label='masculino', color='#2DB200')
plt.legend(loc='upper right')
plt.show()
plt.close()