aux1 = 0
aux2 = 1

escolhido = int(input('Escolha seu numero: '))
while aux2 < escolhido:
    aux3 = aux1 + aux2

    aux1 = aux2
    aux2 = aux3

if aux2 == escolhido: print('Pertence a sequencia de fibonacci')
else: print('Nao pertence a sequencia')