"""
Este código foi exigido pelo professor Rondinelli, na qual ele CALCULE a média de notas
dadas pelo usuário e como saída, o programa deve mostrar a MAIOR NOTA, a MÉDIA e STATUS (aprovado ou reprovado)
 7 = aprovado 5 = reprovado 5-6 = recuperação

"""
# A FUNÇÃO FLOAT É PARA VALORES COM VÍGULA, COMO 7,4|2,2| ETC
nota_1 = float(input("Digite sua primera nota: "))
nota_2 = float(input("Digite sua segunda nota: "))
nota_max = 10 
media = (nota_1 + nota_2) / 2
print()
print(f'Sua média é: {media}')
print()

#AQUI DIZ AS CONDIÇÕES DO ALUNO SE ELE ESTÁ APROVADO OU NÃO
if media >= 7:
    print("Parabéns, você foi APROVADO!")
elif media >= 5 and media < 7:
    print("Você está de recuperação!")  
else:
    print("Você foi REPROVADO!")
    
#NESTE IF/ELSE, ELE MOSTRA QUAL FOI A MAIOR NOTA QUE O ALUNO TIROU
if nota_1 > nota_2:
    print(f'Sua maior nota foi, "{nota_1}"')
else:
    print(f'Sua maior nota foi, "{nota_2}"') 


















