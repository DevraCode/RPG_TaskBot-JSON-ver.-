from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMedia
from telegram.ext import CallbackContext, ConversationHandler


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
import data.persistence as persistence
from data.security import verify_user
from functions.basic_functions import generate_id
from functions.characters_data import male_warrior_01, female_warrior_01, male_mage_01, female_mage_01
from functions.characters_data import male_warrior, female_warrior, male_mage, female_mage




#Lista de personajes
character_list = [male_warrior_01, female_warrior_01, male_mage_01, female_mage_01]

character_select = {
    male_warrior_01: male_warrior,
    female_warrior_01: female_warrior,
    male_mage_01 : male_mage,
    female_mage_01: female_mage
}

#Muestra el primer personaje de la lista, y a partir de ahi, los demás
@verify_user
async def show_characters(update: Update, context: CallbackContext):
    
    chat_id = update.effective_chat.id
    
    index = 0  #La posición del primer personaje de la lista
    
    #Botones de Anterior, Siguiente y Seleccionar
    keyboard = [
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
    