#YOHEL PEREZ 98100658321

#1-2. 
def main():
    ''' funcion principal del programa'''
    archivo = open('mipagina.html' , 'a')
    archivo.write('<html></html>')


def headbody():
    archivo = open('mipagina.html' , 'a')
    archivo.seek(6)
    archivo.write('<head></head> <body> hola mundo yo soy YOHEL PEREZ 98100658321 </body> </html>')

main()
headbody()


#3.
def etiquetas():
    #pone negrilla a algunas palabras del archivo html
    lista = []
    archivo = open('mipagina.html' , 'r+')
    contenido = str(archivo.readlines())
    texto = str(contenido[contenido.find('body')+6: contenido.find('</body')])
    n = texto.count(' ')
    i = 0
    #print(texto)
    while i <= n-1:
        indice = texto.find(' ')
        lista += [texto[:indice]]
        texto = texto.strip(texto[:indice+1])
        i+= 1
        #print(texto)
    #print(contenido, lista)
    i = 1
    textof = contenido[2:contenido.find('body')+6]
    for palabra in lista:
        if i == 2 or i ==5 or i == 7:
            palabra = '<b>' + palabra + '</b> '
            textof += palabra
            i +=1
        else:
            textof += palabra + ' '
            i += 1
    textof += '</html>'
    archivo.close()
    archivo = open('mipagina.html' , 'w')
    archivo.write(textof)
    archivo.close()

#4
import random

texto = input('ingrese un texto')
textof= ' '
palabras = texto.split(' ')
print(palabras)
etiquetas = {1:('<b>', '</b>'), 3:('<u>', '</u>'), 2:('<mark>', '</mark>') }
tamaños ={1:('<h1>', '</h1>'), 2:('<h2>', '</h2>'), 3:('<h3>', '</h3'), 4:('<h4>', '</h4>'), 5: ('<h5>','</h5>'), 6:('<h6>' , '</h6>')}
i = 0
while i <=7:
    for palabra in palabras:
        tamaño = random.randint(1,6)
        etiqueta = random.randint(1,3)
        j = ''
        if palabra == palabras[-1]:
            j= '<br></br>'
        textof += ' ' + etiquetas[etiqueta][0] + tamaños[tamaño][0] + ' '+ palabra   + etiquetas[etiqueta][1] + tamaños[tamaño][1] + ' ' + j
    i +=1

archivo = open('mipagina.html', 'w')
archivo.write('<html> <head> <style type="text/css"> h1,h2, h3, h4, h5, h6 {display:inline;} </style> </head> <body>' + textof + '</body> </html>')
archivo.close()

print(textof)


#laboratorio ----------------------------------------------------

import random
def pbraCEtiqueta(etiqueta, pbraetiqueta):
    ''' recibe la etiqueta y la palabra con su etiqueta
    devuelve un string con la palabra con su etiqueta de cierre'''
    i = 1
    etiqueta = etiqueta.split('<')
    for elemento in etiqueta:
        if i != 1:
            pbraetiqueta += '</' + elemento
        else:
            i +=1
    return pbraetiqueta

def generadorCond1(contador, nombre, tipoCarta):
    '''recibe un contador, el nombre del cliente, y la carta dependiendo de su condicion
    crea una carta en un archivo tipo html con el nombre del cliente y con el texto correspondiente'''
    fiable = open('fiable' + str(contador) + '.html', 'w')
    fiable.write('<html><head><style type="text/css"> h1,h2, h3, h4, h5, h6 {display:inline;} </style> </head> <body> Medellin, Junio 6 del 2016 <br></br> <br></br> Sr.(a) <br></br> <b>' + nombre + '<br></br> <br></br>Asunto: </b> Agradecimiento <br></br><br></br>' + tipoCarta + '<br></br><br></br>Gracias por su atención, <br></br><b>Abarrotes Doña Carmelita </b> </body></html>')
    fiable.close()

#---------------------------------------------------------------------

