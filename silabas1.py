'''


vocales_acentuadas = ['á', 'é', 'í', 'ó', 'ú', 'ü','Á', 'É', 'Í', 'Ó', 'Ú', 'Ü']
vocales_no_acentuadas = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U',]

#print(vocales)
palabra = input(' Entre palabra que se quiere separar en sílabas (debe tener mas dos letras) : ')
print(f'palabra : {palabra}')
lista_letras_palabra = list(palabra)
#print(lista_letras_palabra)
# Identificar si las letras son vocales o consonantes:
silabas = []
lista_vocales_consonantes = []
for letra in lista_letras_palabra:
    if letra in vocales_acentuadas:
        lista_vocales_consonantes.append('va')
    elif letra in vocales_no_acentuadas:
        lista_vocales_consonantes.append('vna')
    else:
        lista_vocales_consonantes.append('c')
print(lista_vocales_consonantes)
l1 = lista_letras_palabra.copy()
l2 = lista_vocales_consonantes.copy()
vocales = vocales_acentuadas.extend(vocales_no_acentuadas)
print(len(l1))
while len(l1) >= 4:
    n_l1 = l1[:4:]
    n_l2 = l2[:4:]
    if (len(n_l1) == 4) and ((n_l2 ==['vna', 'c', 'c', 'vna']) or (n_l2 ==['vna', 'c', 'c', 'va']) or (n_l2 ==['va', 'c', 'vna', 'c'])):
        silabas.append(l1[0])
    elif len(n_l1) == 4 and (n_l2 == ['c', 'vna', 'c', 'vna'] or  n_l2 == ['c', 'vna', 'c', 'va']):
        sil = n_l1[0] + n_l1[1]
        silabas.append(sil)
    elif len(l1) > 4:

        if (n_l2 == ['vna', 'c', 'c', 'vna'] or n_l2 == ['vna', 'c', 'c', 'va'] or n_l2 == ['va', 'c', 'vna', 'c']):
            silabas.append(n_l1[0])
        elif n_l2 == (['c', 'vna', 'c', 'vna'] or n_l2 == ['c', 'vna', 'c', 'va']):
            sil = n_l1[0] + n_l1[1]
            silabas.append(sil)
            print(silabas)
    while len(l1) <= 4:
        if len(l1) == 1 or len(l1) == 2:
            silabas.append(palabra)
        elif len(l1) == 3 and l2[0] == 'vna':
            silabas = [l1[0], l1[1] + l1[2]]
        elif len(l1) == 3 and l2[1] == 'va':
            silabas = [l1[0] + l1[1], l1[2]]
        elif len(l1) == 3 and l2[0] == 'c':
            silabas = [palabra]






print(silabas)


vocales_acentuadas = ['á', 'é', 'í', 'ó', 'ú', 'ü','Á', 'É', 'Í', 'Ó', 'Ú', 'Ü']
vocales_no_acentuadas = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U',]

Diptongos:

Un diptongo es la combinación de dos vocales en una misma sílaba. 
Puede ser la unión de una vocal cerrada átona (una vocal débil 
sin acento: i, u) seguida o precedida de una vocal abierta 
(una vocal fuerte o con acento: a, e, o), o dos vocales cerradas átonas juntas. 
Ejemplos:
cielo (cie-lo)
tierra (tie-rra)
aire (ai-re)
huevo (hue-vo)
Triptongos:

Un triptongo es la combinación de tres vocales en una misma sílaba. 
Suele ser la unión de una vocal cerrada átona (i, u) situada entre 
dos vocales abiertas (a, e, o). Ejemplos:
poesía (po-e-sí-a)
aéreo (a-é-re-o)
miau (miau)
Hiatos:

Un hiato se produce cuando hay dos vocales juntas, pero no forman 
diptongo o triptongo, es decir, no están en la misma sílaba. 
Puede ocurrir en varias situaciones:
Cuando una vocal cerrada tónica (á, é, í, ó, ú) lleva 
tilde y está seguida de otra vocal.
Cuando dos vocales abiertas (a, e, o) están juntas.
Ejemplos:
día (dí-a)
país (pa-ís)
poesía (po-e-sí-a)



Reglas de la separación de sílabas
Las reglas para separar sílabas tienen un principio básico:

en toda sílaba debe haber al menos una vocal.

Ese requisito es indispensable. En nuestro idioma no puede haber una 
sílaba únicamente con consonantes. Puede haber varias en una, pero 
tienen que estar presentes una o más vocales que funcionen como núcleo.

Con ese principio como base, el proceso de separar sílabas considera 
la posición de las vocales y de las consonantes dentro de la palabra. 
Según eso podemos encontrarnos con diferentes casos, cada uno con su propia regla:

Consonantes al inicio de una palabra

Todas las consonantes que se hallen al principio de una palabra 
deben ir sin excepción alguna con la vocal que les sigue:

Casa: ca – sa. En este caso la apalabra comienza con una sola consonante.
Plata: pla – ta. Aquí hay dos consonantes.
Conviene que aclaremos que cuando hablamos de separar en sílabas el 
inicio está de izquierda a derecha. Es contrario a cuando intentamos 
clasificar las palabras según la sílaba tónica, pues en ese caso se 
cuenta desde la derecha.

Consonantes al final de una palabra

Toda consonante que se encuentre al final de una palabra va junto a 
la vocal que la preceda. Aplica tanto cuando es una sola como cuando 
son varias consonantes:

Gavilán: ga – vi – lán.
Bíceps: bí – ceps.
Una consonante ubicada entre dos vocales

Si en la palabra hay una consonante entre dos vocales, debe ir 
acompañando a la que le sigue:

Elegir: e – le – gir.
Colina: co – li – na.
Zamuro: za – mu – ro.
Dos consonantes ubicadas entre dos vocales

En este caso la separación de sílabas dependerá del grupo específico 
de consonantes. Si son “pr”, “br”, “dr”, “cr”, “fr”, “gr”, “kr”, “tr”, “fl”, “pl”, “gl”, “kl”, “cl” o “bl”, 
se mantienen juntas en todo momento y van unidas a la vocal que les sigue:

Alegría: a – le – grí – a.
Ladrido: la – dri – do.
Cofradía: co – fra – dí – a.
Si no es ninguno de esos grupos, debemos separar las consonantes y asignar 
cada una a una vocal distinta:

Reactor: re – ac – tor.
Hipnotizado: hip – no – ti – za – do.
Otra posibilidad es la combinación “tl”. Hace falta comentarla, porque a veces 
genera confusión. Sucede que al separar en sílabas estas consonantes una persona 
puede tomar dos opciones, ambas válidas:

Atletismo: at – le – tis – mo. Esta separación es más común en España y en ciertas 
zonas de América. En su pronunciación estos hablantes separan la “t” de la “l”.
Atletismo: a – tle – tis – mo. Aquí podemos notar que no hay separación. La “t” y 
la “l” se mantienen juntas y acompañan a la vocal que las sigue. Esta opción es más 
común en la mayoría de los países hispanoamericanos.
Tres consonantes ubicadas entre dos vocales

En líneas generales, si tenemos tres consonantes seguidas entre dos vocales debemos 
dejar las dos primeras con la vocal anterior y la otra la unimos a la siguiente vocal:

Constancia: cons – tan – cia.
Sin embargo, hay una excepción. Si la penúltima consonante es
 “p”, “b”, “c”, “g”, “t”, o “d” y la última es “l” o “r”, q
 uedan unidas ambas y la primera consonante se deja con la vocal anterior:

Compraré: com – pra – ré.
Enclave: en – cla – ve.
Cuatro consonantes entre dos vocales

En este caso es muy sencillo. Las dos primeras consonantes van con 
la vocal anterior, mientras que las otras dos van con la siguiente:

Construcción: cons – truc – ción.
Obstrucción: obs – truc – ción.
Pero existen ciertos términos procedentes de lenguas extranjeras 
que se saltan esta norma. Por ejemplo, “ángstrom”: ángs – trom. 
En una situación como esta se deja juntas las primeras tres consonantes, 
siempre con la “s” de último.

Hay dos o más vocales seguidas

No podemos olvidarnos de los encuentros vocálicos, pues también son un caso muy 
importante. Ya explicamos una vez sus reglas de acentuación. Ahora nos 
centraremos en explicar cómo se debe separar en silabas cada uno.

Comencemos por el diptongo, que es el más común. Como sabemos, hay tres 
formas posibles en las que se puede presentar. En todas ellas deberemos conservar unidas las vocales:

Aurora: au – ro – ra.
Cuando: cuan – do.
Cuidado: cui – da – do.
En el caso del triptongo debemos proceder de la misma forma. Las tres 
vocales que constituyen este encuentro vocálico permanecen junta sin 
importar en qué posición de la palabra estén:

Opioide: o – pioi – de.
Actuáis: ac –  tuáis.
Con el hiato ocurre algo similar al diptongo, puesto que también tiene 
tres formas. No obstante, aquí las vocales siempre deben estar separadas:

Aéreo: a – é – re – o.
Peleé: pe – le – é.
Tranvía: tran – ví – a.
Dígrafos

Un último caso es cuando nos topamos con un dígrafo, es decir, dos consonantes 
unidas que anteriormente representaban una sola letra en el abecedario. 
En el español son “ch” y “ll”. Siempre deben ir juntas, sin importar 
en qué posición se encuentren:

Chantajear: chan – ta – je – ar.
Hallemos: ha – lle – mos.
Lo mismo sucede con “gu”, “qu” y “rr”.

Seguidor: se – gui – dor.
Queso: que – so.
Corromper: co – rrom – per.
Ejemplos de división de sílabas
Para ilustrar todas las reglas que tratamos, hemos juntado unos cuantos 
ejemplos. En ellos encontrarás cada uno de los casos:

Palabra	Separación de sílabas	Número de sílabas
Florentino.	Flo - ren - ti - no.	Tetrasílaba.
Mafia.	Ma - fia.	Bisílaba.
Campeonato.	Cam - pe - o - na - to.	Pentasílaba.
Barcelona.	Bar - ce - lo - na.	Tetrasílaba.
Historia.	His - to - ria.	Trisílaba.
Constipación.	Cons - ti - pa - ción.	Tetrasílaba.
Príncipes.	Prín - ci - pes.	Trisílaba.
Español.	Es - pa - ñol.	Trisílaba.
Fútbol.	Fút - bol.	Bisílaba.
Herramientas.	He - rra - mien - tas.	Tetrasílaba.
Cooperación.	Co - o - pe - ra - ción.	Pentasílaba.
Conquistas.	Con - quis - tas.	Trisílaba.
Complacer.	Com - pla - cer.	Trisílaba.
Planteamiento.	Plan - te - a - mien - to.	Pentasílaba.
Independencia.	In - de - pen - den - cia.	Pentasílaba.
Averiguáis.	A - ve - ri - guáis.	Tetrasílaba.
Productividad.	Pro - duc - ti - vi - dad.	Pentasílaba.
Regimiento.	Re - gi - mien - to.	Tetrasílaba.
Tecnología.	Tec - no - lo - gí - a.	Pentasílaba.
Diario.	Dia - rio.	Bisílaba.
Madrid.	Ma - drid.	Bisílaba.
Pasado.	Pa - sa - do.	Trisílaba.
Cenit.	Ce - nit.	Bisílaba.
Población.	Po - bla - ción.	Trisílaba.
Bonanza.	Bo - nan - za.	Trisílaba.
Imágenes.	I - má - ge - nes.	Tetrasílaba.
Regla.	Re - gla.	Bisílaba.
Constelación.	Cons - te - la - ción.	Tetrasílaba.
Títulos.	Tí - tu - los.	Trisílaba.
Paella.	Pa - e - lla.	Trisílaba.
Selector.	Se - lec - tor.	Trisílaba.
Cuarenta.	Cua - ren - ta.	Trisílaba.
Cosmología.	Cos - mo - lo - gí - a.	Pentasílaba.
Referencia.	Re - fe - ren - cia.	Tetrasílaba.
Vigía.	Vi - gí - a.	Trisílaba.
Francia.	Fran - cia.	Bisílaba.
Corresponsal.	Co - rres - pon - sal.	Tetrasílaba.
Juventud.	Ju - ven - tud.	Trisílaba.
Opinión.	O - pi - nión.	Trisílaba.
Bloqueo.	Blo - que - o.	Trisílaba.
Avalancha.	A - va - lan - cha.	Tetrasílaba.
Ventilador.	Ven - ti - la - dor.	Tetrasílaba.
Desplazamiento.	Des - pla - za - mien - to.	Pentasílaba.
Hallar.	Ha - llar.	Bisílaba.
Cosmos.	Cos - mos.	Bisílaba.
Periódico.	Pe - rió - di - co.	Tetrasílaba.
Igualdad.	I - gual - dad.	Trisílaba.
Plantación.	Plan - ta - ción.	Trisílaba.
Obstruyendo.	Obs - tru - yen - do.	Tetrasílaba.
Chile.	Chi - le.	Bisílaba.
Oraciones de separación silábica
Ya vimos palabras separadas en sus sílabas. Pasemos ahora a 
las oraciones (lógicamente, los monosílabos no llevan ninguna división):

Oración	Separación en sílabas
“A mi madre la internaron ayer”.	“A mi ma - dre la in - ter - na - ron a - yer”.
“En España hubo muchos linajes reales”.	“En Es - pa - ña hu - bo mu - chos li - na - jes re - a - les”.
“Alejandro prometió regresar con las municiones”.	
         “A - le - jan - dro pro - me - tió re - gre - sar con las mu - ni - cio - nes”.
“En la actualidad hay muchísimo desempleo”.	“En la ac - tua - li - dad hay mu - chí - si - mo de - sem - ple - o”.
“No hay nadie que pueda acompañarlo”.	“No hay na - die que pue - da a - com - pa - ñar - lo”.
“La nueva sociedad busca enmendar los antiguos errores”.	
           “La nue - va so - cie - dad bus - ca en - men - dar los an - ti - guos e - rro - res”.
“Los profesores merecen respeto”.	“Los pro - fe - so - res me - re - cen res - pe - to”.
“La hija de Jaime quiere ser doctora”.	“La hi - ja de Jai - me quie - re ser doc - to - ra”.
“En este psiquiátrico estuvo mi abuelo por veinte años”.	
“En es - te psi - quiá - tri - co es - tu - vo mi a - bue - lo por vein - te a - ños”.
“De la nada aparecieron cuarenta personas”.	“De la na - da a - pa - re - cie - ron cua - ren - ta per - so - nas”.
“La ética es vital para poder ser un buen profesional”.
	“La é - ti - ca es vi - tal pa - ra po - der ser un buen pro - fe - sio - nal”.
“Los reporteros consiguieron una exclusiva”.	
“Los re - por - te - ros con - si - guie - ron u - na ex - clu - si - va”.
“En este continente nunca hubo un buen explorador”.	
“En es - te con - ti - nen - te nun - ca hu - bo un buen ex - plo - ra - dor”.
“La estrategia del general no fue suficiente”.
	“La es - tra - te - gia del ge - ne - ral no fue su - fi - cien - te”.
“El arroz es uno de mis platillos favoritos”.	“El a - rroz es u - no de mis pla - ti - llos fa - vo - ri - tos”.
Ejercicios
Ya en este punto has visto todas las reglas para separar sílabas 
y muchos ejemplos. Por eso, es momento de que resuelvas unos ejercicios.
 
 Es sencillo: simplemente divide las palabras en sus sílabas según lo que has aprendido.

“Ella negó todas las acusaciones”.
“Sin educación no podemos avanzar como sociedad”.
“Las huelgas nunca sirvieron en ese país”.
“No vayas a comprarte una nueva lavadora sin haber conocido todos los modelos”.
“El acoso escolar ocurre en todas partes del mundo”.
“El asesino reveló la localización de cada cadáver.
“Ninguna persona puede entrar sin su autorización”.
“En mi trabajo ya no hay tantas personas como antes”.
“Queremos edificar una tienda de ropa”.
“Sus nuevos zapatos se estropearon antes de un mes”.
“Los doctores tuvieron dificultad para lograr retirar la bala alojada en su cuerpo”.
“No soy partidario de unas ideas tan extremistas”.
“La verdad nunca puede ser absoluta, según muchos filósofos”.
“Un asteroide de ese tamaño podría destruir más de un planeta”.
“Podríamos estar en desacuerdo en algo, pero nunca dejaría de apoyarte”.
“Su madre no asistió ese día”.
Respuestas

“E – lla ne – gó to – das las a – cu – sa – cio – nes”.
“Sin e – du – ca – ción no po – de – mos a – van – zar co – mo so – cie – dad”.
“Las huel – gas nun – ca sir – vie – ron en e – se pa – ís”.
“No va – yas a com – prar – te u – na nue – va la – va – do – ra sin ha – ber co – no – ci – do to – dos los mo – de – los”.
“El a – co – so es – co – lar o – cu – rre en to – das par – tes del mun – do”.
“El a – se – si – no re – ve – ló la lo – ca – li – za – ción de ca – da ca – dá – ver.
“Nin – gu – na per – so – na pue – de en – trar sin su au – to – ri – za – ción”.
“En mi tra – ba – jo ya no hay tan – tas per – so – nas co – mo an – tes”.
“Que – re – mos e – di – fi – car u – na tien – da de ro – pa”.
“Sus nue – vos za – pa – tos se es – tro – pe – a – ron an – tes de un mes”.
“Los doc – to – res tu – vie – ron di – fi – cul – tad pa – ra lo – grar re – ti – rar la ba – la a – lo – ja – da en su cuer – po”.
“No soy par – ti – da – rio de u – nas i – de – as tan ex – tre – mis – tas”.
“La ver – dad nun – ca pue – de ser ab – so – lu – ta, se – gún mu – chos fi – ló – so – fos”.
“Un as – te – roi – de de e – se ta – ma – ño po – drí – a des – truir más de un pla – ne – ta”.
“Po – drí – a – mos es – tar en de – sa – cuer – do en al – go, pe – ro nun – ca de – ja – rí – a de a – po – yar – te”.
“Su ma – dre no a – sis – tió e – se dí – a”.
Ahora sabes bien cómo debes separar en sílabas. Sin dudas, 
con este nuevo conocimiento podrás entender todas las normas de acentuación. 
¡Tan solo no te olvides de practicar mucho!
'''
import random as rn
def repartir_carta(cartas):
    carta = rn.choice(cartas)
    return carta
