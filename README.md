# Taller_2_Unu
# Foraneos.py
![image](https://user-images.githubusercontent.com/124726079/236866338-5d436781-8f3e-4ed7-800e-5b8bc86a9f14.png)
## *Punto 1*:dog:
- Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.
```ruby
#punto 1
#1
x= int(input("Ingresa un número entero: ")) #pido x
partes = str(x) #la vuelvo un caracter
digitos=[] #hago un arreglo para meter dentro los digitos
for i in partes: #recorro el caracter
    digitos.append(i) #los meto en el arreglo
print(digitos) #printeo el arreglo

```

## *Punto 2* :cat:
- Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entrege los digitos tanto de la parte entera como de la decimal.
```ruby
#punto 2
#2
def partedecimal(x,y):
    return x-y #la diferencia entre el valor y su entero
x=float(input("ingresar un flotante: ")) #pido x
y=int(x) #lo vuelvo entero
print("El " + str(x) + " tiene parte entera de " + str(y)+ " y la parte decimal es " +  str(partedecimal(x,y))) #printeo ambas partes

```

## *Punto 3* :tiger:
- Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos.

```ruby
#punto 3
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

```


## *Punto 4* :koala:
- Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Con cuántos valores de la serie, se tienen errores del 10%, 1%, 0.1% y 0.001%.
```ruby
#punto 4
#4
import math # Importo math y hago def
def coseno(x):
    return  math.cos(x) 
def factorial(n : int ):
    p = 1
    for i in range(1,n+1):
        p *= i
    return p
def seriemcpollo(x,n):
    m=0
    for i in range(n+1):
        m += ((-1)**i)*(x**((2*i)))/(factorial((2*i)))
    return m     # Hago una funcion con la definicion

x=float(input("ingresar x: ")) #ingresar x
n=int(input("ingresar cantidad de las serie de Maclaurin : ")) # la cantidad de la serie que se usan 
print(coseno(x))
print(seriemcpollo(x,n)) #printeo ambas funciones


```

## *Punto 5* :penguin:
- Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde la perpectiva iterativa como recursiva.

```ruby
#punto 5
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

```
## *Punto 6* :frog:
- Desarrollar un programa que determine si en una lista no existen elementos repetidos.

```ruby
#punto6
def orden(a):
    a.sort()
    return a #ordeno el arreglo
def dolly(a):
    a=orden(a)
    s = True
    x = 0
    y = 1 #hago un contador
    while x<len(a) and y<len(a): # recorro el arreglo y lo comparo
        if a[x]==a[y]:
            s = False
            x += 1
            y += 1
        else:
            x +=1
            y +=1
    if s == True:
        return "no hay elementos repetidos" #si no cambia no hay elementos repetidos
    else:            
        return "hay elementos repetidos" #si retorna false es que no hay
a=[int(x) for x in input("Ingrese los numeros del arreglo separados por comas: ").split(',')] #pido el arreglo
saberrepet=dolly(a)
print(a)
print(dolly(a)) #imprimo el resultado
```
## *Punto 7* :whale:
- Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

```ruby
#punto7

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

```
## *Punto 8* :water_buffalo:
- Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista

```ruby
#punto8 :turtle:
#8
def comparar(A,B): 
    C=[]
    for i in A:
        if i in B:
            C.append(i) #se recorre A y si esa i esta en B se pone en el otro arreglo
    return C
C=[]    
A=[]
A = input("Ingrese los elementos del arreglo 1: ").split(",")
B=[]
B = input("Ingrese los elementos del arreglo 2: ").split(",") #pido los dos arreglos
print("los elementos repetidos son  ",comparar(A,B)) #imprimo el arreglo que se crea


```
## *Punto 9*  :honeybee:
- Resolver el punto 7 del taller 1 usando operaciones con vectores.

```ruby
#punto9
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

```
## *Punto 10* 
#10
n = int(input("Ingrese el tamaño de la matriz: "))
A = [] #se pide un numero y se hace un arreglo
for i in range(n):
    B = []
    for j in range(n):
        elemento = int(input(f"Ingrese el elemento ({i+1},{j+1}): "))
        B.append(elemento)
    A.append(B)
    s = 0
for i in range(n):
    s (A[0][i])
#vemos la suma de las diagonales, filas y columnas
e = True
for i in range(n):
    suma1 = 0
    for j in range(n):
        suma1 += A[i][j]
    if suma1 != s:
        e = False
        break
    suma2 = 0
    for j in range(n):
        suma2 += A[j][i]
    if suma2 != s:
        e = False
        break
    y = 0
    for j in range(n):
        if i == j:
            y += A[i][j]
    if y != s:
        e = False
        break
    suma3 = 0
    for j in range(n):
        if i + j == n - 1:
            suma3 += A[i][j]
    if suma3 != s:
        e = False
        break
#imprimo el resultado
if e:
    print("La matriz es mágica")
else:
    print("La matriz no es mágica")


```ruby
#punto10 :elephant:
- Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.

```
#### *Eso es todo por hoy :D* _-Duva-_ LauDeLaRosa :sunflower: :tulip:
