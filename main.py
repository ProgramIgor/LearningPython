print("--------------------------------------")
print("Está pronto para o jogo da Advinhação?")
print("--------------------------------------")

secret_nm = 12
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
    print("Tentativa: {} / {}".format(rodada, total_tentativas))
    chute_str = input("Advinhe o número secreto:")
    print("Seu chute foi",chute_str)
    chute     = int(chute_str)

    acertou = chute == secret_nm
    maior   = chute > secret_nm

    if(acertou):
        print("Acertou, você é o mestre da advinhação!")
    else:
        if(maior):
            print("Hoje suas habilidades de advinhação não desvendaram o número, é um pouco menos, tente novamente..")
        else:
            print("Hoje suas habilidades de advinhação não desvendaram o número, um pouco mais, tente novamente..")

    rodada = rodada + 1

print("Game Over")