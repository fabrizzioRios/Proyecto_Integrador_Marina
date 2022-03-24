import json
import datetime
import random

# Lista de usuarios, donde se agregaran o eliminaran los usuarios que se necesiten
# en el programa, estara compuesta de un diccionario con las keys de Id, Name,
# Password, Username, Is_admin, Is_nurse. Is_admin e Is_nurse son variables booleanas
# que indican el rol del usuario, es decir, si es enfermera o admin.

USERS = [
    {
        "id": 1,
        "name": "Luis",
        "password": "sdasdas",
        "username": "admin",
        "is_admin": True,
        "is_nurse": False,
        "is_pacient": False
    }
]

TICKET = []

# Type places es una lista de diccionarios, donde se indican los tres pisos
# que estan presentes en el hostipal, con la key de description y amount.
# Description tiene el value de Urdengias, Piso y Terapia intensiva y la Amount
# tiene el valor de los precios de cada tipo.

TYPE_PLACES = [
    {
        "description": "Urgency",
        "amount": 0,
    },
    {
        "description": "Floor",
        "amount": 2000,
    },
    {
        "description": "Therapy",
        "amount": 2500,
    },
]


# Clase Usuario, de aqui se designa el username que es nombre de usuario
# y se designa el password como una variable privada, tambien se declara
# si el usuario es enfermera o administrador, se le asigna un id random
# y se obtiene el nombre de la enfermera


class User:
    def __init__(self, username: str, password, name: str):
        self.id = random.randint(1, 20)
        self.username = username
        self.name = name
        self.__password = password if password else ""
        self.is_admin = False
        self.is_nurse = False
        self.is_patient = False

    # Esta funcion añade el usuario a la lista USERS, con los datos anteriores
    # !!! SOLAMENTE AÑADE AL USUARIO A LA LISTA !!!

    def add_user(self):
        user_d = {
            "id": self.id,
            "name": self.name,
            "password": self.__password,
            "username": self.username,
            "is_admin": self.is_admin,
            "is_nurse": self.is_nurse,
            "is_patient": self.is_patient
        }
        USERS.append(user_d)

    # Esta funcion debe de eliminar el usuario de la lista USERS en base a el id, nombre
    # o username.
    # !!!SOLO ELIMINA LOS USUARIOS DE LA LISTA!!!

    def delete_user(self):
        pass


class Ticket:
    def __init__(self, start_date, end_date, type_place, patient_id):
        self.id_ticket = random.randint(1, 20)
        self.patient_id = patient_id
        self.start_date = start_date
        self.end_date = end_date
        self.type_place = type_place

    # Esta funcion añade el ticket a la lista TICKET, con los datos anteriores
    # !!! SOLAMENTE AÑADE EL TICKET A LA LISTA !!!

    def add_ticket(self):
        # amount = amount_calculate(self.type_place, self.start_date, self.end_date)

        ticket_dict = {
            "id": self.id_ticket,
            "patient_id": self.patient_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "type": self.type_place,
            # "amount": amount
        }
        TICKET.append(ticket_dict)

    # Este metodo calcula el precio dependiendo de la fecha de inicio y del tipo de
    # lugar donde esta el paciente

    def amount_calculate(self, type_place, start_date, end_date):
        if type_place == "Urgency":
            pass
        if type_place == "Floor":
            pass
        if type_place == "Therapy":
            pass

        return True

    # Esta funcion debe de eliminar el ticket de la lista TICKET en base a el id del paciente,
    # nombre del paciente o fecha de inicio
    # !!!SOLO ELIMINA LOS TICKETS DE LA LISTA!!!
    def delete_ticket(self):
        pass


# Funcion de menu, donde se despliegan las acciones que un usuario puede elegir
# Esta destinado a ser la parte interactiva que se considera como la base principal
# de donde deriva todo el sistema

def menu():
    # El try controla los errores, en caso de que alguien introduzca un str en
    # lugar de un int, el programa no dara un error, solo hara lo que este
    # dentro del except.
    try:
        print("============================================================="
              "====================================================\n")
        opcion = input("Bienvenido al sistema de gestion de insumos y personal, ¿Que desea hacer?:\n"
                       "\n1)Iniciar Sesion:\n2)Registrar:\n3)Salir")
        opt = char_digit(opcion)
        if opt:
            raise ValueError("Tus datos deben ser numericos")
        opcion = int(opcion)
        if opcion == 1:
            iniciar_sesion()
        elif opcion == 2:
            registrar_usuario()
        elif opcion == 3:
            exit()
        else:
            raise Exception("Introduzca datos validos")
    except ValueError as err:
        print(err)
        menu()
    except Exception as err:
        print(err)
        menu()


