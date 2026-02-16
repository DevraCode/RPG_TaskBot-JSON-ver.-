from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler


#LOCAL IMPORTS
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
import data.persistence as persistence
from data.security import generate_id, verify_user, has_character_selected

from functions.characters_functions import character_exp_up, character_level_up

import asyncio
#TASK FUNCTIONS
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

"""Añadir tarea"""
TASK_NAME = range(1)

#Pregunta primero el nombre de la tarea
@verify_user #Verifica que exista el usuario
@has_character_selected #Verifica que el usuario haya elegido personaje
async def new_task(update:Update, context:CallbackContext, user_id):
    await update.message.reply_text(f"Escribe un nombre para la tarea")
    return TASK_NAME
        

#Añade la tarea a la lista   
async def add_task(update:Update, context:CallbackContext):
    chat_id = update.effective_chat.id

    user_id = generate_id(chat_id) #Obtener el id del usuario

    task = update.message.text.strip().lower() #Se almacena en minúsculas

    if not task:
        await update.message.reply_text("El nombre no puede estar vacío. Inténtalo de nuevo:")
        return TASK_NAME

    #Comprobar que el usuario existe en el sistema
    if user_id in persistence.TASKLIST:

        #Si la tarea ya existe
        user_tasklist = persistence.TASKLIST[user_id]["pending_tasks"]

        if task in user_tasklist:
            await update.message.reply_text(f"{task.capitalize()} ya existe como tarea pendiente")
            return TASK_NAME

        #Si la tarea no existe, se crea y se añade a la lista
        else:
            user_tasklist.append(task)
            await update.message.reply_text(f"{task.capitalize()} añadido como tarea pendiente")
            return ConversationHandler.END

#---------------------------------------------------------------------------------------------------

"""Mostrar las tareas pendientes"""
async def show_pending_tasks(update:Update, context):

    chat_id = update.effective_chat.id

    user_id = generate_id(chat_id)

    #Si existe el usuario
    if user_id in persistence.TASKLIST:
        tasks = persistence.TASKLIST[user_id]["pending_tasks"]

        mensaje = f"📋 Tienes las siguientes tareas pendientes: \n\n"

        #Si no hay tareas pendientes
        if not tasks:
            await update.message.reply_text(text=f"No hay tareas para mostrar", parse_mode="MarkdownV2")
            return
        
        else:
            for task in tasks:
                mensaje += f"• ✨ {task.capitalize()}\n"
                
        await update.message.reply_text(mensaje, parse_mode="MarkdownV2")
            
    
    else:
        await context.bot.send_message(chat_id=chat_id, text=f"Usa el comando /start primero")


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

"""Borrar las tareas pendientes"""
DELETE = range(1) #Estado del ConversationHandler

#Función que solo muestra la lista de tareas pendientes como botones de teclado 
async def delete_task(update:Update, context:CallbackContext):

    chat_id = update.effective_chat.id

    user_id = generate_id(chat_id)

    #Si el usuario no existe o no tiene tareas pendientes
    if user_id not in persistence.TASKLIST or not persistence.TASKLIST[user_id].get("pending_tasks"):
        await update.message.reply_text("¡No tienes tareas pendientes para borrar!")
        return ConversationHandler.END 


    else:
        user_tasklist = persistence.TASKLIST[user_id]["pending_tasks"]
        keyboard = []
        
        #Crea una fila para cada tarea
        for task in user_tasklist:
                keyboard.append([InlineKeyboardButton(f"{task.capitalize()}", callback_data=task)])

        
        keyboard.append([InlineKeyboardButton("Cancelar", callback_data="CANCEL_DELETE")]) #Añade las filas al teclado en forma de botones
        reply_markup = InlineKeyboardMarkup(keyboard) #"Materaliza" el teclado visualmente
                
        await update.message.reply_text(text=f"Tienes las siguientes tareas pendientes, ¿Cual quieres borrar?:", reply_markup=reply_markup)
        return DELETE #Pasa al estado DELETE, que llama a la función delete_button

    
