from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
import data.persistence as persistence
from functions.basic_functions import generate_id

#Función para mostrar la galeria de personajes
async def show_characters(update:Update,context:CallbackContext):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)

    keyboard = []

    #Se comprueba que el usuario existe, si existe, se le muestra la galeria
    if user_id not in persistence.CHARACTER[user_id]:
        await context.bot.send_message(chat_id=chat_id, text=f"Debes registrarte primero")

    else:
        
        buttons = [
            InlineKeyboardButton("Next", callback_data="NEXT")
        ]

        keyboard.append(buttons)
        reply_markup = InlineKeyboardMarkup(keyboard)
        

