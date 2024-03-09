# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 
# 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme 
# o exemplo abaixo:

def ln(x):
    print("-"*x)

ln(30)
print("Gerador de tabuada")
ln(30)

nrTab = int(input("Qual tabuada deseija gerar? Escolha um número de 1 a 10: "))

for i in range(10):
    print(f"{i+1} x {nrTab} = {(i+1)*nrTab}")