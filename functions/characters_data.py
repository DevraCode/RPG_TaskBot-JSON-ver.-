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
male_monk_01 = "assets/characters/monk/male_monk_01.webm"
female_monk_01 = "assets/characters/monk/female_monk_01.webm"
male_archer_01 = "assets/characters/archer/male_archer_01.webm"
female_archer_01 = "assets/characters/archer/female_archer_01.webm"


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
             'character_type':"Guerrero",
             'character_gender' : 'male',
             'character_exp': 0,
             'exp_needed': 1000,
             'needed_lv' : 2,
             'character_level': 1
    }

    name = persistence.CHARACTER[user_id]['character_name']
    type = persistence.CHARACTER[user_id]['character_type']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"{type}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

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
             'character_type':"Guerrera",
             'character_gender' : 'female',
             'character_exp': 0,
             'exp_needed': 1000,
             'needed_lv' : 2,
             'character_level': 1
    }

    name = persistence.CHARACTER[user_id]['character_name']
    type = persistence.CHARACTER[user_id]['character_type']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"{type}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

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
             'character_type':"Mago",
             'character_gender' : 'male',
             'character_exp': 0,
             'exp_needed': 1000,
             'needed_lv' : 2,
             'character_level': 1
    }

    name = persistence.CHARACTER[user_id]['character_name']
    type = persistence.CHARACTER[user_id]['character_type']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"{type}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

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
             'character_type':"Maga",
             'character_gender' : 'female',
             'character_exp': 0,
             'exp_needed': 1000,
             'needed_lv' : 2,
             'character_level': 1
    }

    name = persistence.CHARACTER[user_id]['character_name']
    type = persistence.CHARACTER[user_id]['character_type']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"{type}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

    await update.effective_chat.send_sticker(sticker=persistence.CHARACTER[user_id]['character_img'])
    await update.effective_message.reply_text(mensaje)


#MONJES
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#Monje
async def male_monk(update:Update,context):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)
    user = update.effective_user.first_name

    persistence.CHARACTER[user_id] = {
             'character_name':user,
             'character_img': "assets/characters/monk/male_monk_01.webm",
             'character_type':"Monje",
             'character_gender' : 'male',
             'character_exp': 0,
             'exp_needed': 1000,
             'needed_lv' : 2,
             'character_level': 1
    }

    name = persistence.CHARACTER[user_id]['character_name']
    type = persistence.CHARACTER[user_id]['character_type']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"{type}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

    await update.effective_chat.send_sticker(sticker=persistence.CHARACTER[user_id]['character_img'])
    await update.effective_message.reply_text(mensaje)

#Monja 
async def female_monk(update:Update,context):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)
    user = update.effective_user.first_name

    persistence.CHARACTER[user_id] = {
             'character_name':user,
             'character_img': "assets/characters/monk/female_monk_01.webm",
             'character_type':"Monja",
             'character_gender' : 'female',
             'character_exp': 0,
             'exp_needed': 1000,
             'needed_lv' : 2,
             'character_level': 1
    }

    name = persistence.CHARACTER[user_id]['character_name']
    type = persistence.CHARACTER[user_id]['character_type']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"{type}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

    await update.effective_chat.send_sticker(sticker=persistence.CHARACTER[user_id]['character_img'])
    await update.effective_message.reply_text(mensaje)


#ARQUEROS
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#Arquero
async def male_archer(update:Update,context):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)
    user = update.effective_user.first_name

    persistence.CHARACTER[user_id] = {
             'character_name':user,
             'character_img': "assets/characters/archer/male_archer_01.webm",
             'character_type':"Arquero",
             'character_gender' : 'male',
             'character_exp': 0,
             'exp_needed': 1000,
             'needed_lv' : 2,
             'character_level': 1
    }

    name = persistence.CHARACTER[user_id]['character_name']
    type = persistence.CHARACTER[user_id]['character_type']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"{type}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

    await update.effective_chat.send_sticker(sticker=persistence.CHARACTER[user_id]['character_img'])
    await update.effective_message.reply_text(mensaje)

#Arquera
async def female_archer(update:Update,context):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)
    user = update.effective_user.first_name

    persistence.CHARACTER[user_id] = {
             'character_name':user,
             'character_img': "assets/characters/archer/female_archer_01.webm",
             'character_type':"Arquera",
             'character_gender' : 'female',
             'character_exp': 0,
             'exp_needed': 1000,
             'needed_lv' : 2,
             'character_level': 1
    }

    name = persistence.CHARACTER[user_id]['character_name']
    type = persistence.CHARACTER[user_id]['character_type']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']
    
    mensaje = f"Nombre: {name}" + "\n" + f"{type}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

    await update.effective_chat.send_sticker(sticker=persistence.CHARACTER[user_id]['character_img'])
    await update.effective_message.reply_text(mensaje)
    