dicClientes = {}
archClientes = open('clientes.txt', 'r')
i = 1
for linea in archClientes:
    if i != 1:
        e =linea.find( ' ')
        dicClientes[linea[:e]]= linea[e+1:]
    else:
        i += 1
#-----------------------------------------------
productos = open('productos.txt', 'r')
productosf = {}
i = 1
c= 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM'

for linea in productos:
    if i !=1:
        listaprov = linea.split(',')
        if listaprov[-2][0] not in c:
            descuento= int(listaprov[-1])
            vdescuento = (int(listaprov[-2])* descuento)/100
            productosf[listaprov[0]]= int(listaprov[-2])
        else:
            productosf[listaprov[0]]= int(listaprov[-1])
    else:
        i+= 1
productos.close()

#---------------------------------------------------------------
ventas = open('ventas.txt', 'r')
deudasClientes = {}
i = 1
for linea in ventas:
    if i != 1:
        listica = linea.split(' ')
        ID = listica[0]
        pto = listica[1]
        if ID not in deudasClientes:
            deudasClientes[ID]= productosf[pto]
        else:
            deudasClientes[ID] += productosf[pto]
    else:
        i+=1
ventas.close()

#-.-----------------------------------
archPagos = open('pagos.txt', 'r')
pagos = {}

i = 1
for linea in archPagos:
    if i != 1:
        listica = linea.split(' ')
        if listica[0] not in pagos:
            pagos[listica[0]]= float(listica[1])
        else:
            pagos[listica[0]]+= float(listica[1])
    else:
        i+=1
archPagos.close()

#dicClientes, diccionario key: ID cliente, dato: nombre
#deudasClientes, diccionario key: ID  cliente, dato: valor de su deuda
#pagos, diccionario  key:ID  cliente, dato:  valor que ha pagado
#productos f, diccionario key: ID producto, dato: costo del producto

#--------------------------------------------------------------------------------------
#1
IDdeudores = deudasClientes.keys()
infClientes ={}
tpago = 0
tdeuda = 0
cFiables = 0
cDeudores = 0
for key in deudasClientes:
    cliente = key
    deuda = deudasClientes[key]
    tdeuda+= deuda
    pago = pagos[key]
    tpago += pago
    diferencia = deuda - pago

    if diferencia <= 15000 or diferencia <= (deuda*10)/100:
        ans = 'fiable'
        cFiables += 1
    else:
        ans = 'deudor'
        cDeudores += 1
    infClientes[dicClientes[key]]= ans

bceCaja = tpago - tdeuda

if bceCaja <0:
    bceCaja = '<h2><b>Balance de caja: </b><mark>' + str(bceCaja)+ '</h2></mark></html>'
    print('opo')
else:
    bceCaja = '<h2><b>Balance de caja: ' + str(bceCaja) + '.</h2></html>'


infClientesO= sorted(infClientes)
info = '<b><h1> TIENDA DE ABARROTES DOÑA CARMELITA </b></h1> <br></br> <h3> Lista de clientes</h3><br></br>'
i = 1
for nombre in infClientesO:
    if 'deudor' in infClientes[nombre]:
        info += str(i) + '. <mark>' + nombre + '</mark>' + ' - <u> deudor</u>  <br></br>'
    else:
        info += str(i) + '. <b>' + nombre + '</b>' + ' - fiable <br></br>'
    i +=1

info += '<b> Clientes Fiables:</b> '+ str(cFiables) + '<br></br><b>Clientes Deudores:</b>' + str(cDeudores) + '<br></br>'+ bceCaja


#creacion de la pagina

pagina = open('paginaTienda', 'w')
pagina.write('<html> <head><style type="text/css"> h1,h2, h3, h4, h5, h6 {display:inline;} </style> </head> <body> ' + info)
pagina.close()

#2

