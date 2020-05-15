# -*- coding: utf-8 -*-
"""
Robert Chase would help during major incident resolution to remember who needs to be chased.

@author: ilyinily
"""
# Подключаем модуль случайных чисел
import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('1144691083:AAG27f-0p3aUftFXsnKjYpGpNYAbmjibIbQ')

# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

# Заготовки для трёх предложений
first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    # Если написали «Привет»

    if message.text == "Hi" or "Привет" or "Йо" or "Yo":

        # Пишем приветствие

        bot.send_message(message.from_user.id, "Wassup, I will be your helper in major incident management.")

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup(row_width = 2)

        # По очереди готовим текст и обработчик для каждой кнопки

        key_top_left = types.InlineKeyboardButton(text='WB', callback_data='whiteboard_menu')
        #keyboard.add(key_top_left)

        key_middle_left = types.InlineKeyboardButton(text='Impact', callback_data='impact_menu')
        #keyboard.add(key_middle_left)

        key_bottom_left = types.InlineKeyboardButton(text='Teams', callback_data='teams_menu')
        #keyboard.add(key_bottom_left)

        key_top_right = types.InlineKeyboardButton(text='Solutions', callback_data='solutions_menu')
        #keyboard.add(key_top_right)

        key_middle_right = types.InlineKeyboardButton(text='Hypotheses', callback_data='hypotheses_menu')
        #keyboard.add(key_middle_right)

        key_bottom_right = types.InlineKeyboardButton(text='History', callback_data='History_menu')
        keyboard.add(key_top_left, key_top_right, key_middle_left, key_middle_right, key_bottom_left, key_bottom_right)
        """
        top_row = []
        top_row.append(key_top_left)
        top_row.append(key_top_right)
        middle_row = []
        middle_row.append(key_middle_left)
        middle_row.append(key_middle_right)
        bottom_row = []
        bottom_row.append(key_bottom_left)
        bottom_row.append(key_bottom_right)

        keyboard.add(top_row)
        keyboard.add
"""
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Choose your destiny (flawless victory).', reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Say 'Hi' to start")

    else:

        bot.send_message(message.from_user.id, "Don't get it. I'm not as smart as Marta. Type /help.")


# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):
    if call.data == "whiteboard_menu":
        msg = "Here's what we can do with the whiteboard itself."
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "impact_menu":
        msg = "Here's what we can do with the business impact."
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "teams_menu":
        msg = "Here's what we can do with teams involved."
        bot.send_message(call.message.chat.id, msg)

# Запускаем постоянный опрос бота в Телеграме

bot.polling(none_stop=True, interval=0)
