from Programa_Recompensas import ProgramaRecompensas #Importa la Programa de recompensas

#Define la clase Main
class Main:
    def __init__(self):
        # Inicializa la instancia de ProgramaRecompensas
        self.programa_recompensas = ProgramaRecompensas()

    def menu_principal(self):
        while True:
            # Muestra el menú principal
            print("\nMenú Principal:")
            print("1. Clientes")
            print("2. Administrador")
            print("3. Salir")

            # Solicita al usuario que seleccione una opción
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                # Llama al menú de clientes
                self.programa_recompensas.menu_clientes()

            elif opcion == "2":
                # Solicita nombre de usuario y contraseña para autenticar al administrador
                usuario = input("Ingrese el nombre de usuario: ")
                contrasena = input("Ingrese la contraseña: ")

                # Verifica las credenciales del administrador y muestra el menú de administrador si son correctas
                if self.programa_recompensas.autenticar_admin(usuario, contrasena):
                    self.programa_recompensas.menu_admin()
                else:
                    print("El usuario o contraseña está incorrecto.")

            elif opcion == "3":
                # Guarda la informacion en el archivo
                self.programa_recompensas.guardar_informacion()
                # Sale del programa
                break
            else:
                # Maneja una opción incorrecta
                print("Opción incorrecta. Vuelva a intentar.")

if __name__ == "__main__":
    # Crea una instancia de la clase Main y ejecuta el menú principal
    main = Main()
    main.menu_principal()
