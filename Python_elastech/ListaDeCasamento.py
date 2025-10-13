print("LISTA DE CASAMENTO")

convidados = ("Rebeca", "Rosa", "Fagner", "Raí", "José", "Mateus")

nome = input("DIGITE SEU NOME: ")
for i in convidados:
    if i == nome:
        print(f"Bem-vindo {nome}")
    else:
        print(f"Você não foi convidado, {nome}.")
        break
        
