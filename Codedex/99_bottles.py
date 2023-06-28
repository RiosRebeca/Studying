print("99 bottles")

for b in range(101,0,-1):
  print(f'{b} bottles of beer on the wall\n    {b} bottles of beer\n    Take one down, pass it around\n    ')

#'for' é um loop que permite percorrer elementos em uma sequência (nesse caso, a sequência é o # range)
#o 'f' antes da string quer dizer 'formatted string', nesse caso podemos colocar o valor #armazenado em 'b' dentro da {} sem precisar converter em str para somar str + str

for o in range(100,0,-1):
  print(f'As {o}')
print("e busca-las foi.")

# É bom lembrar que range(start, stop, step) então eu vou começar com um n, terminar em outro e # colocar o intervalo -n, já que é uma contagem regressiva