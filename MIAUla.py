import json
import os
print("Bienvenido a MIAUla, Ingresa una opcion (Numero)")
try:
    with open("MIAUla.json", "r") as file:
        datos=json.load(file)
except FileNotFoundError:
    datos={}
def guardar():
    with open("MIAUla.json", "w") as file:
        json.dump(datos,file, indent=8, ensure_ascii=False)
def limpiar(x):
    return " ".join ((x).strip().lower().split()).title()
def menu():
    print("1. Registrarte ")
    print("2. Iniciar Sesion")
    print("3. Cambiar contraseña")
    print("4. Salir")
def menu_inicio():
    print("Pagina principal")
    print("1. Consultar tareas")
def pedir_opcion():
    while True:
        try:
            opcion=int(input("Ingresa la opcion: "))
            print(f"Su opcion es {opcion}")
            return opcion
        except:
            print("La opcion debe de ser un numero")
inicio=False
while True:
    menu()
    opcion=pedir_opcion()
#Bloque de registro
    if opcion==1:
        while True:
            codigo_unico=input("Ingresa codigo unico: ")
            codigo_unico=codigo_unico.upper()
            if codigo_unico in datos:
                print("Este codigo ya pertenece a otro usuario")
            else:
                print(f"Codigo: {codigo_unico} registrado exitosamente")
                break
        nombre1=input("Ingrese su primer nombre: ")
        nombre1=limpiar(nombre1)
        print(f"Tu primer nombre es {nombre1}")   
        nombre2=input("Ingrese su segundo nombre: ")
        nombre2=limpiar(nombre2)
        print(f"Tu segundo nombre es {nombre2}")
        apellido1=input("Ingrese su primer apellido: ")
        apellido1=limpiar(apellido1)
        print(f"Tu primer apellido es {apellido1}")
        apellido2=input("Ingrese su segundo apellido: ")
        apellido2=limpiar(apellido2)
        print(f"Tu segundo apellido es {apellido2}")
        completo=nombre1+" "+nombre2+" "+apellido1+" "+apellido2
        print(f"Nombre completo: {completo}")
        while True:
            institucion=input("Ingresa nombre de tu institucion academica: ")
            institucion=limpiar(institucion)
            print(f"Institucion Academica: {institucion}")
            siono=input("Deseas continuar?: ")
            siono=limpiar(siono)
            if siono=="Si":
                break
            elif siono=="No":
                print("Intenta de nuevo")
            else:
                print("Si o No")
        while True:
            correo=input("Ingresa tu correo electronico: ")
            if correo in datos:
                print("Este correo ya fue registrado. Intenta con otro")
            else:
                print("Verificacion de correo electronico exitosa")
                break
        while True:
            contraseña=input("Ingresa nueva contraseña: ")
            confirmacion=input("Ingresa nuevamente tu contraseña: ")
            if confirmacion == contraseña:
                print("Coincidencia Exitosa")
                break
            else:
                print("Contraseñas no coinciden. Intenta de nuevo")
        datos[codigo_unico]=[completo, 
                        institucion,
                        correo,
                        contraseña]
        guardar()
#Bloque de inicio de sesion
    elif opcion==2:
        while True:
            buscar=input("Ingrese codigo unico: ")
            buscar=buscar.upper().strip()
            encontrado=False
            if buscar in datos:
                print("Bienvenido")
                while True:
                    contraseña=input("Ingresa contraseña: ")
                    if contraseña == datos[buscar][3]:
                        print("Contraseña correcta")
                        encontrado=True
                        print(f"Bienvenido {datos[buscar][0]} a MIAUla")
                        inicio=True
                        break
                    else:
                        print("Contraseña incorrecta. Intenta otra vez")
                break
            if not encontrado:
                print(f"Codigo unico: {buscar} no esta registrado")
#Bloque de cambio de contraseña
    elif opcion==3:
        while True:
            codigo=input("Ingresa codigo unico: ")
            codigo=limpiar(codigo)
            encontrado=False
            if codigo in datos:
                while True:
                    contraseña=input("Ingresa contraseña: ")
                    if contraseña == datos[codigo][3]:
                        print("Contraseña correcta")
                        encontrado=True
                        while True:
                            nueva_contraseña=input("Ingresa nueva contraseña: ")
                            confirmacion=input("Vuelve a introducir tu nueva contraseña: ")
                            if confirmacion==nueva_contraseña:
                                print("Contraseña cambiada con exito")
                                datos[codigo][3]=nueva_contraseña
                                guardar()
                                break
                            else:
                                print("Contraseñas no conciden. Intenta de nuevo")
                    else:
                        print("Contraseña incorrecta. Intenta otra vez")
            if not encontrado:
                print(f"Codigo unico: {codigo} no esta registrado")
    elif opcion >=5 or opcion <=0: 
        print("Solo existen 4 opciones. Intenta de nuevo")
    elif opcion==4:
        print("Adios")
        break
#Bloque de inicio
    if inicio==True:
        print(f"Nombre de estudiante: {datos[buscar][0]}")
        print(f"Universidad: {datos[buscar][1]}")
        menu_inicio()
        opcion=pedir_opcion()
        if opcion==1:
            try:
                mostrar=os.listdir("Tareas")
                print(mostrar)
            except FileNotFoundError:
                mostrar_error=os.mkdir("Tareas")
                print(mostrar_error)