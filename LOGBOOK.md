#Refatoração do CRUD 13/11/2026

- (De tamanho = 50 eu mudei para TAMANHO = 50)
- No tamanho eu mudei eu mudei ele para maiúsculo, porque antes o 50 aparecia em 3 lugares e depois de mudar bastou apenas mudar uma linha para alterar a capacidade da lista.

- (De while i < tamanho and adicionado == False mudei para while i < TAMANHO and not adicionado, e if adicionado == True: virou if adicionado:. Isso foi feito com adicionado e encontrado também)
- O porquê disso é que esssas váriaveis já guardam um True ou False, então se a gente comparar com == True ou == False é mais código e menos eficaz, com o 'not' adicionado fica uma leitura tipo ' enquanto não foi adicionado'.

- (De i = i + 1 mudei para i += 1)
- O porquê é basicamente que fica de uma forma mais abreviada e tem a mesma função de  'i = i +  1', além de deixar o código mais "limpo".

-  
