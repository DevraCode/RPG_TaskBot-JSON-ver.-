import json
import os
import atexit

#REGISTRO DEL USUARIO
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

USERS_DATA_FILE = "json/users_data.json"
REGISTERED_USERS = {} #Datos del usuario almacenados en user_data.json

USERS_TASK_LIST = "json/task_list.json"
TASKLIST = {} #Lista de tareas del usuario almacenada en task_list.json

USER_CHARACTER = "json/characters.json"
CHARACTER = {}

USERS_REMINDERS_FILE = "json/reminders.json"
REMINDERS = {}


#USUARIOS REGISTRADOS
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#Guardado y carga de usuarios
def save_users():
    global REGISTERED_USERS
    try:
        with open(USERS_DATA_FILE, 'w') as f:
            json.dump(REGISTERED_USERS, f, indent=4)
        print(f"Datos guardados: {len(REGISTERED_USERS)} usuarios escritos en disco.")
    except Exception as e:
        print(f" Error al guardar datos: {e}")


def load_users():
    global REGISTERED_USERS
    if os.path.exists(USERS_DATA_FILE):
        try:
            with open(USERS_DATA_FILE, "r") as f:

                content = f.read().strip()
                if not content:
                    print(f"DEBUG: {USERS_DATA_FILE} está vacío.")
                    return

                data_from_json = json.loads(content)
                REGISTERED_USERS = {str(k): v for k, v in data_from_json.items()}
                print(f" Datos cargados: {len(REGISTERED_USERS)} usuarios en memoria.")

        except json.JSONDecodeError:
            print(" Error al leer el archivo JSON. Iniciando con diccionario vacío.")


#PERSONAJE ELEGIDO POR EL USUARIO
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#Guardado y carga de los personajes
def save_character():
    global CHARACTER
    try:
        with open(USER_CHARACTER, 'w') as f:
            json.dump(CHARACTER, f, indent=4)
        print(f"Datos guardados: {len(CHARACTER)} usuarios escritos en disco.")
    except Exception as e:
        print(f" Error al guardar datos: {e}")

def load_character():
    global CHARACTER
    if os.path.exists(USER_CHARACTER):
        try:
            with open(USER_CHARACTER, "r") as f:

                content = f.read().strip()
                if not content:
                    print(f"DEBUG: {USER_CHARACTER} está vacío.")
                    return

                data_from_json = json.loads(content)
                CHARACTER = {str(k): v for k, v in data_from_json.items()}
                print(f" Datos cargados: {len(CHARACTER)} usuarios en memoria.")

        except json.JSONDecodeError:
            print(" Error al leer el archivo JSON. Iniciando con diccionario vacío.")


#TAREAS DE LOS USUARIOS REGISTRADOS
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

def load_tasklist():
    global TASKLIST
    if os.path.exists(USERS_TASK_LIST):
        try:
            with open(USERS_TASK_LIST, "r") as f:

                content = f.read().strip()
                if not content:
                    print(f"DEBUG: {USERS_TASK_LIST} está vacío.")
                    return


                data_from_json = json.loads(content)
                TASKLIST = {str(k): v for k, v in data_from_json.items()}
                print(f"Tareas cargadas de {len(TASKLIST)} usuarios")

        except json.JSONDecodeError:
            print(f"Error al cargar las tareas")


def save_tasklist():
    global TASKLIST
    try:
        with open(USERS_TASK_LIST, "w") as f:
            json.dump(TASKLIST,f,indent=4)
            print(f"Tareas guardadas de {len(TASKLIST)} usuarios")

    except Exception as e:
        print(f"Error al guardar las tareas {e}")

#REGISTERES USERS' REMINDERS
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
def load_reminders():
    global REMINDERS

    if os.path.exists(USERS_REMINDERS_FILE):
        try:
            with open(USERS_REMINDERS_FILE, "r") as f:
                REMINDERS= json.load(f)
                print(f"Recordatorios cargados de {len(REMINDERS)} usuarios")
        except json.JSONDecodeError:
            print(f"Error al cargar los recordatorios")
            REMINDERS = {}

def save_reminders(chat_id, datos_json):
    global REMINDERS

    str_chat_id = str(chat_id)

    if str_chat_id not in REMINDERS:
        REMINDERS[str_chat_id] = {"reminders" : []}
    
    REMINDERS[str_chat_id]["reminders"].append(datos_json)

    try:
        with open(USERS_REMINDERS_FILE, "w") as f:
            json.dump(REMINDERS,f, indent=4)
            print(f"Recordarios guardados del usuario {str_chat_id})")

    except Exception as e:
        print(f"Error al guardar los recordatorios {e}")
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

def load_data():
    load_users()
    load_character()
    load_tasklist()
    load_reminders()

atexit.register(save_users)
atexit.register(save_character)
atexit.register(save_tasklist)
atexit.register(save_reminders)
