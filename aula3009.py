animais = ['cachorro', 'gato', 'cavalo']
animais_permitidos = ['cachorro', 'gato', 'cavalo', 'girafa', 'mula', 'bode', 'jacare', 
                      'passaro', 'tigre', 'baleia', 'tubarão']

while True:
    if len(animais_permitidos) < 12:
        nome_animal = input("Digite o nome do animal: ")
    for posicao, item in enumerate(animais):
        print(posicao, item)
        posicao = 0
    for animais in animais_permitidos:
        print(posicao, item)
        posicao = posicao + 1 

        if nome_animal in animais_permitidos:
           animais += [nome_animal]
        else:
            print('Animal invalido')

        print(animais)
        
    else:
        print(animais)


    
        