#Función que hace interactuables los botones
async def delete_button(update:Update, context:CallbackContext):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)

    
    query = update.callback_query #Almacena la opción escogida por el usuario y los datos del mismo
    await query.answer() #Elimina el estado de carga, se puede poner un mensaje entre los parentésis

    data = query.data #Obtiene los callback_data definidos en cada boton de la función delete_task, para condicionar las opciones mediante ifs


    user_tasklist = persistence.TASKLIST[user_id]["pending_tasks"]

    #Si el usuario existe
    if user_id in persistence.TASKLIST:

        #Si el usuario presionó "Cancelar"
        if data == "CANCEL_DELETE":
            await query.edit_message_text("Operación de eliminación de tareas cancelada.")
            return ConversationHandler.END

        #El usuario pulsa sobre una tarea de la lista y esta se eliminará
        if data in user_tasklist:
            user_tasklist.remove(data)

        if not user_tasklist:
        # No quedan tareas: Finalizar la conversación
            await query.edit_message_text("✅ ¡Todas las tareas han sido eliminadas! Conversación finalizada.")
            return ConversationHandler.END

        #IMPORTANTE: Por cada tarea borrada, se debe reconstruir el teclado, ya que Telegram no es dinámico, se debe hacer manualmente 
        keyboard = []
        for task in user_tasklist:
            keyboard.append([InlineKeyboardButton(f"{task.capitalize()}", callback_data=task)])
        
    keyboard.append([InlineKeyboardButton("Terminar Eliminación", callback_data="CANCEL_DELETE")]) #Se añade un botón de Terminar Eliminación
    reply_markup = InlineKeyboardMarkup(keyboard)

    #Se edita el primer mensaje
    await query.edit_message_text(
        "Tarea eliminada. Toca otra para seguir borrando:",
        reply_markup=reply_markup
    )

    return DELETE



#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

"""Completar las tareas"""
COMPLETE = range(1)

async def complete_task(update:Update, context:CallbackContext):

    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)

    if user_id not in persistence.TASKLIST or not persistence.TASKLIST[user_id].get("pending_tasks"):
        await update.message.reply_text("¡No tienes tareas pendientes para completar!")
        return ConversationHandler.END 

    else:
        user_tasklist = persistence.TASKLIST[user_id]["pending_tasks"]
        keyboard = []
        
        #Crear una nueva fila para cada tarea
        for task in user_tasklist:
                keyboard.append([InlineKeyboardButton(f"{task.capitalize()}", callback_data=task)])

        
        keyboard.append([InlineKeyboardButton("Cancelar", callback_data="CANCEL_DELETE")])
        reply_markup = InlineKeyboardMarkup(keyboard)
                
        await update.message.reply_text(text=f"Selecciona las tareas que quieres marcar como completadas:", reply_markup=reply_markup)
        return COMPLETE
    

def auxiliar_exp_button(data: str) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("+150 EXP", callback_data=data)]
    ]

    return InlineKeyboardMarkup(keyboard)


async def complete_button(update:Update, context:CallbackContext):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)

    query = update.callback_query
    await query.answer()

    data = query.data

    user_tasklist = persistence.TASKLIST[user_id]["pending_tasks"]
    user_completed_tasks = persistence.TASKLIST[user_id]["completed_tasks"]
    

    if user_id in persistence.TASKLIST:

        if data == "CANCEL_DELETE":
            await query.edit_message_text("Operación cancelada.")
            return ConversationHandler.END

        if data in user_tasklist:
            user_tasklist.remove(data)
            user_completed_tasks.append(data)
            character_exp_up(user_id)

            nuevo_teclado = auxiliar_exp_button(data)
            await query.edit_message_reply_markup(reply_markup=nuevo_teclado)
            await asyncio.sleep(1)

            

        if not user_tasklist:
            character_exp = persistence.CHARACTER[user_id]["character_exp"] 

            await query.edit_message_text(f"✅ Ya no quedan tareas pendientes para completar")

            await context.bot.send_message(chat_id=chat_id, text=f"Has acumulado {character_exp} EXP")
            
            if character_level_up(user_id):
               nuevo_nivel = persistence.CHARACTER[user_id]["character_level"]
               await context.bot.send_message(chat_id=chat_id, text=f"🎊 ¡Has subido al nivel {nuevo_nivel}! 🎊")

            return ConversationHandler.END
        

        


        keyboard = []
        for task in user_tasklist:
            keyboard.append([InlineKeyboardButton(f"{task.capitalize()}", callback_data=task)])
            
        
    keyboard.append([InlineKeyboardButton("Terminar", callback_data="CANCEL_DELETE")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        "Tarea marcada como completada. Toca otra para seguir completando tareas o finaliza la operación:",
        reply_markup=reply_markup
    )

    

    return COMPLETE


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text("Operacion cancelada.")
    return ConversationHandler.END
