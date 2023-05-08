#1
x= int(input("Ingresa un número entero: ")) #pido x
partes = str(x) #la vuelvo un caracter
digitos=[] #hago un arreglo para meter dentro los digitos
for i in partes: #recorro el caracter
    digitos.append(i) #los meto en el arreglo
print(digitos) #printeo el arreglo

#3
def comparar(x,y):
    if len(str(x))!=len(str(y)): #comparo la longitud de los digitos para ver que sean iguales
        return "No puede ser espejo porque no miden lo mismo bro"
    else:
        for i in range(len(str(y))): #recorro y
            if str(x)[i] == str(y)[len(str(y))-1-i]: #los comparo
                return "si son espejos"
            else:
                return "no son espejos"        
x=int(input("ingresar numero 1: ")) #pido las variables
y=int(input("ingresar numero 2: "))
print(comparar(x,y)) #printeo la respuesta

#5
def mcd(a,b): #busco el mcd
    if b>a:
        return mcd(b,a)
    elif a%b!=0:
        return mcd(b,a%b)
    return b #retorno el valor
def mcm(a,b):
    return (a*b)/mcd(a,b) # Busco el mcm con el mcd
x = int(input("numero 1 : "))
y = int(input("numero 2 : ")) #pido los dos valores
z = mcm(x,y)
print(z) #imprimo z

#7
def vocalitas(A): #Se define la funcion
    B = [] #Se crea un arreglo
    for A in A: # se recorre el arreglo en si mismo
        s = 0 # se hace un contador
        for i in A:
            if i.lower() in "aeiouáéíóú": # se buscan las vocales
                s += 1
                if s >= 2:
                    B.append(A) #las que tengan dos o mas se unen a un arreglo
                    break
    if B:
        return B
    else:
        return "No existe"
A=[]
A = input("Pon elementos del arreglo separados por coma: ").split(",") #se pide el arreglo
print("los elementos con 2 o mas vocales son ",  vocalitas(A)) #se retorna A
 #9
n1 = float(input("Ingresar número 1: "))
n2 = float(input("Ingresar número 2: "))
n3 = float(input("Ingresar número 3: "))
n4 = float(input("Ingresar número 4: "))
n5 = float(input("Ingresar número 5: ")) # se piden 5 numeros
numeros = [n1, n2, n3 , n4 , n5] #se meten al arreglo
menorMayor = sorted(numeros)
mayorMenor = sorted(numeros, reverse=True) #se ordenan de manera ascendente y descendente 
promedio = (n1+n2+n3+n4+n5)/5 #se sacas el promedio
if len(numeros) % 2 == 0:
    mediana = (numeros[len(numeros)//2] + numeros[len(numeros)//2 - 1]) / 2 #se saca la mediana
else:
    mediana = numeros[len(numeros)//2]
pmultiplicativo = (n1 * n2* n3 * n4 * n5)**0.2
peque = min(numeros)
grande = max(numeros)
raiz = peque**1/3
potencia = grande**peque
print("el promedio aritmetico es  " + str(promedio))
print("el promedio multiplicativo es " + str(pmultiplicativo))
print("la mediana es " + str(mediana))
print("de menor a mayor son " + str(menorMayor))
print("de menor a mayor son " + str(mayorMenor))
print("el mayor elevado al menor es " + str(potencia))
print("la raiz cubica del menor es " + str(raiz)) #se imprimen todas las funciones