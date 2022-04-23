import json
from datetime import datetime
import random

# Lista de usuarios, donde se agregaran o eliminaran los usuarios que se necesiten
# en el programa, estara compuesta de un diccionario con las keys de Id, Name,
# Password, Username, Is_admin, Is_nurse. Is_admin e Is_nurse son variables booleanas
# que indican el rol del usuario, es decir, si es enfermera o admin.

USERS = [
    {
        "id": 1,
        "name": "Luis",
        "password": "123",
        "username": "admin",
        "is_admin": True,
        "is_nurse": False,
        "is_patient": False,
        "weight": None,
        "height": None,
        "blood": None,
        "reason": None,
        "doctor": None,
    },
    {
        "id": 1,
        "name": "Luis2",
        "password": "123",
        "username": "not_admin",
        "is_admin": False,
        "is_nurse": False,
        "is_patient": True,
        "weight": None,
        "height": None,
        "blood": None,
        "reason": None,
        "doctor": None,
    },
    {
        "id": 1,
        "name": "Luis3",
        "password": "123",
        "username": "not_admin2",
        "is_admin": False,
        "is_nurse": True,
        "is_patient": False,
        "weight": None,
        "height": None,
        "blood": None,
        "reason": None,
        "doctor": None,
    }
]

PATIENTS = []

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
        self.__password = password
        self.is_admin = False
        self.is_nurse = False
        self.is_patient = False
        self.weight = None
        self.height = None
        self.blood = None
        self.floor = None
        self.doctor = None

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
            "is_patient": self.is_patient,
            "weight": self.weight,
            "height": self.height,
            "blood": self.blood,
            "reason": self.floor,
            "doctor": self.doctor,
        }
        USERS.append(user_d)

    # Esta funcion debe de eliminar el usuario de la lista USERS basandose en el id, nombre
    # o username.
    # !!!SOLO ELIMINA LOS USUARIOS DE LA LISTA!!!

    @classmethod
    def delete_user(cls):
        try:
            username = input("Que usuario quieres eliminar?")
            for i in range(len(USERS)):
                if USERS[i]['username'] == username:
                    del USERS[i]
                    break
            return True
        except:
            return False

    @classmethod
    def log_in(cls, username, passw):
        try:
            user_find = next(item for item in USERS if item["username"] == username and item["password"] == passw)
            return user_find
        except:
            return None

    @classmethod
    def search_user(cls, username):
        try:
            user_find = next(item for item in USERS if item["username"] == username)
            return user_find
        except:
            return None


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
        costo = 0
        date_type = '%Y-%m-%d'
        start_date = datetime.strptime(start_date, date_type)
        end_date = datetime.strptime(end_date, date_type)
        totaltime = str((end_date - start_date).days)
        if type_place == "Urgency":
            # Abrir el json
            with open('insumos.json') as lista_insumos:
                insumos = json.load(lista_insumos)
            # Codigo para mostrar los insumos
            print("----------- Lista de insumos -----------")
            print("Nombre : Precio ")
            for key in insumos['All_Insumos']:
                print(f"{insumos['All_Insumos'][key]['name']} : {insumos['All_Insumos'][key]['price']}")
            print("----------------------------------------")
            # Seleccionar insumos
            # costo = seleccionar_insumos()
        if type_place == "Floor":
            costo = TYPE_PLACES[1]["amount"] * float(totaltime)
        if type_place == "Therapy":
            costo = TYPE_PLACES[2]["amount"] * float(totaltime)
        costo = costo * 1.20  # Se agrega el honorario del doctor
        return costo

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
            if not USERS:
                raise ValueError("Para poder iniciar sesion deben existir usuarios, registra uno!")
            else:
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
        print("\n=========================== Iniciar Sesion ==========================\n")
        username = input("Nombre de usuario:")
        if len(username) < 0:
            raise ValueError("Tus datos no pueden estar vacios")
        passw = input("Contraseña:")
        if len(passw) < 0:
            raise ValueError("Tus datos no pueden estar vacios")
        user = User.log_in(username, passw)
        if user is None:
            raise ValueError("Tu usuario o contraseña no es valida")
        if user.get("is_admin"):
            menu_administrador(user)
        if user.get("is_nurse"):
            menu_enfermera(user)
        if user.get("is_patient"):
            menu_paciente(user)
        else:
            raise ValueError("Introduzca datos validos")
    except ValueError as err:
        print(err)
        iniciar_sesion()


def registrar_usuario():
    try:
        print("\n=========================== Registrar Usuarios ==========================\n")
        choice = input("Seleccione el tipo de usuario que desea registrar:\n\n1) Administrador\n2) Enfermera\n3) "
                       "Paciente")
        chc = char_digit(choice)
        if chc:
            raise ValueError("Tus datos deben ser numericos")

        user_name = str(input("Ingresar el username:"))
        name_user = str(input("Ingresar el nombre:"))
        password_user = str(input("Ingrese la contraseña a registrar:"))
        user_created = User(user_name, password_user, name_user)

        choice = int(choice)
        if choice == 1:
            user_created.is_admin = True
            user_created.add_user()
            user = User.log_in(user_created.username, password_user)
            menu_administrador(user)

        if choice == 2:
            user_created.is_nurse = True
            user_created.add_user()
            user = User.log_in(user_created.username, password_user)
            menu_enfermera(user)

        if choice == 3:
            weight = int(input("Ingrese el peso del paciente:"))
            height = int(input("Ingrese la altura en cm:"))
            blood = input("Ingrese el tipo de sangre:")
            reason = str(input("Motivo de la hospitalización:"))
            floor = str(input("Piso en el que se encuentra:"))
            doctor = str(input("Doctor que atiende al paciente:"))
            user_created.weight = weight
            user_created.height = height
            user_created.blood = blood
            user_created.reason = reason
            user_created.floor = floor
            user_created.doctor = doctor
            user_created.is_patient = True
            user_created.add_user()
            user = User.log_in(user_created.username, password_user)
            menu_paciente(user)

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
def menu_enfermera(user):
    try:
        print("\n=========================== Menu de enfermeras ==========================\n")
        choice = input(
            f"Bienvenido/a {user.get('name')} , ¿que desea hacer?\n\n1)Registrar un Paciente:\n2)Generar una "
            f"cuenta:\n3)Consultar Paciente:\n4)Salir")
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
            menu()
        else:
            raise ValueError("Introduzca datos validos")
    except ValueError as err:
        print(err)
        menu_enfermera(user)


