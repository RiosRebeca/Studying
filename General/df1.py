#!/usr/eurek/Documents/Studying/General/bin/python3 

#shebang n serve para windows, só p Linux e macOS

print("Desafio do Fagner")

# Desafio:

lista = ["agua", str(2), str(3.4), ["terra"], "casa", str(6), str(1235.56), "ar", str(777), str(666), str(999), str(3.14), "Fogo", "Shemhamphorasch"]

quantidade = sum(len(lista) for elemento in lista )
print(quantidade)
