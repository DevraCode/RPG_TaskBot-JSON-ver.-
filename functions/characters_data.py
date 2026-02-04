from telegram import Update

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
import data.persistence as persistence
from functions.basic_functions import generate_id


#DEFINIR PERSONAJES

#Definimos las rutas de las imágenes de los personajes que se usaran para la función show_characters definida en characters_functions.py y SOLO PARA MOSTRAR
male_warrior_01 = "assets/characters/warrior/male_warrior_01.webm"
female_warrior_01 ="assets/characters/warrior/female_warrior_01.webm"
male_mage_01 = "assets/characters/mage/male_mage_01.webm"
female_mage_01 ="assets/characters/mage/female_mage_01.webm"


#Definimos las funciones que rellenan el json de los personajes al seleccionarlos
#GUERREROS
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#Guerrero
async def male_warrior(update:Update,context):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)
    user = update.effective_user.first_name

    persistence.CHARACTER[user_id] = {
             'character_name':user,
             'character_img': "assets/characters/warrior/male_warrior_01.webm",
             'character_type':"male_warrior",
             'character_exp': 0,
             'character_level': 0
    }

    name = persistence.CHARACTER[user_id]['character_name']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

    await update.effective_chat.send_sticker(sticker=persistence.CHARACTER[user_id]['character_img'])
    await update.effective_message.reply_text(mensaje)


#Guerrera
async def female_warrior(update:Update,context):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)
    user = update.effective_user.first_name

    persistence.CHARACTER[user_id] = {
             'character_name':user,
             'character_img': "assets/characters/warrior/female_warrior_01.webm",
             'character_type':"female_warrior",
             'character_exp': 0,
             'character_level': 0
    }

    name = persistence.CHARACTER[user_id]['character_name']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

    await update.effective_chat.send_sticker(sticker=persistence.CHARACTER[user_id]['character_img'])
    await update.effective_message.reply_text(mensaje)


#MAGOS
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

#Mago
async def male_mage(update:Update,context):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)
    user = update.effective_user.first_name

    persistence.CHARACTER[user_id] = {
             'character_name':user,
             'character_img': "assets/characters/mage/male_mage_01.webm",
             'character_type':"male_mage",
             'character_exp': 0,
             'character_level': 0
    }

    name = persistence.CHARACTER[user_id]['character_name']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

    await update.effective_chat.send_sticker(sticker=persistence.CHARACTER[user_id]['character_img'])
    await update.effective_message.reply_text(mensaje)

#Maga
async def female_mage(update:Update,context):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)
    user = update.effective_user.first_name

    persistence.CHARACTER[user_id] = {
             'character_name':user,
             'character_img': "assets/characters/mage/female_mage_01.webm",
             'character_type':"female_mage",
             'character_exp': 0,
             'character_level': 0
    }

    name = persistence.CHARACTER[user_id]['character_name']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

    await update.effective_chat.send_sticker(sticker=persistence.CHARACTER[user_id]['character_img'])
    await update.effective_message.reply_text(mensaje)


