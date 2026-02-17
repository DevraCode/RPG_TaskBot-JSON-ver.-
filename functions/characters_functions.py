from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMedia
from telegram.ext import CallbackContext, ConversationHandler

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
import data.persistence as persistence
from data.security import verify_user, not_character_selected, has_character_selected
from functions.basic_functions import generate_id
from functions.characters_data import male_warrior_01, female_warrior_01, male_mage_01, female_mage_01, male_monk_01, female_monk_01, male_archer_01, female_archer_01
from functions.characters_data import male_warrior, female_warrior, male_mage, female_mage, male_monk, female_monk, male_archer, female_archer

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

#Lista de personajes
character_list = [male_warrior_01, female_warrior_01, male_mage_01, female_mage_01, male_monk_01, female_monk_01, male_archer_01, female_archer_01]

#Esto enlaza los personajes con sus respectivas funciones
character_select = {
    male_warrior_01: male_warrior,
    female_warrior_01: female_warrior,
    male_mage_01 : male_mage,
    female_mage_01: female_mage,
    male_monk_01: male_monk,
    female_monk_01: female_monk,
    male_archer_01: male_archer,
    female_archer_01: female_archer
}

character_type = ["Guerrero", "Guerrera", "Mago", "Maga", "Monje", "Monja", "Arquero", "Arquera"] #Clases de personajes

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

#Muestra el primer personaje de la lista, y a partir de ahi, los demás
@verify_user
@has_character_selected
async def show_characters(update: Update, context: CallbackContext, user_id):
    
    chat_id = update.effective_chat.id
    
    index = 0  #La posición del primer personaje de la lista

    #Botones de Anterior, Siguiente y Seleccionar
    keyboard = [
            [InlineKeyboardButton(character_type[index], callback_data="ignore")],
            [
                InlineKeyboardButton("Anterior", callback_data=f"PREV_{index}"),
                InlineKeyboardButton("Siguiente", callback_data=f"NEXT_{index}")
            ],
            [InlineKeyboardButton("Seleccionar", callback_data=f"SELECT_{index}")]
        ]
    
    #Enviamos el primer personaje de la galería
    await context.bot.send_sticker(
            chat_id=chat_id,
            sticker=character_list[index],
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


#Manejador de botones
async def characters_buttons(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "ignore":
        await query.answer()
        return

    await query.answer() 
 
    data = query.data.split("_") #Split para que separe el data y obtenga NEXT O PREV con el índice separado ([NEXT, 0] [PREV, 0])
    accion = data[0] #Primera posición de los data obtenidos, o sea, NEXT o PREV
    indice_actual = int(data[1]) #Se convierte a int la segunda posición del data obtenido, que fue 0, que se guardó en la variable index de la función anterior

    #Calculamos los índices
    if accion == "NEXT":
        nuevo_indice = (indice_actual + 1) % len(character_list) #Pasará a NEXT_1, NEXT_2...etc. Y pasa al siguiente personaje
    elif accion == "PREV":
        nuevo_indice = (indice_actual - 1) % len(character_list)#Pasará a PREV_1, PREV_2... Y pasa al anterior personaje
    else:
        nuevo_indice = indice_actual

        for i,character in enumerate(character_select):
            if i == nuevo_indice:
                character_selected = list(character_select.values())[i]
                await character_selected(update,context)
        return

    #Borra el Sticker actual y muestra el siguiente, dando la sensación de dinamismo 
    await query.message.delete()
        
    #Creamos el nuevo teclado con el nuevo índice que mostrará al siguiente o al anterior personaje
    nuevo_keyboard = [
        [InlineKeyboardButton(character_type[nuevo_indice], callback_data="ignore")],
        [
            InlineKeyboardButton("Anterior", callback_data=f"PREV_{nuevo_indice}"),
            InlineKeyboardButton("Siguiente", callback_data=f"NEXT_{nuevo_indice}")
        ],
            [InlineKeyboardButton("Seleccionar", callback_data=f"SELECT_{nuevo_indice}")]
        ]

    #Se envía el nuevo personaje
    await context.bot.send_sticker(
        chat_id=query.message.chat_id,
        sticker=character_list[nuevo_indice],
        reply_markup=InlineKeyboardMarkup(nuevo_keyboard)
        )
    
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
@not_character_selected
async def character_status(update:Update,context):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)
    
    name = persistence.CHARACTER[user_id]['character_name']
    type = persistence.CHARACTER[user_id]['character_type']
    level = persistence.CHARACTER[user_id]['character_level']
    exp = persistence.CHARACTER[user_id]['character_exp']

    mensaje = f"Nombre: {name}" + "\n" + f"{type}" + "\n" + f"Nivel: {level}" + "\n" + f"EXP: {exp}"

    await update.effective_chat.send_sticker(sticker=persistence.CHARACTER[user_id]['character_img'])
    await update.effective_message.reply_text(mensaje)



def character_exp_up(user_id):
    user_completed_tasks = persistence.TASKLIST[user_id]["completed_tasks"]
    contador = 0

    for task in user_completed_tasks:
        contador+=150

    exp = str(contador)
    persistence.CHARACTER[user_id]["character_exp"] = contador
    
def character_level_up(user_id, character_exp):
    
    current_level = persistence.CHARACTER[user_id]["character_level"]

    exp_needed = current_level * 1000 #EXP necesaria para el siguiente nivel

    if character_exp >= exp_needed: 
        new_level = current_level + 1
        persistence.CHARACTER[user_id]["character_level"] = new_level

        return True #Devuelve true si se cumple la condición
    
    return False


def character_evolution(user_id, character_level):
    
    needed_character_level = 2 
    

    #Si el nivel actual del personaje supera al necesario
    if character_level >= needed_character_level: 
        print(f"{needed_character_level} Funciona")

        return True
    
    return False