def iniciar_sesion():

    # Se pedira los datos de iniciar sesion, tendra que pedir el
    # username y el password, y debera de haber una condicional
    # que evalue si el username y el password esta dentro de
    # el diccionario de usuarios, si no esta debera de decir que
    # el usuario no existe y que debe registrarlo, si el usuario esta
    # debera evaluar si es administrador, enfermera o paciente
    try:
        print("=========================== Iniciar Sesion ==========================\n")
        choice = input("Bienvenido/a, ¿que desea hacer?\n\n1)Menu Administrador:\n2)Menu Enfermera:\n3)Menu "
                       "Paciente:\n4)Salir")
        chc = char_digit(choice)
        if chc:
            raise ValueError("Tus datos deben ser numericos")
        choice = int(choice)
        if choice == 1:
            menu_administrador()
        if choice == 2:
            menu_enfermera()
        if choice == 3:
            menu_paciente()
        if choice == 4:
            menu()
        else:
            raise ValueError("Introduzca datos validos")
    except ValueError as err:
        print(err)
        iniciar_sesion()


def registrar_usuario():
    try:
        print("=========================== Registrar Usuarios ==========================\n")
        choice = input("Seleccione el tipo de usuario que desea registrar:\n\n1) Administrador\n2) Enfermera\n3) "
                       "Paciente")
        chc = char_digit(choice)
        if chc:
            raise ValueError("Tus datos deben ser numericos")
        choice = int(choice)
        if choice == 1:
            menu_administrador()
        if choice == 2:
            menu_enfermera()
        if choice == 3:
            menu_paciente()
        if choice == 4:
            iniciar_sesion()
        else:
            raise ValueError("Introduzca datos validos")
    except ValueError as err:
        print(err)
        registrar_usuario()
    # Registrara usuario, pedira los datos de la clase usuario y
    # se indicara aca si es enfermera, administrador o paciente


# Este menu se desplegara al acceder a la cuenta en dado caso de que el
# usuario sea una enfermera, aqui se tendra la opcion de registrar un
# paciente, generar una cuenta, consultar paciente/s y salir al menu de inicio
def menu_enfermera():
    try:
        print("=========================== Menu de enfermeras ==========================\n")
        choice = input("Bienvenido/a, ¿que desea hacer?\n\n1)Registrar un Paciente:\n2)Generar una cuenta:\n3)Consultar "
                       "Paciente:\n4)Salir")
        chc = char_digit(choice)
        if chc:
            raise ValueError("Tus datos deben ser numericos")
        choice = int(choice)
        if choice == 1:
            registrar_usuario()
        if choice == 2:
            generar_cuenta()
        if choice == 3:
            ver_usuario()
        if choice == 4:
            iniciar_sesion()
        else:
            raise ValueError("Introduzca datos validos")
    except ValueError as err:
        print(err)
        menu_enfermera()


# Este menu se desplegara al acceder a la cuenta en dado caso de que el
# usuario sea una administrador, aqui se tendra la opcion de ver
# enfermeras, eliminar usuarios, y salir al menu de inicio

def menu_administrador():
    try:
        print("=========================== Menu del administrador ==========================\n")

        choice = input("Bienvenido/a, ¿que desea hacer?\n\n1)Ver enfermeras:\n2)Eliminar Usuarios:\n3)Salir")
        chc = char_digit(choice)
        if chc:
            raise ValueError("Tus datos deben ser numericos")
        choice = int(choice)
        if choice == 1:
            pass
        if choice == 2:
            ver_usuario()
        if choice == 3:
            iniciar_sesion()

        else:
            raise ValueError("Introduzca datos validos")
    except ValueError as err:
        print(err)
        menu_administrador()


# Este menu se desplegara al acceder a la cuenta en dado caso de que el
# usuario sea una paciente, aqui se tendra la opcion de checar el estado de
# cuenta, checar los insumos y precios y salir al menu.

def menu_paciente():
    try:
        print("=========================== Menu de pacientes ==========================\n")

        choice = input("Bienvenido/a, ¿que desea hacer?\n\n1)Ver mi estado de cuenta:\n2)Ver lista de insumos:\n3)Salir")
        chc = char_digit(choice)
        if chc:
            raise ValueError("Tus datos deben ser numericos")
        choice = int(choice)
        if choice == 1:
            generar_cuenta()
        if choice == 2:
            ver_usuario()
        if choice == 3:
            iniciar_sesion()

        else:
            raise ValueError("Introduzca datos validos")
    except ValueError as err:
        print(err)
        menu_paciente()


def ver_tickets():
    # Vera tickets en base a el codigo del paciente
    pass


def ver_usuario():
    # Ver enfermeras, pacientes
    pass


def generar_cuenta():
    # Generara la cuenta de un paciente, y debera poder hacer la sumatoria de
    # todas las cuentas
    pass


def char_digit(input_string):
    return any(char_dig.isalpha() for char_dig in input_string)


if __name__ == "__main__":
    menu()
