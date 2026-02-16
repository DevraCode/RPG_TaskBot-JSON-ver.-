from telegram import Update
from telegram.ext import CallbackContext


import os
import hashlib

from dotenv import load_dotenv
from functools import wraps


import data.persistence as persistence

"""
Por seguridad, se encriptan los datos de los usuarios. De esta forma, se refuerza la seguridad del bot
"""

load_dotenv()
SECRET_WORD = os.getenv("SECRET_WORD") #Palabra secreta para encriptar el id del usuario, guardada en .env

#Función que genera un id único para cada usuario partiendo del chat id
def generate_id(chat_id):
    bin_id = f"{chat_id}{SECRET_WORD}".encode()
    id = hashlib.sha256(bin_id).hexdigest()
    return id[:12]


def verify_user(func):
    @wraps(func)
    async def verify(update:Update, context:CallbackContext, *args, **kwargs):
        chat_id = update.effective_chat.id
        user_id = generate_id(chat_id)

        if user_id not in persistence.REGISTERED_USERS:
            await context.bot.send_message(chat_id=chat_id, text=f"Debes ser usuario registrado")
            return
        return await func(update,context,user_id = user_id,*args,**kwargs)
    return verify


def not_character_selected(func):
    @wraps(func)
    async def verify_character(update:Update, context:CallbackContext, *args, **kwargs):
        chat_id = update.effective_chat.id
        user_id = generate_id(chat_id)

        if user_id not in persistence.CHARACTER:
            await context.bot.send_message(chat_id=chat_id, text=f"Debes elegir un personaje primero")
            return
        return await func(update,context,*args,**kwargs)
    return verify_character


def has_character_selected(func):
    @wraps(func)
    async def verify_character(update:Update, context:CallbackContext, *args, **kwargs):
        chat_id = update.effective_chat.id
        user_id = generate_id(chat_id)

        if user_id in persistence.CHARACTER:
            await context.bot.send_message(chat_id=chat_id, text=f"Ya tienes asignado un personaje")
            return
        return await func(update,context,*args,**kwargs)
    return verify_character

