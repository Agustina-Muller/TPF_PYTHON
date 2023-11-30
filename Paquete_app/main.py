import Menuapp as main
programa_en_ejecucion = True

###ESTRUCTURA PRINCIPAL###

while programa_en_ejecucion:
    main.mostrar_menu()

    opcion = input("Seleccione una opción: ")

    switch_menu = {
        '1': main.iniciar_sesion,
        '2': main.registrar_usuario,
        '3': main.salir
    }

    selected_option = switch_menu.get(opcion)

    if selected_option:
        selected_option()
    else:
        print("Opción no válida. Inténtelo de nuevo.")

    if opcion == '3':
        programa_en_ejecucion = False 