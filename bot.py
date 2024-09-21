from telegram import Updatefrom telegram.ext import Updater, CommandHandler, CallbackContext
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('SPW сервер ублюдков')
def main() -> None:    updater = Updater("8184725973:AAGoywBfX2hanNGW0vwDBkUj3-jGWMIm-l4", use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
if name == '__main__':    main()