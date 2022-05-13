import json
import search_tools


def menu():
    user = None
    try:
        print("============================================================="
              "====================================================\n")
        opcion = input("Bienvenido al sistema de gestion de insumos y personal, ¿Que desea hacer?:\n"
                       "\n1)Iniciar Sesion:\n2)Registrar:\n3)Salir")
        opt = search_tools.char_digit(opcion)
        if opt:
            raise ValueError("Tus datos deben ser numericos")
        opcion = int(opcion)
        if opcion == 1:
            if not search_tools.USERS:
                raise ValueError("Para poder iniciar sesion deben existir usuarios, registra uno!")
            else:
                iniciar_sesion()
        elif opcion == 2:
            registrar_usuario(user)
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
    try:
        print("\n=========================== Iniciar Sesion ==========================\n")
        username = input("Nombre de usuario:")
        if len(username) < 0:
            raise ValueError("Tus datos no pueden estar vacios")
        passw = input("Contraseña:")
        if len(passw) < 0:
            raise ValueError("Tus datos no pueden estar vacios")
        user = search_tools.User.log_in(username, passw)
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


def registrar_usuario(user):
    try:
        if user is None:
            print("\n=========================== Registrar Usuarios ==========================\n")
            choice = input("Seleccione el tipo de usuario que desea registrar:\n\n1) Administrador\n2) Enfermera\n3) "
                           "Paciente")
            chc = search_tools.char_digit(choice)
            if chc:
                raise ValueError("Tus datos deben ser numericos")

            user_name = str(input("Ingresar el username:"))
            name_user = str(input("Ingresar el nombre:"))
            password_user = str(input("Ingrese la contraseña a registrar:"))
            user_created = search_tools.User(user_name, password_user, name_user)

            choice = int(choice)
            if choice == 1:
                user_created.is_admin = True
                user_created.add_user()
                user = search_tools.User.log_in(user_created.username, password_user)
                menu_administrador(user)

            if choice == 2:
                user_created.is_nurse = True
                user_created.add_user()
                user = search_tools.User.log_in(user_created.username, password_user)
                menu_enfermera(user)

            if choice == 3:
                weight = int(input("Ingrese el peso del paciente:"))
                height = int(input("Ingrese la altura en cm:"))
                blood = input("Ingrese el tipo de sangre:")
                reason = str(input("Motivo de la hospitalización:"))
                floor = int(input("Piso en el que se encuentra:\n1) Urgencias(Urgency)\n2) Piso(Floor)"
                                  "\n3) Terapia intensiva(Therapy)"))

                doctor = str(input("Doctor que atiende al paciente:"))

                user_created.place = search_tools.check_place(floor)

                user_created.weight = weight
                user_created.height = height
                user_created.blood = blood
                user_created.reason = reason
                user_created.doctor = doctor
                user_created.is_patient = True
                user_created.add_user()
                user = search_tools.User.log_in(user_created.username, password_user)

                menu_paciente(user)

        if user.get('is_admin') or user.get('is_nurse'):
            print("\n=========================== Registrar Usuarios ==========================\n")
            user_name = str(input("Ingresar el username:"))
            name_user = str(input("Ingresar el nombre:"))
            password_user = str(input("Ingrese la contraseña a registrar:"))
            user_created = search_tools.User(user_name, password_user, name_user)
            weight = int(input("Ingrese el peso del paciente:"))
            height = int(input("Ingrese la altura en cm:"))
            blood = input("Ingrese el tipo de sangre:")
            reason = str(input("Motivo de la hospitalización:"))
            floor = int(input("Piso en el que se encuentra:\n1) Urgencias(Urgency)\n2) Piso(Floor)"
                              "\n3) Terapia intensiva(Therapy)"))

            doctor = str(input("Doctor que atiende al paciente:"))

            user_created.place = search_tools.check_place(floor)

            user_created.weight = weight
            user_created.height = height
            user_created.blood = blood
            user_created.reason = reason
            user_created.doctor = doctor
            user_created.is_patient = True
            user_created.add_user()
            if user.get('is_admin'):
                menu_administrador(user)
            if user.get('is_nurse'):
                menu_enfermera(user)
        else:
            raise ValueError("Introduzca datos validos")
    except ValueError as err:
        print(err)
        registrar_usuario(user)


