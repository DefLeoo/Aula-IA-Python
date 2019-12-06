import pandas as pd
import matplotlib.pyplot as plt

#importacao de arquivo (nome, encoding para Brail, separador, lenguaguem)
arquivo = pd.read_csv('IES_2011.csv', encoding='ISO-8859-1',sep=';', engine='python')
ies = arquivo.iloc[:, 9]
mroies = ies.value_counts()
print(mroies)

mroies2 = pd.Series(mroies.inde,index=mroies.values)

plt.figure(figsize=(8,8))
plt.plot(mroies,marker='0')
plt.grid()
plt.tittle('NRO IES POR UF')
plt.xlabel('NRO')
plt.ylabel('UF')
plt.show()