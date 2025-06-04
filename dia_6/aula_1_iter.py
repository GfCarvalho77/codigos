frutas=['banana','pera','uva','abacaxi','mamão','laranja','bergamota']

for fruta in frutas:
    print(f"Gosto de {fruta}")

for fruta in range(len(frutas)):
    print(f"No índice {fruta} está {frutas[fruta]}")

for idx, fruta in enumerate(frutas):
    print(f"No índice {idx} está {fruta}")