def menu_enfermera(user):
    try:
        print("\n=========================== Menu de enfermeras ==========================\n")
        choice = input(
            f"Bienvenido/a {user.get('username')} , ¿que desea hacer?\n\n1)Registrar un Paciente:\n2)Generar una "
            f"cuenta:\n3)Ver cuenta:\n4)Consultar Paciente:\n5)Salir")
        chc = search_tools.char_digit(choice)
        if chc:
            raise ValueError("Tus datos deben ser numericos")
        choice = int(choice)
        if choice == 1:
            registrar_usuario(user)
            menu_enfermera(user)
        if choice == 2:
            generar_cuenta(user)
            menu_enfermera(user)
        if choice == 3:
            ver_pacientes(user)
            menu_enfermera(user)
        if choice == 4:
            menu_monto(user)
            menu_enfermera(user)
        if choice == 5:
            menu()
        else:
            raise ValueError("Introduzca datos validos")
    except ValueError as err:
        print(err)
        menu_enfermera(user)


def menu_administrador(user):
    try:
        print("\n=========================== Menu del administrador ==========================\n")

        choice = input(f"Bienvenido/a {user.get('username')} , ¿que desea hacer?\n\n1)Registrar un paciente\n2)Ver "
                       f"pacientes\n3)Ver enfermeras:\n4)Eliminar Usuarios:\n5)Informacion de Usuarios\n6)Generar "
                       f"ticket\n7)Eliminar ticket\n8)Ver tickets\n9)Salir")
        chc = search_tools.char_digit(choice)
        if chc:
            raise ValueError("Tus datos deben ser numericos")
        choice = int(choice)
        if choice == 1:
            registrar_usuario(user)
        if choice == 2:
            ver_pacientes(user)
            menu_administrador(user)
        if choice == 3:
            ver_enfermeras()
            menu_administrador(user)
        if choice == 4:
            print(
                "\n================================================="
                "===================================================\n")
            deleted = search_tools.User.delete_user()
            if deleted:
                print("--- USUARIO ELIMINADO CON EXITO ---")
            else:
                raise ValueError("No se pudo eliminar el usuario")
            menu_administrador(user)
        if choice == 5:
            search_tools.data_analysis()
            menu_administrador(user)
        if choice == 6:
            generar_cuenta(user)
            menu_administrador(user)
        if choice == 7:
            print(
                "\n==================================================="
                "=================================================\n")
            deleted_ticket = search_tools.Ticket.delete_ticket()
            if deleted_ticket:
                print("--- TICKET ELIMINADO CON EXITO ---")
            else:
                raise ValueError("No se pudo eliminar el ticket")
            menu_administrador(user)
        if choice == 8:
            ver_tickets(user)
            menu_administrador(user)
        if choice == 9:
            menu()
        else:
            raise ValueError("Introduzca datos validos")
    except ValueError as err:
        print(err)
        menu_administrador(user)


def menu_paciente(user):
    try:
        user = user
        print("\n=========================== Menu de pacientes ==========================\n")

        choice = input(
            f"Bienvenido/a {user.get('username')} ID: {user.get('id')}"
            f", ¿que desea hacer?\n\n1)Generar mi cuenta\n2)Ver mi estado de "
            f"cuenta:\n3)Ver lista de insumos:\n4)Ver mis datos\n5)Salir")
        chc = search_tools.char_digit(choice)
        if chc:
            raise ValueError("Tus datos deben ser numericos")
        choice = int(choice)
        if choice == 1:
            generar_cuenta(user)
            menu_paciente(user)
        if choice == 2:
            ver_tickets(user)
            menu_paciente(user)
        if choice == 3:
            ver_lista_de_insumos()
            menu_paciente(user)
        if choice == 4:
            ver_pacientes(user)
            menu_paciente(user)
        if choice == 5:
            menu()
        else:
            raise ValueError("Introduzca datos validos")
    except ValueError as err:
        print(err)
        menu_paciente(user)


