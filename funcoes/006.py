'''
Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. 
A palavra secreta será representada por espaços em branco, um para cada letra da palavra.
O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra.
Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes.
Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada.
Após um número máximo de erros, o jogador perde.
O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse exercício.
'''

import random

palavras_secretas = ['gato', 'cachorro', 'papagaio', 'galinha', 'elefante', 'zebra']
palavra_secreta = random.choice(palavras_secretas)
tentativas_maximas = 6
letras_acertadas = ["_"] * len(palavra_secreta)
print(" ".join(letras_acertadas))

while True:
    letra = input("\nDigite uma letra: ").lower()

    if letra not in palavra_secreta:
        tentativas_maximas -= 1
        print(f"Letra incorreta. Tentativas restantes: {tentativas_maximas}")   
    else:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_acertadas[i] = letra

        print(" ".join(letras_acertadas))
    if "_" not in letras_acertadas:
        print(f"Parabéns! Você acertou a palavra: {palavra_secreta}")
        break
    if tentativas_maximas == 0:
        print(f"Você perdeu! A palavra era {palavra_secreta}.")
        break