# Este menu se desplegara al acceder a la cuenta en dado caso de que el
# usuario sea una administrador, aqui se tendra la opcion de ver
# enfermeras, eliminar usuarios, y salir al menu de inicio

def menu_administrador(user):
    try:
        print("\n=========================== Menu del administrador ==========================\n")

        choice = input(f"Bienvenido/a {user.get('name')} , ¿que desea hacer?\n\n1)Registrar un paciente\n2)Ver "
                       f"pacientes\n3)Ver enfermeras:\n4)Eliminar Usuarios:\n5)Salir")
        chc = char_digit(choice)
        if chc:
            raise ValueError("Tus datos deben ser numericos")
        choice = int(choice)
        if choice == 1:
            pass
        if choice == 2:
            ver_pacientes()
            menu_administrador(user)
        if choice == 3:
            ver_enfermeras()
            menu_administrador(user)
        if choice == 4:
            deleted = User.delete_user()
            if deleted:
                print("--- USUARIO ELIMINADO CON EXITO ---")
            menu_administrador(user)
        if choice == 5:
            menu()

        else:
            raise ValueError("Introduzca datos validos")
    except ValueError as err:
        print(err)
        menu_administrador(user)


# Este menu se desplegara al acceder a la cuenta en dado caso de que el
# usuario sea una paciente, aqui se tendra la opcion de checar el estado de
# cuenta, checar los insumos y precios y salir al menu.

def menu_paciente(user):
    try:
        print("\n=========================== Menu de pacientes ==========================\n")

        choice = input(
            f"Bienvenido/a {user.get('name')} , ¿que desea hacer?\n\n1)Ver mi estado de cuenta:\n2)Ver lista de "
            f"insumos:\n3)Salir")
        chc = char_digit(choice)
        if chc:
            raise ValueError("Tus datos deben ser numericos")
        choice = int(choice)
        if choice == 1:
            generar_cuenta()
        if choice == 2:
            ver_usuario()
        if choice == 3:
            menu()
        else:
            raise ValueError("Introduzca datos validos")
    except ValueError as err:
        print(err)
        menu_paciente(user)


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


def ver_enfermeras():
    try:
        print("\n====================================================================================================\n")

        decision = int(input("1) Ver todas las enfermeras\n2) Ver enfermera en especifico\n3)Salir\n"))
        if decision == 1:
            print("\n=========== ENFERMERAS ==========\n")
            for usuario in USERS:
                if usuario["is_nurse"]:
                    print(f"Id: {usuario.get('id')} Nombre: {usuario.get('name')}\n")
        if decision == 2:
            name = str(input("Nombre de usuario de la enfermera:\n"))
            nurse = User.search_user(name)
            if nurse is None:
                raise ValueError("El nombre de usuario es incorrecto o no existe")
            if not nurse.get('is_nurse'):
                raise ValueError("Tu usuario debe ser una enfermera")
            print(f"\n============ ENFERMERA {nurse.get('id')} ============\n")
            print(f"Nombre: {nurse.get('name')} Nombre de usuario: {nurse.get('username')}")
        if decision == 3:
            print(
                "\n"
                "====================================================================================================\n")
            pass
    except ValueError as err:
        print(err)
        ver_pacientes()


def ver_pacientes():
    try:
        print("\n====================================================================================================\n")
        decision = int(input("1) Ver todos los pacientes\n2) Ver paciente en especifico\n3) Salir"))
        if decision == 1:
            print("\n=========== PACIENTES ============\n")
            for usuario in USERS:
                if usuario.get("is_patient"):
                    print(f"Id: {usuario.get('id')} Nombre: {usuario.get('name')}\n")
        if decision == 2:
            name = str(input("Usuario del paciente:"))
            patient = User.search_user(name)
            if patient is None:
                raise ValueError("El nombre de usuario es incorrecto o no existe")
            if not patient.get('is_patient'):
                raise ValueError("Tu usuario debe ser una paciente")
            print(f"\n============ PACIENTE {patient.get('id')} ============\n")
            print(f"Nombre: {patient.get('name')} ----- Usuario: {patient.get('username')}\nPeso: {patient.get('weight')} ----- Estatura: {patient.get('height')} ----- "
                  f"Tipo de sangre: {patient.get('blood')}\nRazon de internamiento: {patient.get('reason')} ----- "
                  f"Medico que lo atiende(io): {patient.get('doctor')}\n")
        if decision == 3:
            print(
                "\n"
                "====================================================================================================\n")

            pass
    except ValueError as err:
        print(err)
        ver_pacientes()


if __name__ == "__main__":
    menu()
