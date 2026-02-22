import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, filters


#LOCAL IMPORTS
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
import data.persistence as persistence
from data.time_zone import ZONE, DIAS
from functions.basic_functions import start, delete_user
from functions.task_functions import TASK_NAME, DELETE, COMPLETE
from functions.task_functions import new_task, add_task, show_pending_tasks, delete_task, delete_button, cancel, complete_task, complete_button
from functions.menu import menu

from functions.characters_functions import show_characters, characters_buttons, character_status

#BOT TOKEN
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("El token de Telegram no se encontró. Asegúrate de que BOT_TOKEN esté definido en el archivo .env.")


#MAIN FUNCTION
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#Main function. Build the bot and store handlers
def main():
    #---------------------------------------------------------------------------------------------------
    persistence.load_data() #load user´s data
  
    #--------------------------------------------------------------------------------------------------- 
    app = ApplicationBuilder().token(BOT_TOKEN).post_init(menu).build()


    #Handlers
    #---------------------------------------------------------------------------------------------------
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("showtasks", show_pending_tasks))
    app.add_handler(CommandHandler("deluser", delete_user))

    app.add_handler(CommandHandler("characters", show_characters))
    app.add_handler(CallbackQueryHandler(characters_buttons, pattern="^(NEXT_|PREV_|SELECT_)"))
    app.add_handler(CommandHandler("status", character_status))



    #Conversation Handlers
    #---------------------------------------------------------------------------------------------------
    add_task_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("addtask", new_task)],
        states = {
            TASK_NAME: [MessageHandler(filters.TEXT & (~filters.COMMAND), add_task)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        per_message=False)
    
    
    del_task_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("deltask", delete_task)],
        states = {
            DELETE: [CallbackQueryHandler(delete_button)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        per_message=False)
    
    complete_task_handler = ConversationHandler(
        entry_points=[CommandHandler("comtask", complete_task)],
        states = {
            COMPLETE: [CallbackQueryHandler(complete_button)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        per_message=False)
    
      
    
    
    
    app.add_handler(add_task_conv_handler)
    app.add_handler(del_task_conv_handler)
    app.add_handler(complete_task_handler)
    

   

   #---------------------------------------------------------------------------------------------------
    app.run_polling()



#BOT RUNNING
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#Si el nombre del script coincide con main comienza el bot
if __name__ == "__main__":
    main()