def generar_cuenta(user):
    print(
        "\n"
        "====================================================================================================\n")
    patient_id = user.get('id')
    start_date = str(input("Introduzca la fecha de ingreso:\n(YY-MM-DD)"))
    end_date = str(input("Introduzca la fecha de egreso:\n(YY-MM-DD)"))
    if user.get('is_admin') or user.get('is_nurse'):
        user_new = str(input("Cual es el nombre de usuario del paciente?"))
        data_user = search_tools.User.search_user(user_new)
        type_place = data_user.get('place')
        patient_id = data_user.get('id')
        new_ticket = search_tools.Ticket(patient_id, start_date, end_date, type_place)
        new_ticket.add_ticket()
        id_ticket = new_ticket.id_ticket
        monto_totalpaciente(data_user, id_ticket)

    type_place = user.get('place')
    new_ticket = search_tools.Ticket(patient_id, start_date, end_date, type_place)
    new_ticket.add_ticket()
    id_ticket = new_ticket.id_ticket
    monto_totalpaciente(user, id_ticket)


def ver_enfermeras():
    try:
        print("\n====================================================="
              "===============================================\n")
        decision = int(input("1) Ver todas las enfermeras\n2) Ver enfermera en especifico\n3)Salir\n"))
        if decision == 1:
            print("\n=========== ENFERMERAS ==========\n")
            for usuario in search_tools.USERS:
                if usuario["is_nurse"]:
                    print(f"Id: {usuario.get('id')} Nombre: {usuario.get('name')}\n")
        if decision == 2:
            name = str(input("Nombre de usuario de la enfermera:\n"))
            nurse = search_tools.User.search_user(name)
            if nurse is None:
                raise ValueError("El nombre de usuario es incorrecto o no existe")
            if not nurse.get('is_nurse'):
                raise ValueError("Tu usuario debe ser una enfermera")
            print(f"\n============ ENFERMERA {nurse.get('id')} ============\n")
            print(f"Nombre: {nurse.get('name')} Nombre de usuario: {nurse.get('username')}")
        if decision == 3:
            print(
                "\n"
                "================================================="
                "===================================================\n")
            pass
    except ValueError as err:
        print(err)
        ver_enfermeras()


def ver_pacientes(user):
    try:
        print(
            "\n====================================================================================================\n")
        decision = int(input("1) Ver todos los pacientes\n2) Ver paciente en especifico\n3) Salir"))
        if decision == 1:
            if user.get('is_patient'):
                raise ValueError("No tienes permisos para esto")
            else:
                print("\n=========== PACIENTES ============\n")
                for usuario in search_tools.USERS:
                    if usuario.get("is_patient"):
                        print(
                            f"Nombre: {usuario.get('name')} ----- Usuario: {usuario.get('username')}\nPeso: "
                            f"{usuario.get('weight')} ----- Estatura: {usuario.get('height')} ----- Tipo de sangre:"
                            f" {usuario.get('blood')}\nRazon de internamiento: {usuario.get('reason')} ----- "
                            f"Medico que lo atiende(io): {usuario.get('doctor')}\n")
                        print("=================================================="
                              "==================================================\n")
        if decision == 2:
            name = str(input("Usuario del paciente:"))
            patient = search_tools.User.search_user(name)
            if patient is None:
                raise ValueError("El nombre de usuario es incorrecto o no existe")
            if not patient.get('is_patient'):
                raise ValueError("Tu usuario debe ser una paciente")
            print(f"\n============ PACIENTE {patient.get('id')} ============\n")
            print(
                f"Nombre: {patient.get('name')} ----- Usuario: {patient.get('username')}\nPeso: {patient.get('weight')}"
                f"----- Estatura: {patient.get('height')} ----- "
                f"Tipo de sangre: {patient.get('blood')}\nRazon de interna"
                f"miento: {patient.get('reason')} ----- "
                f"Medico que lo atiende(io): {patient.get('doctor')}\n")
        if decision == 3:
            print(
                "\n"
                "==============================================================================================="
                "=====\n")
            pass
    except ValueError as err:
        print(err)
        ver_pacientes(user)


def ver_lista_de_insumos():
    with open('insumos.json') as lista_insumos:
        insumos = json.load(lista_insumos)
    print("=============== Lista de insumos =================")
    print("     Nombre : Precio ")
    for key in insumos['All_Insumos']:
        print(f"{insumos['All_Insumos'][key]['name']} : {insumos['All_Insumos'][key]['price']}")

    print("==================================================")


