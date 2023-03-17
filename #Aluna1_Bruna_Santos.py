#Aluna1_Bruna_Santos
#Aluna2_Emeliely_Vieira

#Jogo do código secreto

while True:    
    #Descobrindo o código secreto
    print("REGRAS PARA O CÓDIGO SECRETO:")
    print(" ")
    print("1 - Deverá ter apenas 4 vogais (a,e,i,o);\n2 - Poderá ser escrito em qualquer ordem;\n3 - Não será aceito repetição de vogal. ")
    jogadas = 0
    print("Digite o seu código com apenas 4 vogais: ",end ="")
    codigo = input()

    #Validando as vogais do código escolhido
    vogais_possiveis = ["a","e","i","o"]
    tem_vogais_possiveis = True

    for vogal in codigo: #Validando o código
        if vogal not in vogais_possiveis:
            tem_vogais_possiveis = False
            
    if tem_vogais_possiveis:
        print("\n"*100)
        print("Seu código foi escondido!")
    else:
        print("Código inválido!! Só pode usar as vogais a,e,i,o.")

    #COMEÇANDO O JOGO
    print("")
    print("COMEÇANDO O JOGO")
    print("")
    #Tentativas para adivinhar o código
    tentativa = 0
    letras_certas = 0
    continuar = "s"
    while True:  
        tentativa += 1 #O número de tentativas é incrementado no programa
        jogadas += 1
        print("Tentativa {}:".format(tentativa))  #O número da tentativa é exibida
        tentativa_jogador = input()  #O jogador digita a tentativa
        if tentativa_jogador == codigo:  #Se a tentativa é igual ao código
            print('Ganhou!')  #O jogador acertou a tentativa
            print("O número de tentativas é:", tentativa)
            continuar = input("Deseja jogar novamente? Digite s para sim e n para não: ")#Descobrindo se o jogador deseja jogar novamente ou encerrar o programa
            if continuar == "n": 
                print("O maior número de jogadas para a vitória é:",jogadas)
                break #Sair do loop do jogo
            elif continuar == "s":
                break #Sair do loop do jogo e retornar ao início do programa
        else:
            print("Tente novamente!")
        letras_certas = 0 #Reiniciar o contador de letras certas para a próxima tentativa
        for i in range(len(codigo)):#Descobrindo a quantidade de letras certas que o jogador acertou
            if codigo[i] == tentativa_jogador[i]:
                letras_certas += 1
        print("Acertou",letras_certas,"nas posições corretas.")
    if continuar == "n":
        break #Sair do loop do programa e encerrar o programa