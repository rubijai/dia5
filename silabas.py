'''


def obtener_vocales_espanol():
    vocales_con_tilde = ['á', 'é', 'í', 'ó', 'ú', 'ü']
    vocales_sin_tilde = ['a', 'e', 'i', 'o', 'u']

    vocales1 = vocales_con_tilde + vocales_sin_tilde
    vocales2 = [v.upper() for v in vocales_sin_tilde ] + [v.upper() for v in vocales_con_tilde ]
    vocales = vocales1 + vocales2

    return vocales

# Ejemplo de uso
vocales_espanol = obtener_vocales_espanol()
print(vocales_espanol)
'''

vocales = ['á', 'é', 'í', 'ó', 'ú', 'ü',
           'a', 'e', 'i', 'o', 'u',
           'A', 'E', 'I', 'O', 'U',
           'Á', 'É', 'Í', 'Ó', 'Ú', 'Ü']
print(vocales)

palabra = input(' Entre palabra que se quiere separar en sílabas (debe tener mas dos letras) : ')
print(f'palabra : {palabra}')
lista_letras_palabra = list(palabra)
print(lista_letras_palabra)
# Identificar si las letras son vocales o consonantes:
lista_vocales_consonantes = []
for letra in lista_letras_palabra:
    if letra in vocales:
        lista_vocales_consonantes.append('v')
    else:
        lista_vocales_consonantes.append('c')
print(lista_vocales_consonantes)
# listado de primeras tres letras
lista_1 = lista_vocales_consonantes[:3:]
lista_2 = lista_vocales_consonantes[:6:]
print(lista_1,lista_2)
silabas = []
def separar_silabas(lista_1,lista_2,lista_letras_palabra):
    if lista_1 == ['v', 'c', 'v']:
        silabas.append(lista_letras_palabra[0])
        lista_letras_palabra = lista_letras_palabra[1::]
        print(lista_letras_palabra)
        lista_1 = lista_vocales_consonantes[1::]
        if len(lista_1) == 2:
            silabas.append(lista_letras_palabra[0] + lista_letras_palabra[1])
        elif len(lista_1) == 3:
            silabas.append(lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2])

        else:
            if lista_1[:4:] == ['c', 'v', 'c', 'v']:
                print(lista_letras_palabra)
        return silabas, lista_letras_palabra, lista_1
    if lista_1 == ['c', 'v', 'c']:
        if lista_2 == ['c', 'v', 'c', 'c', 'c', 'c']:
            silabas.append(
                lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2] + lista_letras_palabra[3])
            lista_letras_palabra = lista_letras_palabra[5::]
            return silabas, lista_letras_palabra, lista_1
        elif lista_2 == ['c', 'v', 'c', 'c', 'c', 'v']:
            silabas.append(
                lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2] + lista_letras_palabra[
                    3])
            return silabas, lista_letras_palabra, lista_1
    if lista_1 == ['c', 'v', 'c']:
        if lista_2 == ['c', 'v', 'c', 'v', 'c', 'v']:
            silabas.append(lista_letras_palabra[0] + lista_letras_palabra[1])
            lista_letras_palabra = lista_letras_palabra[2::]
            return silabas, lista_letras_palabra, lista_1
        elif lista_2 == ['c', 'v', 'c', 'c', 'c', 'v']:
            silabas.append(
                lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2] + lista_letras_palabra[3])
            return silabas, lista_letras_palabra, lista_1
    if lista_1 == ['c', 'c', 'v']:
        if len(lista_letras_palabra) == 3:
            silabas.append(lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2])
            lista_letras_palabra = lista_letras_palabra[4::]
            return silabas, lista_letras_palabra, lista_1
        if len(lista_letras_palabra) == 4:
            silabas.append(
                lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2] + lista_letras_palabra[
                    3])
            lista_letras_palabra = lista_letras_palabra[4::]
            return silabas, lista_letras_palabra, lista_1
        if len(lista_letras_palabra) == 6 and lista_vocales_consonantes == ['c', 'c', 'v', 'c', 'c', 'v']:
            silabas.append(
                lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2] + lista_letras_palabra[
                    3])
            lista_letras_palabra = lista_letras_palabra[4::]
            return silabas, lista_letras_palabra, lista_1
        if lista_2 == ['c', 'c', 'v', 'c', 'c', 'v']:
            silabas.append(
                lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2] + lista_letras_palabra[3])
            lista_letras_palabra = lista_letras_palabra[5::]
            return silabas, lista_letras_palabra, lista_1
    if lista_1 == ['c', 'v', 'c']:
        if lista_2 == ['c', 'v', 'c', 'c', 'v', 'c']:
            silabas.append(lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2])
            lista_letras_palabra = lista_letras_palabra[4::]
            return silabas, lista_letras_palabra, lista_1
    if lista_1 == ['c', 'v', 'c']:
        if lista_2 == ['c', 'v', 'c', 'c', 'v', 'c']:
            silabas.append(lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2])
            lista_letras_palabra = lista_letras_palabra[4::]
            return silabas, lista_letras_palabra, lista_1


silabas, lista_letras_palabra, lista_1 = separar_silabas(lista_1,lista_2,lista_letras_palabra)
'''


print(lista_letras_palabra, lista_letras_palabra[0]+lista_letras_palabra[1])

silabas.append(lista_letras_palabra[0] + lista_letras_palabra[1])
print(silabas)

print(silabas)
print(len(lista_letras_palabra),silabas)
'''

