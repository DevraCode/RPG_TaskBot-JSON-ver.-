from telegram import Update

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
import data.persistence as persistence
from functions.basic_functions import generate_id


#DEFINIR PERSONAJES
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
             'character_id': "01",
             'character_name':user,
             'character_img': "assets/characters/warrior/male_warrior_01.webm",
             'character_type':"male_mage",
             'character_exp': 0,
             'character_level': 0
    }

    name = persistence.CHARACTER[user_id]['character_name']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

    await context.bot.send_sticker(chat_id = chat_id, sticker = persistence.CHARACTER[user_id]['character_img'])
    await context.bot.send_message(chat_id=chat_id, text=mensaje)


#Guerrera
async def female_warrior(update:Update,context):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)
    user = update.effective_user.first_name

    persistence.CHARACTER[user_id] = {
             'character_id': "01",
             'character_name':user,
             'character_img': "assets/characters/warrior/female_warrior_01.webm",
             'character_type':"male_mage",
             'character_exp': 0,
             'character_level': 0
    }

    name = persistence.CHARACTER[user_id]['character_name']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

    await context.bot.send_sticker(chat_id = chat_id, sticker = persistence.CHARACTER[user_id]['character_img'])
    await context.bot.send_message(chat_id=chat_id, text=mensaje)


#MAGOS
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

#Mago
async def male_mage(update:Update,context):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)
    user = update.effective_user.first_name

    persistence.CHARACTER[user_id] = {
             'character_id': "01",
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

    await context.bot.send_sticker(chat_id = chat_id, sticker = persistence.CHARACTER[user_id]['character_img'])
    await context.bot.send_message(chat_id=chat_id, text=mensaje)

#Maga
async def female_mage(update:Update,context):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)
    user = update.effective_user.first_name

    persistence.CHARACTER[user_id] = {
             'character_id': "01",
             'character_name':user,
             'character_img': "assets/characters/mage/female_mage_01.webm",
             'character_type':"male_mage",
             'character_exp': 0,
             'character_level': 0
    }

    name = persistence.CHARACTER[user_id]['character_name']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

    await context.bot.send_sticker(chat_id = chat_id, sticker = persistence.CHARACTER[user_id]['character_img'])
    await context.bot.send_message(chat_id=chat_id, text=mensaje)


