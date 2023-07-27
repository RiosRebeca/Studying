gaveta = [ 'blusa', 'vestido', 'sapato', 'blusa', 'short', 'saia', 'bota', 'meia', 'calça', 'blusa']

if 'blusa' in gaveta:
    print("Encontrei blusa na gaveta.")
else:
    print("Não encontrei nenhuma blusa na gaveta.")

# Esse só verifica se tem o valor, mas não tem dizendo se se repete e quantas vezes


carrinho = []

for escolha in range(10):
    itens = input("Escolha um ítem: ")
    carrinho.append(itens)

print(carrinho)