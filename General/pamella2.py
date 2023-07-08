print("TESTANDO FÍSICA PARA PAMELLA")

nome = input('Qual o seu nome?') # a variável é igual a resposta
print(nome)                       # a resposta fica armazenada na variável e ela retorna em str

# Fórmula dea velocidade 

sf = int(input('Qual o espaço final em metros?'))
s0 = int(input('qual o espaço inicial em metros?'))
tf = int(input('qual o tempo final em segundos?'))
t0 = int(input('qual o tempo inicial em segundos?'))

vm = (sf - s0) / tf-t0

print(vm)