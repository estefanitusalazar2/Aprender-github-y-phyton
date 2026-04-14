Print ("hola mundo")

print ("hola mundo 2")
Print ("hola mundo 3")
print ("hola mundo 4")




#Ingresando el lower
nombre = "Estefania"

# PROPIEDADES DEL str
print(nombre)

# Mayúscula
print(nombre.upper())

# Minúscula 
print(nombre.lower())

# El largo
print(len(nombre))

# La primera letra
print(nombre[0])

# La última letra
print(nombre[-1])

# Las primeras 3 letras
print(nombre[0] + nombre[1] + nombre[2])
print(nombre[0:3])



#print (nombre [1:3])
print(nombre[1:3])
# #print(nombre[3:3])
print(nombre[3:3])

#Solicitar el nombre, apellido, edad
nombre = input("Ingrese su nombre: ").lower()
apellido = input("Ingrese su apellido: ").lower()
edad = input("Ingrese su edad: ")
anio_nacimiento = 2026 - int(edad)

#crea el correo institucional. Todo en minuscula
print(nombre[0:2] + nombre[-1]+ "." + apellido[0] + str(anio_nacimiento) + "@inacapmail.cl")

#Las primeras 2 letras del nombre
#la ultima letra del nombre
#mas un "."
#mas la primera letra del apellido
#mas el año de nacimiento
#@inacapmail.cl
