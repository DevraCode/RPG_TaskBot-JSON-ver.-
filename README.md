# <img width="99" height="101" alt="espadas-ezgif com-gif-maker (1) (1)" src="https://github.com/user-attachments/assets/2b223684-1a8c-4892-b718-ee356fbfa3a1" /> RPG TaskBot <img width="99" height="101" alt="espadas-ezgif com-gif-maker (1) (1)" src="https://github.com/user-attachments/assets/16710121-78cc-4480-9579-0dad964cc930" />
## Spanish

### Importante
Este bot está diseñado para usarlo de forma casera con pocos usuarios, ya que los datos (encriptados) se guardan en archivos JSON. Evidentemente, no aguantará muchas conexiones simultáneas al mismo tiempo.
Para la escalabilidad del bot, lo suyo es migrar a una base de datos y que una API te proporcione los datos de los personajes (Cosa que haré en un futuro).

### ¿Por qué un bot de tareas RPG?
La idea de este bot surge de la necesidad de mejorar la productividad mediante tareas y recordatorios, con un enfoque divertido para motivar al usuario.
Como si un juego de rol se tratase, el usuario eligirá a uno de los personajes disponibles y subirá de nivel a medida que vaya completando tareas.

### Iniciando el bot
Para empezar a utilizar el bot, el usuario deberá buscar @RPG_Taskbot en el buscador de Telegram
![Telegram_bot1](https://github.com/user-attachments/assets/e787f25c-07a3-4ab6-bdcd-2543ce6ff45e)

Al abrir el chat con el bot, click en Iniciar y se abrirá automáticamente el comando /start

![Telegram_bot2_edited](https://github.com/user-attachments/assets/905aeb3a-c74e-4e91-ab9e-e5f22303c876)


Y el bot responderá con un mensaje de bienvenida al usuario, en el que saludará al mismo (mi nombre de usuario está censurado en la imagen) y le explicará brevemente como elegir un personaje.

![Telegram_bot3_edited_2](https://github.com/user-attachments/assets/69a6a570-c33c-435e-add4-6093588cefed)

### Comandos del bot
/start -> Inicializa el bot y almacena al usuario y sus datos en un archivo JSON 

/addtask (nombre de la tarea) -> Añade una tarea como argumento tras el comando a la lista de tareas. Ej: /addtask Hacer la compra  
/showtasks -> Muestra la lista de tareas pendientes del usuario  
/comtask -> Muestra la lista de tareas pendientes y permite marcar las tareas realizadas como completadas  
/deltask -> Permite eliminar una tarea de la lista de tareas pendientes  
/reminder -> Establece un recordatorio los días seleccionados  
/deluser -> Elimina completamente al usuario del bot, con sus tareas y recordatorios  

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## English

### Important
This bot is designed for home use with few users, as the (encrypted) data is stored in JSON files. Obviously, it will not be able to handle many simultaneous connections at the same time.
For the bot to be scalable, it would be best to migrate to a database and have an API provide you with the character data (which I will do in the future).
The idea for this bot arose from the need to improve productivity through tasks and reminders, with a fun approach to motivate the user. 
As if it were a role-playing game, the user will choose one of the available characters and level up as they complete tasks.

### Why an RPG task bot?
The idea for this bot arose from the need to improve productivity through tasks and reminders, with a fun approach to motivate the user.
As if it were a role-playing game, the user will choose one of the available characters and level up as they complete tasks.

### Starting the bot
To start using the bot, the user must search for @RPG_Taskbot in the Telegram search engine.
![Telegram_bot1](https://github.com/user-attachments/assets/42e78bdf-78a9-41d2-944b-b9a5515a8795)

### Bot commands
/start -> Initializes the bot and stores the user and their data in a JSON file  
/addtask (task name) -> Adds a task as an argument after the command to the task list. E.g.: /addtask Do the shopping  
/showtasks -> Shows the user's list of pending tasks  
/comtask -> Shows the list of pending tasks and allows you to mark completed tasks as done  
/deltask -> Allows you to remove a task from the list of pending tasks  
/reminder -> Sets a reminder for the selected days  
/deluser -> Completely removes the user from the bot, along with their tasks and reminders  





