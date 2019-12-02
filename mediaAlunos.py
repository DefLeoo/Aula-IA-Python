# -*- coding: UTF-8 -*-

import pandas as pl

alunosDicionario  = {'Nome':['Ricardo', 'roberto', 'Carlos'], 
           'Nota':[4,7,5,5, 9],
           'Aprovado':['Não', 'Sim', 'Não', 'Sim']}


a = pd.DataFrame(alunosDicionario)

print(a)


"""
 A saida seria 
   
    Nome        Nota   Aproado
  
 0  Ricardo     4.0    Não
 1  Pedro       7.0    Sim
 2  Roberto     5.5    Não
 3  Carlos      9.0    Sim

"""
"""

   Para trabalhar com DataFrame


   //para exibir dados de qualquer planilha excel:

   a.head()

   //Tamanho do DataFrame ou seja quantas linhas e quantas colunas:

   a.shape



   //da os dados da tabela como soma, VALOR MÁX , VALOR MIN, MEDIA E ETC:

    a.describe()


   
    // FILTRANDO DADOS DA TABELA:

    a['Nome'] -> imprime todos os dados da coluna nome


    a.loc[[0]] -> Linha do indice 0 = 0  Ricardo     4.0    Não


    a.loc[[0, 2]] ->  0  Ricardo     4.0    Não
                      1  Pedro       7.0    Sim


     a.loc[[0 : 2]] -> Desta forma ele puxa do indice 0 até o 3


     a.loc[a['Nome']=='Pedro'] -> Filtra por nome


   // Vou selecionar os atletas que tem probabilidade de serem Nota maior ou igual a 10%:
    a.loc[(a['Nota']*100) >= 10]

   

   // Criando uma nova planilha a partir da que já existe:

    planila2 = a.loc[0:2]



    // Criando uma nova tabela a partir da que existe onde nota == 9

    planilha2 = a.loc[a['Nota']==9]
    
    //Ou para diferente de 9

    planilha2 = a.loc[a['Nota']!=9]

    print(planilha2)

    //Para alunos reprovados
    
    alunosReprovads =  a.loc[a['Aprovado']!='Não']


"""
    