def puntos_jugador(cartas_jugador):
    s = sum(cartas_jugador)
    if s == 21 and len(cartas_jugador)== 2:
        p_jugador = 0
    elif s > 21 and 11 in cartas_jugador:
        p_jugador = s-10
    else:
        p_jugador = s
    return p_jugador

def puntos_computador(cartas_computador):
    s = sum(cartas_computador)
    if s == 21 and len(cartas_computador)== 2:
        p_computador = 0
    elif s > 21 and 11 in cartas_computador:
        p_computador = s-10
    else:
        p_computador = s
    return p_computador

    p_computador = sum(cartas_computador)
    return p_computador







def juego():
    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    cartas_jugador = []
    cartas_computador = []
    for i in range(2):
        cartas_jugador.append(repartir_carta(cartas))
        cartas_computador.append(repartir_carta(cartas))
    print(f' cartas_jugador : {cartas_jugador} p_jugador : {puntos_jugador(cartas_jugador)} ')
    print(f' carta computador : {cartas_computador[0]}')
    otra_carta = input( 'Desea otra carta? entre: si o no')
    jugar = True
    while jugar == True:
        if otra_carta == 'si':
            cartas_jugador.append(repartir_carta(cartas))
            print(f' cartas_jugador : {cartas_jugador} p_jugador : {puntos_jugador(cartas_jugador)} ')
            print(f' cartas_computador : {cartas_computador[0]}  ')
            otra_carta = input('Desea otra carta? entre: si o no')

        if otra_carta == 'no':
            p_computador = puntos_computador(cartas_computador)
            while p_computador != 0 and p_computador < 17:
                cartas_computador.append(repartir_carta(cartas))
                print(f' cartas_computador : {cartas_computador}  ')
            jugar = False

otro_juego = (input('JUGAR bLACKJACK : entre si o no'))
if otro_juego == 'si':
    juego()
