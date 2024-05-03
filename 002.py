total = int(input("quantos giros o jogador realizou?"))

if total >= 502: 
    print("não é possivel realizar tantos giros simultaneamente!")
elif total >= 2 and total <= 30:
    print("item comum")
elif total >= 31 and total <= 70:
    print("item incomun")
elif total >= 71 and total <=90:
    print("item raro")
elif total >= 91 and total <= 120:
    print("item ultra raro")
elif total >= 121 and total <= 150:
    print("item épico")
elif total >= 151 and total <= 170:
    print("item ultra épico")
elif total >= 171 and total <= 222:
    print("ITEM LENDÁRIO")
elif total >= 223 and total <= 322:
    print("item mítico")
elif total >=323 and total <= 499:
    print("ITEM ÚNICO")
elif total ==500 or total == 501:
    print("você voltou a girar itens comuns!")
elif total >= 1 and not total == 2:
    print("item de inicio de jogo")
else:
    print("sem itens")