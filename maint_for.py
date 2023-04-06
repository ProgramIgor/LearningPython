print("--------------------------------------")
print("Está pronto para o jogo da Advinhação?")
print("--------------------------------------")

secret_nm = 12
total_tentativas = 3


for rodada in range(1, total_tentativas + 1):
    print("Tentativa: {} / {}".format(rodada, total_tentativas))
    chute_str = input("Advinhe o número secreto entre 1 e 100:")
    print("Seu chute foi",chute_str)
    chute     = int(chute_str)

    if(chute < 1 or chute > 100):
        print('O número deve ser entre 1 e 100')
        continue

    acertou = chute == secret_nm
    maior   = chute > secret_nm

    if(acertou):
        print("Acertou, você é o mestre da advinhação!")
        break
    else:
        if(maior):
            print("Hoje suas habilidades de advinhação não desvendaram o número, é um pouco menos, tente novamente..")
        else:
            print("Hoje suas habilidades de advinhação não desvendaram o número, um pouco mais, tente novamente..")

print("Fim do Jogo")