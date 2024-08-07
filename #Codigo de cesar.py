#Codigo de cesar

texto = input('Digite a mensagem para ser criptografada : ')

chave = 3
modo = 1
CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
convertido = ''
texto2 = texto.upper()


for caractere in texto2:
    if caractere in CARACTERES:
        num = CARACTERES.find(caractere)
        if modo == 1:
            num = num + chave
        else:
            print(error)


        if num >= len(CARACTERES):
            num = num - len(CARACTERES)
        elif num < 0:
            num = num + len(CARACTERES)

        convertido = convertido + CARACTERES[num]
    else:

        convertido = convertido + caractere




if modo == 1:
    print("O texto original é :", texto)
    print('O texto modificado é:', convertido)
else:
    print('error')