#--------------------------------------------------------------------------------------
c1 =''
c2 = ''
c3 = ''
cartafiables =open('cartafibles.txt' , 'r')
cartafiables.readline()
#carta 1 pago completo
c1 += cartafiables.readline()
c1 += cartafiables.readline()
c1 += cartafiables.readline()


cartafiables.readline()
cartafiables.readline()
cartafiables.readline()
#carta 2 consumido - pagado <= 10%
c2 += cartafiables.readline()
c2 += cartafiables.readline()
c2 += cartafiables.readline()


cartafiables.readline()
cartafiables.readline()
cartafiables.readline()

#carta 3  debe <= 15000
c3 += cartafiables.readline()
c3 += cartafiables.readline()
c3 += cartafiables.readline()
cartafiables.close()

# carta 4 morosos
c4 = ''
cartaMorosos = open('morosos.txt', 'r')
c4 += cartaMorosos.readline()
c4 += cartaMorosos.readline()
cartaMorosos.close()

#carta 5 invitacion
c5 =''
invitacion = open('invitacion.txt', 'r')
c5 += invitacion.readline()
c5 += invitacion.readline()
invitacion.close()


#-------------------------------------------------------------------------------

palabrasClaves = open('palabrasclaves.txt', 'r') #abrir archivo de palabras claves, cada linea se convierte en una lista con split(' ') y se mete luego en una lista mas general
listaPbras = []
i = 1
for linea in palabrasClaves:
    if i != 1:
        linea = linea.strip('\n')
        i = linea.rfind(' ')
        linea= [linea[:i]] + [linea[i+1:]]
        listaPbras += [linea]
    else:
        i+=1

#----------------------------------------------------------------------------------



IDclientes = dicClientes.keys()
clientesInact = [] #diccionario con clientes inactivos
dicClientesFiabl1 =[] # diccionario key:valor deuda, dato: ID cliente
dicClientesFiabl2 ={} # diccionario key:valor deuda, dato: ID cliente
dicClientesFiabl3 ={} # diccionario key:valor deuda, dato: ID cliente
dicClientesDeud = {} #diccinoario key: valor deuda, dato: ID cliente
for key in IDclientes:
    cliente = key
    deuda = deudasClientes.get(key, 'no')
    pago = pagos.get(key , 'no')
    if  deuda== 'no':
        clientesInact += [key]
    elif deuda-pago == 0:
        dicClientesFiabl1 += [key]
    elif deuda - pago <= (deuda*10)/100:
        dicClientesFiabl2[deuda-pago]=key
    elif deuda - pago <= 15000:
        dicClientesFiabl3[deuda-pago]= key
    else:
        dicClientesDeud[deuda-pago]= key

#-------------------------------------------------------------------------------
#generación de cartas

#cartas inactivos:
contador = 1
if len(clientesInact) !=0:
    for cliente in clientesInact:
        i = random.randint(0, len(listaPbras)-1)
        pbraClave = listaPbras[i][0]
        while pbraClave not in c5:
            i = random.randint(0, len(listaPbras)-1)
            pbraClave = listaPbras[i][0]
        etiqueta = pbraClave[1]
        lengthetiqueta = len(etiqueta)
        palabra = pbraClave[0]
        pbraetiqueta = etiqueta + palabra
        pbraetiqueta = pbraCEtiqueta(etiqueta, pbraetiqueta)
        c5 = c5.replace(pbraClave[0], pbraetiqueta)
        inactivo = open('inactivo'+ str(contador)+'.html', 'a')
        inactivo.write('<html><head><style type="text/css"> h1,h2, h3, h4, h5, h6 {display:inline;} </style> </head> <body> Medellin, Junio 6 del 2016 <br></br> <br></br> Sr.(a) <br></br> <b>' + dicClientes[cliente]+ '<br></br> <br></br>Asunto: </b> invitación <br></br><br></br>' + c5 + '<br></br><br></br>Gracias por su atención, <br></br><b>Abarrotes Doña Carmelita </b> </body></html>')
        contador +=1
        if contador == 3:
            inactivo.close()
            break

