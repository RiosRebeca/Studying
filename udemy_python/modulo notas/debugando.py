print("Try/Except - Finally and Else")

'''
Dica de quando e onde tratar o código:

RODA ENTRADA DEVE SER TRATADA!

A FUNÇÃO DO USUÁRIO É DESTRUIR O SEU SISTEMA

O 'else' é executado somente se não ocorrer o o erro. Pra cada except que tivermos, podemos ter um 'else' porque se não entrar no except, ele vai para o else.

O 'finally' é sempre executado independente se houve erro ou não. Normalmente ele é usado para fechar ou desalocar recursos. As vezes vc abre a conexão com bancos de dados. Geralemte quando usa esse tipo de conexão, utiliza a leitura de dados e depois fecha essa conexão de dados. Então usamos ele PRA FECHAR A CONEXÃO COM BANCO DE DADOS OU ARQUIVO DE LEITURA.

'''

num = None              # pq se o usar n digitar correto, a vari n vai existir

try:
    num = int(input(f'Informe o número: '))
except ValueError:
    print('Valor Incorreto')
else:
    print(f'Você digitou {num}')

# Finally

try:
      num2 = int(input(f'Informe o número: '))
except ValueError:
    print('Você digitou um número inválido.')
else:
    print(f'Você  digitou o número {num2}')
finally:
    print('Executamos o finally.')

# EXEMPLO DE UMA FORMA ERRADA DE TRATAR

def dividir(a, b):
    return a/b

num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except Exception as seila:
    print('Valor Incorreto ', seila)

# COMO TRATAR DE FORMA CORRETA
# OBS: Você é responsável pelo código de suas funções, trate-as!

dividir2(a, b):
   try:
       return int(a)/int(b)
   except ValueError:              # dá pra passar uma tupla e iria funcionar
       return 'Valor incorreto'    # Em um único except:
   except ZeroDivisionError:       # (ValorError, ZeroDivisionError)
       return 'Não é possível realizar uma divisão por zero'

num3 = input('Informe o primeiro mnúmero: ')
num4 = input('Informe o segundo mnúmero: ')

print(dividir2(num3, num4))

# EXEMPLO DE FAGNER

def get():
    try:
        a = int(input("digite o valor: "))
        b = a-2
        return a, b
    except:
        main()

def dividir(a, b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        print("err: ", err)
        main()

def main():
    a, b = get()
    c = dividir(a,b)
    print(c)

main()



l para listar onde estamos no código 
n próxima linha
p imprime variável 
c continua a execução - finaliza o debugging

