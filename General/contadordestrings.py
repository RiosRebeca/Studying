#!/usr/bin/python3

"""
    Na linha 1 temos uma instrução chamada shebang, ela precisa ser definida para a
    identificação e execução do codigo de python, o shebang é uma instrução posicionada
    necessariamente na primeira linha do arquivo, pois define para o Sistema Operacional 
    qual comando ira executar o script. em termos tecnicos ela fala para o sistema operacional
    qual compilador usar para executar, permitindo a execucao simples.
"""

# Listas/Basico

"""
    Uma lista é definida por [], uma lista é um conjunto de itens ordenados em sequencia e armazenados
    numa unica variavel chamada lista, a lista é uma classe que contem diversos metodos como por exemplo
    index(), pop(). Alguns desses são muitos utilizados.
"""

lista = [] # Definimos a lista

casa = "minha"
lista = ["agua", 2, 3.4, ["pedra"], casa]

"""
    Leia o documento que passarei com todos os metodos disponiveis para a classe lista, e descubra mais 
    sobre essa classe muito usada, explore conforme quiser.
"""

# Aula Listas/String

"""
    Toda string é uma lista. a classe string é definida por uma serie de characters printeveis
    ordenados em um conjunto ou seja uma LISTA, porem a classe string não contem os mesmos metodos
    que a classe lista.

    Ainda assim qualquer string pode ser percorrida.
"""

mystring = "Olá."


"""
    Como a string funciona igual a uma lista, podemos pegar itens especificos dessa lista pelo index
    para usar isso vamos combinar a lista seguido de [], exemplo:
"""

 # Lembrando que O python sempre conta a partir do 0

o = mystring[0]
l = mystring[1]
a = mystring[2]


# Desafio:

"""
    Para o desafio, vc precisa desenvolver uma forma de contar quantas strings tem nessa lista a seguir
    para completar o desafio vc pode usar o
        * for
        * type()
        * if
"""
casa = 99 + 105
lista = ["agua", 2, 3.4, ["terra"], casa, 6, 1235.56, "ar", casa, 777, 666, 999, 3.14, "Fogo", "Shemhamphorasch"]
