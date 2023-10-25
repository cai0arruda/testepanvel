def criptografia(mensagem, rotacoes):
    mensagem_cifrada = ""
    
    for caractere in mensagem:
        if caractere.isalpha():
            deslocamento = ord('a' if caractere.islower() else 'A')
            caractere_cifrado = chr((ord(caractere) - deslocamento + rotacoes) % 26 + deslocamento)
            mensagem_cifrada += caractere_cifrado
        else:
            mensagem_cifrada += caractere
    
    return mensagem_cifrada

mensagem = input("Digite a mensagem de texto: ")
rotacoes = int(input("Digite o número de rotações: "))

mensagem_cifrada = criptografia(mensagem, rotacoes)
print("Mensagem Cifrada:", mensagem_cifrada)
