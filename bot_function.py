
from krestiki_noliki import *
from telegram.ext import ConversationHandler
FIRST_STEP, STEP = range(2)


def start(update, context):
    # print(context.user_data)
    context.user_data.clear()
    # reply_keyboard = KEYS_M
    markup_key = ReplyKeyboardMarkup([['С другом']], one_time_keyboard=True)
    update.message.reply_text("Тебе нужен соперник, оглянись , "
                              "есть подходяшие кондидатуры?", reply_markup=markup_key)
    return FIRST_STEP


def first_step(update, context):
    polosa = '-----------------'
    pole = '  1  |  2  |  3  \n' + polosa + '\n  4  |  5  |  6  \n' + polosa + '\n  7  |  8  |  9  '
    context.user_data['pole'] = pole

    context.user_data['win'] = False
    context.user_data['count_step'] = 0
    context.user_data['player'] = krestiki_noliki.chei_hod(context.user_data['count_step'])
    markup_key = ReplyKeyboardMarkup([[1,2,3], [4,5,6], [7,8,9]], one_time_keyboard=True)
    update.message.reply_text(f"{context.user_data['pole']}\nпервым ходит {context.user_data['player']} "
                              f"куда его поставим?", reply_markup=markup_key)

    return STEP


def step(update, context):
    hod = update.message.text
    try:
        int(hod)
        if int(hod) >0<10:
            context.user_data['pole']=krestiki_noliki.hodd(context.user_data['pole'],
                                                           krestiki_noliki.convert_to_index(hod),
                                                           context.user_data['player'])
            context.user_data['win']=krestiki_noliki.winer(context.user_data['pole'])
            context.user_data['count_step'] += 1
        else:
            update.message.reply_text('Что то не так , такой ячейки нету\nПопробуй еще раз')
            return STEP
    except:
        update.message.reply_text('Непонятно, попробуйте еще раз')
        return STEP
    if context.user_data['win'] or not context.user_data['count_step'] <9:
        if context.user_data['win']:
            update.message.reply_text(f"Спустя {context.user_data['count_step']} ходов,\nпобедил "
                                      f"{context.user_data['player']} поздравляем!\n\n{context.user_data['pole']}")
            update.message.reply_text('До новых встреч, приходите еще! %))')
            return ConversationHandler.END
        else:
            update.message.reply_text(f"{context.user_data['pole']}\n!Победила дружба!")
            update.message.reply_text('До новых встреч, приходите еще!')
            return ConversationHandler.END
    context.user_data['player'] = krestiki_noliki.chei_hod(context.user_data['count_step'])
    markup_key = ReplyKeyboardMarkup([[1, 2, 3], [4, 5, 6], [7, 8, 9]], one_time_keyboard=True)
    update.message.reply_text(f"{context.user_data['pole']}\nтеперь ходит {context.user_data['player']} "
                              f"куда его поставим?", reply_markup=markup_key)
    return STEP


def cancel(update, context):
    update.message.reply_text(
        'до новых встреч!',
        reply_markup=ReplyKeyboardRemove()
    )
    print(context.user_data)
    return ConversationHandler.END