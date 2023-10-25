def teste():
    rex = int(input("Digite a posição de REX: "))
    bob = int(input("Digite a posição de BOB: "))
    oli = int(input("Digite a posição de OLI: "))

    if rex == bob and bob == oli:
        return "Oli conseguirá fugir"
    if rex > bob and rex < oli:
        return "Rex pegará o gato"
    elif bob > rex and bob < oli:
        return "Bob pegará o gato"
   
vencedor = teste()
print(vencedor)