print (str (10/3))
#Phyton suele poner todos los decimales, hay que redondear por lo tanto...

resultado= 10/3
print(f"{resultado: .2f}")
print (f"{resultado: .0%}")


#2f sirve para hacer un redondeo si es sobre 6, si es 5 y segundo decimal no redondea el 5


edad=18

if edad >=18:
    print ("Eres mayor de edad")
else: 
    print ("Eres menor de edad")

# Soliciten 2 numeros y verifiquen si es mayor el a o el b 

numero1= int(input("Ingrese el primer número: "))
numero2= int(input("ingrese el segundo número: "))

if numero1 > numero2:
    print ("El primer numero es el mayor" + str(numero1))  
elif numero1 == numero2: 
    print("los dos numeros son iguales")
else:
    print ("El segundo numero es mayor que el primero")


# Input siempre debe tener sus parentesis al lado de la palabra. 
# Int siempre se utiliza para poner una variable que es texto convertida en numero 
#Como en el ejercicio anteriormente visto. 
#Elif es una variable intermedia que nos sirve por si los números son nuevos. 
# El == es una pregunta, por ejemplo "=2 == 4 entonces eso significa, 2 es igual igual a 4?"