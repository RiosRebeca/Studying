print("DEFININDO FUNÇÕES")

'''

Funfções: são pequenos trechos de código que realizam tarefas específicas; 
Uma função pode ou não receber uma entrada de dados e retormar uma saída de dados. Elas são muito úteis para executar procedimentos similares várias vezes.

OBS: se vc escrever uma função que realiza várias tarefas dentro delas, é bom fazer uma verificação para 1ue a função seja simplificada


Usamos algumas funções como: print(), len(), max(), min(), counter(), etc.

 Algumas funções podemos usar para qualquer tipo de dados, como o print() que vai impirmir qualquer dado, independente se for str, int, float, etc. 
 Já existente funções que não servem para qualquer classe, exemplo .append() que é usado para listas.
 Existem funções que recebem dados do usuário como input() e outras que não recebem dados como .clear() (usados para limpar listas).

As Built-in existem para fazer o DRY (Don't repet yourself) para não ficar repetindo o mesmo código várias vezes.

Existem formas de CONSTUIR sua própria função.

def nome_da_função(parametros_de_entrada):
    blobo_da_função

onde: 

nome_da_função: sempre com letra minúscula, se for nome composto as palavras devem ser separadas por _

parametros de entrada: são opciomais, onde tendo mais de um devem ser separados por "," sendo opcionais ou não (quais dados a função recebe para funcionar?)

bloco da função: também chamado de corpo da função ou implementação, é onde o processamento da função acontece. Neste bloco pode ter ou não retorno da função.

OBS: para definir uma função usamos uma palavra reservada def, informando ao pyth0on que estamos definindo uma função. Também abrimos o bloco de código com o já conhecido ":" que é utilizado em python para definir blocos.


1- Dentro das funções podemos usar outras funções 
2 - nossa função só executa uma tarefa, ou seja a única coisa que ela faz é dizer "oi"
3- A função não recebe nenhum parâmetro de entrada quando o () não tem nada 
4 - A função só retorna algo se tiver return

Em python podemos inclusive criar variáveis do tipop de uma função e executar essa função através da variável.

OBS: Não precisamos necessariamente criar uma variável ára receber o retorno de uma função. Podemos passar a execurção da função para outras funções (como o print).


'''

# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco'] 

print(cores)          # função integrada (Built-in) do python print()
                      # Built-in são funções já existentes dentro da linguagem

cores.append('roxo')
print(cores)          # OUTPUT: ['verde', 'amarelo', 'azul', 'branco', 'roxo']

# DEFINIDO a primeira função 

def diz_oi():
    print('oi!')

# CHAMANDO para execução 

diz_oi()             # Nunca esqueça de utilizar o () ao executar uma função

def cantar_parabens():
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas Felicidades")
    print("Muitos anos de vida!")  

cantar_parabens()


for n in range(5):
    cantar_parabens()

def vejo_uma_porta_abrir():


# FUNÇÕES COM RETORNO

numeros = [1, 2, 3]

ret_pop = numeros.pop()  # Vai tirar o último elemento de uma lista  e retorna ele

print(numeros)
print(ret_pop)  

# Em python, quando uma função não retorna nenhum valor é impresso "None"

def quadrado_de_sete():
    return 7*7           # FUNÇÕES PYTHON QUE RETORNAM COM A PALVRA "RETURN"

quadrado_de_sete()

print(f"Retorno: {quadrado_de_sete()}.")

# Aqui ele vau retornar o 49 que é o resultado daquela operação 


