#!C:\Users\eurek\AppData\Local\Microsoft\WindowsApps\python3

#shebang n serve para windows, só p Linux e macOS se você não baixar  plataforma que roda

print("Desafio do Fagner")

# Desafio:

lista = ["agua", str(2), str(3.4), ["terra"], "casa", str(6), str(1235.56), "ar", str(777), str(666), str(999), str(3.14), "Fogo", "Shemhamphorasch"]

quantidade = sum(len(lista) for elemento in lista )
print(quantidade)

# Usando a lógica:

# 1- Eu tenho a variável 'lista', nela eu vou add os valores que estão dentro de [], no exemplo acima, o valor são diferentes elementos de diferentes classes - str, int e float.

# 2- Quando eu uso a função 'len', ele vai me dar o valor da quantidade de elementos dentro a lista. Nesse exemplo, o len() por si só irá retornar 14.

# 3- Só que eu uso o loop 'for' para percorrer cada caractere de cada elemento individualmente que está dentro (in) da minha variável.

# 4- Após essa ter os números int obtidos, a função sum() irá somar cada um dos caracteres e retornar a soma do valor dos caracteres de todos os elementos dentro da lista.

