from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler


import data.persistence as persistence

def generate_character_id(character):
    character_list = ["male_warrior","female_warrior","male_mage","female_mage"]

    if character in character_list:
        return character_list.index(character) + 1
        

generate_character_id("male_warrior")