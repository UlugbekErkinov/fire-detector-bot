import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the 'start' command handler
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hi there! I will notify you in case of fire. I am developed by Ulugbek Erkinov.")

# Define the 'check' command handler
def check(update: Update, context: CallbackContext):
    # Simulate the check for fire condition (dummy function)
    is_fire = is_fire_detected()

    if is_fire:
        message = "Fire detected in the room!"
    else:
        message = "No fire detected in the room."

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def is_fire_detected():
    #dummy function
    import random
    return random.choice([True, False])

def main():
    # Set up the Telegram bot
    updater = Updater(token='6071167249:AAEYaJLYR4MjXD9EyGB3mjiDj3JpOGF2r3I', use_context=True)
    dispatcher = updater.dispatcher

    # Add command handlers
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    check_handler = CommandHandler('check', check)
    dispatcher.add_handler(check_handler)

    # Start the bot
    updater.start_polling()
    logger.info("Bot started.")

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
