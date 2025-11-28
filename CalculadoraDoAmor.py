print("Calculadora do Amor")
print("<3 <3 <3 <3 <3")

nome1 = input("Digite o nome da 1ª pessoa: ")
nome2 = input("Digite o nome da 2ª pessoa: ")


nomes = nome1.lower() + nome2.lower()

placar = 0

for char in nomes:
    if char in "aeiou":
        placar += 5
    

    if char in "amor":
        placar += 10

print("\nSeu placar de compatibilidade:", placar)


if placar < 10:
    print("Nunca vai dar certo!")
elif placar < 50:
    print("Talvez com muito esforço!")
elif placar < 100:
    print("Vocês formam um belo casal!")
else:
    print("Vocês terão um relacionamento muito bom! <3")
