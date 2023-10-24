print("EXERCÍCIOS - SEÇÃO 8")

'''
S8Q2
Faça um função que receba a data atual (dia, mês, ano em inteiro) e exiba-a na tela no formato textual por extenso. Exemplo: data 01/01/2000 --> 01 de Janeiro de 2000.
'''

dia = int(input("INSIRA O DIA: "))
mes = int(input("INSIRA O MÊS: "))
ano = int(input("INSIRA O ANO: "))

def data_atual(dia: int, mes: int, ano: int):
    if mes == 1:
        return f"{dia} de Janeiro de {ano}"
    elif mes == 2:
        return f"{dia} de Fevereiro de {ano}"
    elif mes == 3:
        return f"{dia} de Marçode {ano}"
    elif mes == 4:
        return f"{dia} de Abril de {ano}"
    elif mes == 5:
        return f"{dia} de Maio de {ano}"
    elif mes == 6:
        return f"{dia} de Junho de {ano}"
    elif mes == 7:
        return f"{dia} de Julho de {ano}"
    elif mes == 8:
        return f"{dia} de Agosto de {ano}"
    elif mes == 9:
        return f"{dia} de Setembro de {ano}"
    elif mes == 10:
        return f"{dia} de Outubro de {ano}"
    elif mes == 11:
        return f"{dia} de Novembro de {ano}"
    return f"{dia} de Dezembro de {ano}"

print(data_atual(dia, mes, ano))    # Tem que chamar com os argumentos