#carta condicion 1 pago completo
contador = 0
#print(len(dicClientesFiabl1))
if len(dicClientesFiabl1) != 0:
    for cliente in dicClientesFiabl1:
        contador +=1
        i = random.randint(0, len(listaPbras)-1)
        pbraClave = listaPbras[i][0]
        while pbraClave not in c1:
            i = random.randint(0, len(listaPbras)-1)
            pbraClave = listaPbras[i][0]
        etiqueta = listaPbras[i][1]
        pbraetiqueta = etiqueta + pbraClave
        #print(pbraClave, etiqueta)
        pbraetiqueta = pbraCEtiqueta(etiqueta, pbraetiqueta)
        #print(pbraetiqueta)
        carta = c1
        carta= carta.replace(pbraClave, pbraetiqueta)
        generadorCond1(contador, dicClientes[cliente], carta)
        if contador == 3:
            break

#carta condicion 2 deuda -pagado <= 10%
if len(dicClientesFiabl2) !=0:
    fiablSort= sorted(dicClientesFiabl2)
    for pagocliente in fiablSort:
        contador +=1
        i = random.randint(0,len(listaPbras)-1)
        pbraClave = listaPbras[i][0]
        while pbraClave not in c2:
            i = random.randint(0,len(listaPbras)-1)
            pbraClave = listaPbras[i][0]
        etiqueta = listaPbras[i][1]
        pbraetiqueta = etiqueta + pbraClave
        pbraetiqueta = pbraCEtiqueta(etiqueta,pbraetiqueta)
        carta = c2
        carta = carta.replace(pbraClave, pbraetiqueta)
        generadorCond1(contador,dicClientes[dicClientesFiabl2[pagocliente]], carta)
        if contador == 6:
            break

#carta condicion 3 debe <= 15000
if len(dicClientesFiabl3) != 0:
    fiablSort = sorted(dicClientesFiabl3)
    for pagocliente in fiablSort:
        contador +=1
        i = random.randint(0, len(listaPbras)-1)
        pbraClave = listaPbras[i][0]
        while pbraClave not in c3:
            i = random.randint(0, len(listaPbras)-1)
            pbraClave = listaPbras[i][0]
        etiqueta = listaPbras[i][1]
        pbraetiqueta = etiqueta +pbraClave
        pbraetiqueta = pbraCEtiqueta(etiqueta, pbraetiqueta)
        carta = c3
        carta = carta.replace(pbraClave, pbraetiqueta)
        generadorCond1(contador, dicClientes[dicClientesFiabl3[pagocliente]], carta)
        if contador ==9:
            break
contador =0
#carta morosos
if len(dicClientesDeud) !=0:
    deudSort = sorted(dicClientesDeud)
    for pagocliente in deudSort:
        contador +=1
        i = random.randint(0, len(listaPbras)-1)
        pbraClave = listaPbras[i][0]
        while pbraClave not in c4:
            i = random.randint(0, len(listaPbras)-1)
            pbraClave = listaPbras[i][0]
        etiqueta = listaPbras[i][1]
        pbraetiqueta = etiqueta + pbraClave
        pbraetiqueta = pbraCEtiqueta(etiqueta,pbraetiqueta)
        carta = c4
        carta = carta.replace(pbraClave, pbraetiqueta)
        moroso = open('moroso' + str(contador) + '.html', 'w')
        moroso.write('<html><head><style type="text/css"> h1,h2, h3, h4, h5, h6 {display:inline;} </style> </head> <body> Medellin, Junio 6 del 2016 <br></br> <br></br> Sr.(a) <br></br> <b>' + dicClientes[dicClientesDeud[pagocliente]] + '<br></br> <br></br>Asunto: </b> Cobro por mora <br></br><br></br>' + carta + '<br></br><br></br>Gracias por su atención, <br></br><b>Abarrotes Doña Carmelita </b> </body></html>')
        moroso.close()
        if contador == 3:
            break