if len(lista_letras_palabra) == 3:
    silabas.append(lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2])
if len(lista_letras_palabra) == 2:
    silabas.append(lista_letras_palabra[0] + lista_letras_palabra[1])
print(silabas)
'''

if lista_letras_palabra != []:
    print(lista_letras_palabra)
    if len(lista_letras_palabra) == 3:
        silabas.append(lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2])
    if len(lista_letras_palabra) == 2:
        silabas.append(lista_letras_palabra[0] + lista_letras_palabra[1])

separar_silabas(lista_1, lista_2, lista_letras_palabra)
print(silabas)
'''



'''
silabas = []
def separar_silabas(lista_vocales_consonantes,lista_letras_palabra):
    while lista_letras_palabra != []:
        print(len(lista_letras_palabra))
        lista_3vc = lista_vocales_consonantes[:3:]
        print(lista_3vc)
        if lista_3vc == ['v', 'c', 'v']:
            silabas.append(lista_letras_palabra[0])
            print(silabas)
            lista_letras_palabra = lista_letras_palabra[1::]
            lista_vocales_consonantes = lista_vocales_consonantes[1::]
            print(lista_letras_palabra)
            lista_3vc = lista_3vc[1::]
            print(lista_3vc)
        elif lista_3vc == ['v', 'c', 'c']:
            silaba = lista_letras_palabra[0] + lista_letras_palabra[1]
            silabas.append(silaba)
            print(silabas)
            lista_letras_palabra = lista_letras_palabra[2::]
            print(lista_letras_palabra)
            lista_3vc = lista_3vc[2::]
            print(lista_3vc)

        elif lista_3vc == ['c', 'v', 'c']:
            if len(lista_letras_palabra) == 3:
                silaba = lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2]
                silabas.append(silaba)
                print(silabas)
                lista_letras_palabra = lista_letras_palabra[3::]
                print(lista_letras_palabra)
                lista_3vc = lista_3vc[3::]
                print(lista_3vc)
            else:
                silaba = lista_letras_palabra[0] + lista_letras_palabra[1]
                silabas.append(silaba)
                print(silabas)
                lista_letras_palabra = lista_letras_palabra[2::]
                print(lista_letras_palabra)
                lista_3vc = lista_3vc[3::]
                print(lista_3vc)


        elif lista_3vc == ['c', 'v', 'c'] :
            silabas.append(lista_letras_palabra)
            lista_letras_palabra = []
            lista_3vc = []
        elif lista_3vc == ['c', 'v'] :
            silabas.append(lista_letras_palabra)
            lista_letras_palabra = []
            lista_3vc = []


    return f'{silabas} {lista_letras_palabra} {lista_3vc}'

silabas = []
def separar_silabas(lista_vocales_consonantes,lista_letras_palabra):
    while lista_letras_palabra != []:
        print(len(lista_letras_palabra))
        if len(lista_vocales_consonantes) > 5:
            lista_3vc = lista_vocales_consonantes[:5:]
            print(lista_3vc)
            #l = lista_3vc[:3:]
            #print(l)

        elif lista_3vc[:3:] == ['v', 'c', 'v']:
            print(lista_3vc)
            silabas.append(lista_letras_palabra[0])
            print(silabas)
            break
            lista_letras_palabra = lista_letras_palabra[1::]
            lista_vocales_consonantes = lista_vocales_consonantes[1::]
            print(lista_letras_palabra)
            lista_3vc = lista_3vc[1::]
            print(lista_3vc)

        elif lista_3vc[:2:] == ['v', 'c', 'c']:
            silaba = lista_letras_palabra[0] + lista_letras_palabra[1]
            silabas.append(silaba)
            print(silabas)
            lista_letras_palabra = lista_letras_palabra[2::]
            print(lista_letras_palabra)
            lista_3vc = lista_3vc[2::]
            print(lista_3vc)
            break
        elif lista_3vc[:2:] == ['c', 'v', 'c']:
            if len(lista_letras_palabra) == 3:
                silaba = lista_letras_palabra[0] + lista_letras_palabra[1] + lista_letras_palabra[2]
                silabas.append(silaba)
                print(silabas)
                lista_letras_palabra = lista_letras_palabra[3::]
                print(lista_letras_palabra)
                lista_3vc = lista_3vc[3::]
                print(lista_3vc)
            else:
                silaba = lista_letras_palabra[0] + lista_letras_palabra[1]
                silabas.append(silaba)
                print(silabas)
                lista_letras_palabra = lista_letras_palabra[2::]
                print(lista_letras_palabra)
                lista_3vc = lista_3vc[3::]
                print(lista_3vc)


        elif lista_3vc == ['c', 'v', 'c'] :
            silabas.append(lista_letras_palabra)
            lista_letras_palabra = []
            lista_3vc = []
        elif lista_3vc == ['c', 'v'] :
            silabas.append(lista_letras_palabra)
            lista_letras_palabra = []
            lista_3vc = []


    return f'{silabas} {lista_letras_palabra} '

print(separar_silabas(lista_vocales_consonantes,lista_letras_palabra))

'''
