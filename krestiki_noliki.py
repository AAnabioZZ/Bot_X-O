from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update

import krestiki_noliki
from krestiki_noliki import *

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


def check_int(st:str)->int:
    try:
        int(st)
        if int(st) >0<10:
            return int(st)
        else: return check_int(input('Ошибка ввода, попробуйте снова: '))
    except:
        return check_int(input('Ошибка ввода, попробуйте снова: '))


def convert_to_index(a:int)->int:
    a=int(a)
    if a == 1:
        return 2
    elif a == 2:
        return 8
    elif a == 3:
        return 14
    elif a == 4:
        return 38
    elif a == 5:
        return 44
    elif a == 6:
        return 50
    elif a == 7:
        return 74
    elif a == 8:
        return 80
    elif a == 9:
        return 86
    else:
        return convert_to_index(check_int(input('Некорректный ввод\n'
                                      'Введите номер свободной ячейки: ')))


def hodd(pol: str,hod: int, play: str) -> str:
    if pol[hod] != '❌' and pol[hod] != '⭕':
        pol = pol[:hod]+play+pol[hod+1:]
    else:
        hod=convert_to_index(check_int(input('Эта ячейка занято повторите выбор:')))
        return hodd(pol,hod,play)
    return pol


def winer(pol:str):
    p1,p2,p3,p4,p5,p6,p7,p8,p9=2,8,14,38,44,50,74,80,86
    if pol[p1] == pol[p2] ==pol[p3]:
        return True
    elif pol[p4] == pol[p5] ==pol[p6]:
        return True
    elif pol[p7] == pol[p8] ==pol[p9]:
        return True
    elif pol[p1] == pol[p4] ==pol[p7]:
        return True
    elif pol[p2] == pol[p5] ==pol[p8]:
        return True
    elif pol[p3] == pol[p6] ==pol[p9]:
        return True
    elif pol[p1] == pol[p5] ==pol[p9]:
        return True
    elif pol[p3] == pol[p5] ==pol[p7]:
        return True
    else: return False


def chei_hod(count_hod:int):
    if count_hod %2 == 0 :
        return '❌'
    else: return '⭕'

# polosa='-----------------'
# pole= '  1  |  2  |  3  \n'+polosa+'\n  4  |  5  |  6  \n'+polosa+'\n  7  |  8  |  9  '
# count=0
# win=False
# print('\n'*20+f'Привет сиграем в крестики нолики ?\nТебе понадобится апонент так что ищи друга')
# print('Приступим')
#
# while not win and count<9:
#     print(pole)
#     play=chei_hod(count)
#     shag=convert_to_index(check_int(input(f'Cейчас ходит{play}\nКуда ставим{play}?: ')))
#     pole=hodd(pole,shag,play)
#     win=winer(pole)
#     count+=1
#     print('\n'*20)
#
# if win:
#     print(f'Спустя {count} ходов,\nпобедил {chei_hod(count-1)} поздравляем!\n\n{pole}')
#     input("для выхода нажмити Ввод ")
# else:
#     print(f'{pole}\n!Победила дружба!')
#     input("для выхода нажмити Ввод ")