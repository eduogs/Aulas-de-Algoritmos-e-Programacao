# Alunos Eduardo  Oliveira e Gabriel Gusmão
# 1- A > B

a = float(input("DIGITE A: "))
b = float(input("DIGITE B: "))
    
if a > b:
    print(f'{a}, é maior que {b}')
    print('A é maior do que B')
elif a < b:
    print(f'{b}, é maior que {a}')
    print('B é maior do que A')
else:
    print(f'{a} é igual a {b}')
    print('A é igual a B')


#2- X > 10 AND Y <= 4

x = float(input("DIGITE X: "))
y = float(input("DIGITE Y: "))

if x > 10 and y <= 4:
    print("As condições X > 10 AND Y <= 4 são atendidas.")
else:
    print("As condições X > 10 AND Y <= 4 não são atendidas.")


#3- TEMPERATURA >= 30°

temperatura = float(input('Digite quantos a TEMPERATURA que está agora: '))

if temperatura >= 30:
    print('É, hoje está quente')

else:( 'Hoje não está quente' )

