import json
logueado = False # refleja en el menu si estas logueado o no. 


### FUNCIONES AUXILIARES ###
def cargar_usuarios():
    """
    cargar_usuarios
    
    Lee el archivo y devuelve un diccionario con los usuarios y contraseñas almacenados.
    Si el archivo está vacío o no existe, devuelve un diccionario vacío.
    """
    try:
        with open(r'usuarios.json', 'r') as archivo:
            contenido = archivo.read()
            return json.loads(contenido) if contenido else {}  # Manejar archivo vacío
    except FileNotFoundError:
        return {}
    except json.decoder.JSONDecodeError:
        print("El archivo 'usuarios.json' no contiene un JSON válido.")
        return {}
    
    

def guardar_usuarios(usuarios):
    """
    guardar_usuarios
    Toma el diccionario y lo guarda en el archivo.
    """
    with open(r'usuarios.json', 'w') as archivo:
        json.dump(usuarios, archivo)
        
        

def registrar_usuario():
    """
    registrar_usuarios
    Registra un nuevo usuario en la aplicación.

    Solicita al usuario un nombre de usuario y una contraseña,
    realiza validaciones y almacena la información en el archivo de usuarios.
    confirma la contraseña, y se fijo que tenga de 6 a 10 caracteres.
    Se asegura que el usuario no exista
    """
    print(">>>Registrando nuevo usuario<<<")
    usuario = input("Usuario: ")
    
      
    while True:
        
        contraseña = input("Contraseña (debe tener mínimo 6 caracteres, máximo 10): ")
        confirmar_contraseña = input("Confirmar Contraseña: ")

        if contraseña == confirmar_contraseña:
            if 6 <= len(contraseña) <= 10:
                print("Contraseña válida. Usuario registrado con éxito.")
                break
            else:
                print("La contraseña debe tener entre 6 y 10 caracteres, por favor intenta de nuevo.")
        else:
            print("Las contraseñas no coinciden. Intenta de nuevo.")
    
    usuarios = cargar_usuarios()

 
    if usuario not in usuarios:
        
        usuarios[usuario] = contraseña
        guardar_usuarios(usuarios)
        print(f"Usuario '{usuario}' registrado con éxito.")
    else:
        print(f"El usuario '{usuario}' ya existe. Por favor, elige otro nombre.")



def iniciar_sesion():
    """
    iniciar_sesion
    tiene solo 3 intentos
    """
    global logueado
    print(">>>Iniciando sesión<<<")
   
    for intento in range(3):
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        usuarios = cargar_usuarios()

        if usuario in usuarios and usuarios[usuario] == contraseña:
            print(f"Bienvenido, {usuario}!")
            logueado = True
            return
        else:
            print(f"Intento {intento + 1} de 3 : Usuario o contraseña incorrectos. Inténtelo de nuevo.")

    print(f"Has alcanzado el número máximo de intentos. Volviendo al menú principal.")

def salir():
    """
    salir
    Sale de la aplicación
    """
    print(">>>Saliendo de la aplicación.<<<")
    quit()

###ESTRUCTURA PRINCIPAL###
def mostrar_menu():
    """
    mostrar_menu
    Muestra el menu y comenta si estas o no logueado
    """
    print("Bienvenido")
    if logueado:
        print ("Sesión iniciada")
    else:
        print("Sesión no iniciada")
    print("1. Iniciar Sesión")
    print("2. Registrarse")
    print("3. Salir")

while True:
    
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    switch_menu = {
        '1': iniciar_sesion,
        '2': registrar_usuario,
        '3': salir
    }

    selected_option = switch_menu.get(opcion)

    if selected_option:
        selected_option()
    else:
        print("Opción no válida. Inténtelo de nuevo.")
        
help(registrar_usuario)
