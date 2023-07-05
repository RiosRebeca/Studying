#!C:\Users\eurek\AppData\Local\Microsoft\WindowsApps\python3

print("Usando dir e help") 


import random                        #É importante importar as classes no início do arquivo
import math

classe = dir(random)                 #Aqui ele vai criar uma lista com os elementos dentro da classe
print(classe)

classe = len(dir(random))            #Aqui ele vai dizer quantos elementos têm dentro da lista
print(classe)

help(classe)                         #O 'help' vai especificar a função de cada elemento da lista dentro              				     #da classe


classe_math = len(dir(math))
print(classe_math)

classe_math = dir(math)
print(classe_math)
                                       
help(classe_math)                     

"""
Existem muitas funções dentro de uma classe e não conseguimos conhecer todas dentro de uma linguagem, por isso usar o 'help' é importante.
"""