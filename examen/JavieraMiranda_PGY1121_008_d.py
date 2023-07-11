import funciones as fn


while True:
    fn.ver_menu()
    opcion = fn.validar_opcion()
    if opcion == 1:
        fn.comprar_entradas()
    elif opcion == 2:
        fn.ubicaciones_disponibles()
    elif opcion == 3:
        fn.listado_asistentes()
    elif opcion == 4:
        fn.ganancias_totales()
    else:
        fn.salir()