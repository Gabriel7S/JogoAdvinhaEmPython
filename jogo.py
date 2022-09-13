import advinhacoes
import forca



print("*********************")
print("Escolha seu jogo !")
print("*********************")
print("(1) Forca ou (2) Advinhação")
print("*********************")
jogo = int(input("Qual jogo ?"))
if(jogo ==1):
        print("Você escolheu Jogo da Forca")
        forca.jogar()
elif( jogo == 2):
        print(" Você escolheu Jogo de advinhação")
        advinhacoes.jogar()
