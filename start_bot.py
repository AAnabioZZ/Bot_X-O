g_token = "5502983826:AAHqnDHCxzwFkZeJI08dxeLk0XNniSUrbMY"
from bot_function import (FIRST_STEP,STEP,first_step,cancel,start,step)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(g_token)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    conv_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            FIRST_STEP: [MessageHandler(Filters.regex('^(С другом|С Ботом)$'), first_step)],
            STEP: [MessageHandler(Filters.text & ~Filters.command, step)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()