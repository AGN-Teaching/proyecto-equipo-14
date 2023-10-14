from Programa_Recompensas import ProgramaRecompensas #Importa la Programa de recompensas


class Menu:
    def __init__(self):
        # Inicializa la instancia de ProgramaRecompensas
        self.programa_recompensas = ProgramaRecompensas()

    # Menú para elegir entre Cliente Normal, Cliente VIP o Registrarse.
    def menu_clientes(self):
        while True:
            print("1. Cliente")
            print("2. Cliente VIP")
            print("3. Registrarse")
            print("4. Volver al Menú Principal ")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.programa_recompensas.ingresar_cliente()
            elif opcion == "2":
                self.programa_recompensas.ingresar_cliente_vip()
            elif opcion == "3":
                self.programa_recompensas.agregar_cliente()
            elif opcion == "4":
                self.programa_recompensas.guardar_informacion()
                break
            else:
                print("Opcion incorrecta vuelva a intentar")

    # Metodos para agregar y eliminar beneficios, Compañias y clientes

    def menu_beneficios(self):
        while True:
            print(" Menu Beneficios")
            print("1. Agregar Beneficio")
            print("2. Eliminar Beneficio")
            print("3. Regresar")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.programa_recompensas.agregar_beneficio()
            elif opcion == "2":
                self.programa_recompensas.eliminar_beneficio()
            elif opcion == "3":
                self.programa_recompensas.guardar_informacion()
                break
            else:
                print("Opción incorrecta, vuelva a intentar")

    def menu_compania(self):
        while True:
            print(" Menu Compañias")
            print("1. Agregar Compañia")
            print("2. Eliminar Compañia")
            print("3. Regresar")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.programa_recompensas.agregar_compania_socia()
            elif opcion == "2":
                self.programa_recompensas.menu_eliminar_compania()
            elif opcion == "3":
                self.programa_recompensas.guardar_informacion()
                break
            else:
                print("Opción incorrecta, vuelva a intentar")

    def menu_clientes_admin(self):
        while True:
            print(" Menu Clientes")
            print("1. Agregar Cliente")
            print("2. Eliminar Cliente")
            print("3. Mostrar informacion del cliente")
            print("4. Regresar")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.programa_recompensas.agregar_cliente()
            elif opcion == "2":
                self.programa_recompensas.menu_eliminar_cliente()
            elif opcion == "3":
                self.programa_recompensas.ver_informacion_cliente()
            elif opcion == "4":
                self.programa_recompensas.guardar_informacion()
                break
            else:
                print("Opción incorrecta, vuelva a intentar")

    # Menú principal para el administrador.

    def menu_admin(self):
        while True:
            print("\nMenú Administrador:")
            print("1. Menu Compañias")
            print("2. Menu Beneficios")
            print("3. Clientes")
            print("4. Mostrar Información")
            print("5. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_compania()
            elif opcion == "2":
                self.menu_beneficios()
            elif opcion == "3":
                self.menu_clientes_admin()
            elif opcion == "4":
                self.programa_recompensas.mostrar_informacion()
            elif opcion == "5":
                self.programa_recompensas.guardar_informacion()
                break
            else:
                print("Opción incorrecta. Por favor, seleccione una opción válida.")



