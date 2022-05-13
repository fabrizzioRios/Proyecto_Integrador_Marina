from Version_1_ProyectoHospital import seleccionar_insumos
from datetime import datetime
import random
import json
import matplotlib.pyplot as plt

USERS = [
    {
        "id": 1,
        "name": "marina",
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
        "place": None
    }
]

TICKET = []

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
        self.reason = None
        self.doctor = None
        self.place = None

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
            "reason": self.reason,
            "doctor": self.doctor,
            "place": self.place
        }
        USERS.append(user_d)
        with open('usuarios.txt', 'a') as file:
            file.write(f"{str(user_d)}\n")

    @classmethod
    def delete_user(cls):
        try:
            username = input("Que usuario quieres eliminar?")
            for i in range(len(USERS)):
                if USERS[i]['username'] == username:
                    if USERS[i]['is_admin']:
                        raise ValueError("No puedes eliminar a otro administrador")
                    with open('deleted_users.txt', 'a') as file:
                        file.write(f"{str(USERS[i])}\n")
                    del USERS[i]
                    break
            return True
        except ValueError as err:
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
    def __init__(self, patient_id, start_date, end_date, type_place):
        self.id_ticket = random.randint(1, 20)
        self.patient_id = patient_id
        self.start_date = start_date
        self.end_date = end_date
        self.type_place = type_place

    def add_ticket(self):
        amount = self.amount_calculate(self.type_place, self.start_date, self.end_date)

        ticket_dict = {
            "id": self.id_ticket,
            "patient_id": self.patient_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "type": self.type_place,
            "amount": amount
        }
        TICKET.append(ticket_dict)
        with open('cuentas.txt', 'a') as file:
            file.write(f"{str(ticket_dict)}\n")

    def amount_calculate(self, type_place, start_date, end_date):
        costo = 0
        date_type = '%Y-%m-%d'
        start_date = datetime.strptime(start_date, date_type)
        end_date = datetime.strptime(end_date, date_type)
        totaltime = str((end_date - start_date).days)
        if self.type_place == "Urgency":
            with open('insumos.json') as lista_insumos:
                insumos = json.load(lista_insumos)
            print("----------- Lista de insumos -----------")
            print("Nombre : Precio ")
            for key in insumos['All_Insumos']:
                print(f"{insumos['All_Insumos'][key]['name']} : {insumos['All_Insumos'][key]['price']}")
            print("----------------------------------------")
            costo = seleccionar_insumos()
        if type_place == "Floor":
            costo = TYPE_PLACES[1]["amount"] * float(totaltime)
        if type_place == "Therapy":
            costo = TYPE_PLACES[2]["amount"] * float(totaltime)
        costo = costo * 1.20
        return costo

    @classmethod
    def delete_ticket(cls):
        try:
            ticket_id = int(input("¿Cual es el id del ticket?"))
            for i in range(len(TICKET)):
                if TICKET[i]['id'] == ticket_id:
                    with open('deleted_tickets.txt', 'a') as file:
                        file.write(f"{str(TICKET[i])}\n")
                    del TICKET[i]
                    break
            return True
        except Exception as err:
            return False

    @classmethod
    def find_ticket(cls, id):
        try:
            ticket_find = next(item for item in TICKET if item["id"] == id)
            return ticket_find
        except Exception as err:
            return None


def check_place(floor):
    if floor == 1:
        return "Urgency"
    if floor == 2:
        return "Floor"
    if floor == 3:
        return "Therapy"


def char_digit(input_string):
    return any(char_dig.isalpha() for char_dig in input_string)


def data_analysis():
    print(
        "\n====================================================================================================\n")
    data_users = int(input("Ver graficas:\n1)Pay\n2)Barras\n3)Salir"))
    if data_users == 1:
        c_admins = 0
        c_nurses = 0
        c_patients = 0
        for i in USERS:
            if i.get('is_admin'):
                c_admins += 1
            if i.get('is_nurse'):
                c_nurses += 1
            if i.get('is_patient'):
                c_patients += 1
        etiquetas = ['Pacientes', 'Enfermeras', 'Administradores']
        valores = [c_patients, c_nurses, c_admins]
        colores = ['red', 'green', 'blue']
        plt.pie(x=valores, labels=etiquetas, colors=colores, autopct='%1.2f%%', shadow=True)
        plt.title('Usuarios')
        plt.show()
        data_analysis()
    if data_users == 2:
        c_admins = 0
        c_nurses = 0
        c_patients = 0
        for i in USERS:
            if i.get('is_admin'):
                c_admins += 1
            if i.get('is_nurse'):
                c_nurses += 1
            if i.get('is_patient'):
                c_patients += 1
        eje_x = ['Administradores', 'Enfermeras', 'Pacientes']
        eje_y = [c_admins, c_nurses, c_patients]
        plt.bar(eje_x, eje_y)
        plt.ylabel('Cantidad de usuarios')
        plt.xlabel('Tipos de usuarios')
        plt.title('Cantidad y tipos de usuarios')
        plt.show()
        data_analysis()
    if data_users == 3:
        pass
