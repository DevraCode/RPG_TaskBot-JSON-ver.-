import datetime
from telegram import Update

#LOCAL IMPORTS
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
import data.persistence as persistence
from data.time_zone import ZONE
from data.security import generate_id, verify_user


#BASIC FUNCTIONS
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

#Inicia el bot
async def start(update:Update, context):

    chat_id = update.effective_chat.id #Obtiene el id del chat
    user = update.effective_user.first_name #Obtiene el nombre del usuario
    
    user_id = generate_id(chat_id) #Id del usuario que va a ser almacenada
   

    if user_id not in persistence.REGISTERED_USERS:

        persistence.REGISTERED_USERS[user_id] = {
            'user_id': user_id,
            'user': user,
            'fecha_registro': str(datetime.datetime.now(ZONE))
        }

        persistence.TASKLIST[user_id] = {
            "pending_tasks": [],
            "completed_tasks": []
        }

        await context.bot.send_message(chat_id = chat_id, text=f"Hola, {user}. \nElige a un personaje para comenzar tu aventura. \nPara ello, busca el comando /characters en el menú, pulsa sobre él en este mismo mensaje o escríbelo directamente")
        print(f"DEBUG: Nuevo usuario registrado: {user}")


    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Ya estás registrado. Usa el menú para ver las opciones disponibles"
        )
    
    for key in persistence.REGISTERED_USERS:
            print(f"{key}")



#---------------------------------------------------------------------------------------------------

#Función que borra al usuario del bot, su personaje, su lista de tareas y sus recordatorios
@verify_user
async def delete_user(update:Update, context, user_id):
        
    persistence.REGISTERED_USERS.pop(user_id)
    persistence.TASKLIST.pop(user_id)
    persistence.CHARACTER.pop(user_id)
    
    await update.message.reply_text(f"Usuario borrado con éxito")

    #---------------------------------------------------------------------------------------------------