def ver_tickets(user):
    try:
        if search_tools.TICKET:
            print(
                "\n"
                "===================================================================="
                "================================\n")
            opcion = int(input("Que desea hacer?\n1)Ver un ticket\n2)Ver todos los tickets\n3)Salir"))
            if opcion == 1:
                if user.get("is_patient") or user.get("is_nurse") or user.get("is_admin"):
                    id_ticket = int(input("Coloque el ID del ticket:"))
                    one_ticket = search_tools.Ticket.find_ticket(id_ticket)
                    if one_ticket:
                        print(f"\nId del ticket:{one_ticket.get('id')}"
                              f"\nId del paciente:{one_ticket.get('patient_id')}"
                              f"\nLugar donde estuvo:{one_ticket.get('type')}"
                              f"\nFecha de ingreso:{one_ticket.get('start_date')}"
                              f"\nFecha de salida:{one_ticket.get('end_date')}"
                              f"\nTotal: ${one_ticket.get('amount')}\n")
                        ver_tickets(user)
                    else:
                        raise ValueError("El id del ticket es erroneo o no existe")
            if opcion == 2:
                if user.get("is_admin") or user.get("is_nurse"):
                    for i in range(0, len(search_tools.TICKET)):
                        item = search_tools.TICKET[i]
                        print(
                            "\n"
                            "====================================================="
                            "===============================================\n")
                        for clave in item:
                            print(clave, ":", item[clave])
                        print(
                            "\n"
                            "===================================================="
                            "===============================================\n")
                    ver_tickets(user)
                else:
                    raise ValueError("No tienes los permisos necesarios")
            if opcion == 3:
                pass
        else:
            print("No existen tickets, agrega uno para poder ver sus datos")
    except ValueError as err:
        print(err)
        ver_tickets(user)


def menu_monto(user):
    print(
        "\n"
        "====================================================================================================\n")
    print("Teclea la opcion: \n1)Monto total de un paciente \n2)Monto total general\n3)Salir")
    op = int(input("Teclea la opcion:"))
    if op == 1:
        id_ticket = int(input("Cual es el id de su ticket?"))
        monto_totalpaciente(user, id_ticket)
        menu_monto(user)
    if op == 2:
        monto_general(user)
        menu_monto(user)
    if op == 3:
        pass
    else:
        print("Tu opcion no es correcta teclea una opcion correcta")
        menu_monto(user)


def monto_totalpaciente(user, id_ticket):
    print(
        "\n"
        "====================================================================================================\n")
    new_ticket = search_tools.Ticket.find_ticket(id_ticket)
    if new_ticket:
        if new_ticket.get('amount') != 0:
            print(f"El monto total de tu cuenta es: ${new_ticket.get('amount')}\n"
                  f"El id de tu ticket es {new_ticket.get('id')}")
        if new_ticket.get('amount') == 0:
            print("Tu monto no puede ser 0")
    else:
        print("El id del ticket es incorrecto o no existe")

def monto_general(user):
    print(
        "\n"
        "====================================================================================================\n")
    total = 0
    for i in search_tools.TICKET:
        total = total + i.get("amount")

    print("El total en general es: $", total)
    menu_monto(user)


def seleccionar_insumos():
    with open('insumos.json') as lista_insumos:
        insumos = json.load(lista_insumos)
        costoacumulado = 0

    while True:
        print(
            "\n"
            "====================================================================================================\n")
        selection = input("Eliga uno de los insumos escribiendo el nombre tal cual. Escriba 'Exit' para salir : ")
        if selection == 'Exit':
            break
        try:
            nombre = insumos['All_Insumos'][selection]['name']
            precio = insumos['All_Insumos'][selection]['price']
            print(f"Seleccionaste {nombre} con un costo de {precio} por unidad.")
            cantidad = int(input("Escribe tu cantidad de insumos utilizados : "))
            costoacumulado += precio * cantidad
        except Exception as ex:
            print("<Error en la entrada de datos : No se agrego a la lista >")

    return costoacumulado


if __name__ == "__main__":
    menu()
