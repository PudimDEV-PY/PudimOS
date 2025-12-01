import time
print("--------------------------------------------------------------------------------------------------------------")
time.sleep(1)
print("Seja-bem vindo ao PudimOS DEBUG")
print("Para começar, crie um usario!")
print("--------------------------------------------------------------------------------------------------------------")
time.sleep(2)
User = input("Qual e o nome do usario? : ")
time.sleep(1)
Senha = input("Qual e a senha? : ")
time.sleep(1)
Tipo = input("Tipo do user Sudo/User? : ")
time.sleep(1)
print("--------------------------------------------------------------------------------------------------------------")
print(f"O seu nome e {User}")
print(f"O sua senha e {Senha}")
print(f"O seu Tipo e {Tipo}")
print("--------------------------------------------------------------------------------------------------------------")
print("Start PudimOS......")
time.sleep(1)
print("(0   )")

time.sleep(0.5)
print("(00  )")
time.sleep(0.5)

print("(000 )")
time.sleep(0.5)

print("(0000)")
time.sleep(1)

print("--------------------------------------------------------------------------------------------------------------")
print(f"               _.-;;-._             tipo: {Tipo}    ")
print(f"        '-..-'|   ||   |            User: {User}   ")
print(f"        '-..-'|_.-;;-._|            Sistem : PudimOS  ")
print(f"        '-..-'|   ||   |            By: PudimDEV  ")
print(f"        '-..-'|_.-''-._|            Logo: jgs  ")
print("--------------------------------------------------------------------------------------------------------------")
time.sleep(3)
menu = r"""
             ________________________________________________              
            /                                                \             
           |    _________________________________________     |            
           |   | PudimOS                                 |    |            
           |   | ========================================|    |            
           |   | Para abrir o app em abixo escreva o nome|    |            
           |   | Dele                                    |    |            
           |   |=========================================|    |            
           |   |  [Calc] [PPT]                           |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |                                         |    |            
           |   |_________________________________________|    |            
           |                                                  |            
            \_________________________________________________/            
                   \___________________________________/                   
                ___________________________________________                
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_             
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_          
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_       
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_    
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_ 
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
                                                              
"""

print(menu)

# Calc

import time
import random

while True:
    EXE = input("[Executar algum app?] : ")

    # =============================== CALCULADORA ===============================
    if EXE == "Calc":
        print("Seja bem-vindo ao calc")
        time.sleep(1)

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        soma = num1 + num2
        sub = num1 - num2

        print("\nResultados:")
        print(f"{num1} + {num2} = {soma}")
        print(f"{num1} - {num2} = {sub}")

        time.sleep(1)
        print("saindo em 3..")
        time.sleep(1)
        print("saindo em 2..")
        time.sleep(1)
        print("saindo em 1..")
        time.sleep(1)
        print(menu)

    # ======================== PEDRA PAPEL TESOURA (PPT) =========================
    elif EXE == "PPT":
        print("Bem-vindo ao Pedra, Papel e Tesoura!")
        time.sleep(1)

        escolhas = ["pedra", "papel", "tesoura"]

        jogador = input("Escolha (pedra/papel/tesoura): ").lower()
        pc = random.choice(escolhas)

        print(f"Você escolheu: {jogador}")
        print(f"O computador escolheu: {pc}")

        if jogador == pc:
            print("Empate!")
        elif (jogador == "pedra" and pc == "tesoura") or \
             (jogador == "papel" and pc == "pedra") or \
             (jogador == "tesoura" and pc == "papel"):
            print("Você venceu!")
        else:
            print("Você perdeu!")

        time.sleep(3)
        print(menu)

    # ========================== ERRO / TENTAR DE NOVO ==========================
    else:
        print("App inválido! Tente novamente.\n")
        continue  # volta pro menu


     
     
     
     
     
     



















time.sleep(3)
exit

