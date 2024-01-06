#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

a=34

print(a)
# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

type(8.5)


# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

type(a)



# 4) Crear una variable que contenga tu nombre

# In[2]:

mi_nombre='deiby ibarra'


# 5) Crear una variable que contenga un número complejo

# In[3]:

n_complejo= 6+9j



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:


type=(n_complejo)


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi=3.1416
round(pi)

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

var1='True'
var2=True
#no ya que el que tiene comilla delimita cadenas

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(var1))
print(type(var2))


# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

c=3.4+7
print(c)

# 11) Realizar una operación de suma de números complejos

# In[2]:

g=8+5j
i=9+6j
print(g+i)

# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

u= a+1.09
print(c)


# 13) Realizar una operación de multiplicación

# In[5]:

print(4*9)


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

print(2**8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

h=27/4
print(h)


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

print(27//4)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

27%4



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

5*4+7



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

var4 = 'deiby'
var3 = 'alexander'

print(var4+var3)

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

"2"==2
#ocurre porque al estar encerrado en comilla delimita cadenas


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

2==int('2')



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

a = float('3,8')
# Convertir el string '3,8' a un número de punto flotante
a = float('3.8'.replace('.'))

# Imprimir el resultado
print(a)

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

numero=3
numero-=2
print(numero)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

1<<2
#esta operacion realiza un desplazamiento de bits a la izquierda por lo tante el numero binario 1 que es 0001 en notacion de 4 bits se desplaza
#dos posiciones a la izquierda lo que resulta en 0100

#el sistema de numeracion binario es un sistema numerico que utiliza solo dos digitos , 0 y 1. cada psicion en un numero binario representa la potencia de 2

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

2+'2'
#no esta permitido ya que involucra la suma de un numero entero con una cadena de texto. al intentar la suma un entero con una cadena se produce un error



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
numero=20
texto="el numero era el "

resultado=texto+str(numero)
print(resultado)