# -*- coding: utf-8 -*-
"""
Robert Chase would help during major incident resolution to remember who needs to be chased.

@author: ilyinily
"""
# Подключаем модуль случайных чисел
import random
# And the module to use emoji
from emoji import emojize
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('1144691083:AAG27f-0p3aUftFXsnKjYpGpNYAbmjibIbQ')

# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

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
        key_top_left = types.InlineKeyboardButton(text=emojize(':volcano: WB :volcano:'), callback_data='whiteboard_menu')
        key_middle_left = types.InlineKeyboardButton(text=emojize(':heavy_dollar_sign: Impact :heavy_dollar_sign:'), callback_data='impact_menu')
        key_bottom_left = types.InlineKeyboardButton(text=emojize(':two_men_holding_hands: Teams :two_men_holding_hands:'), callback_data='teams_menu')
        key_top_right = types.InlineKeyboardButton(text=emojize(':scroll: Solutions :scroll:'), callback_data='solutions_menu')
        key_middle_right = types.InlineKeyboardButton(text=emojize(':thought_balloon: Hypotheses :thought_balloon:'), callback_data='hypotheses_menu')
        key_bottom_right = types.InlineKeyboardButton(text=emojize(':books: History :books:'), callback_data='history_menu')
        keyboard.add(key_top_left, key_top_right, key_middle_left, key_middle_right, key_bottom_left, key_bottom_right)

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
        # Готовим кнопки
        keyboard = types.ReplyKeyboardMarkup(row_width = 2, one_time_keyboard = True)

        # По очереди готовим текст и обработчик для каждой кнопки
        key_top_left = types.InlineKeyboardButton(text='New WB', callback_data='new_whiteboard')
        key_middle_left = types.InlineKeyboardButton(text='Crisis Call Started', callback_data='crisis_call_started')
        key_bottom_left = types.InlineKeyboardButton(text='List WB History', callback_data='whiteboard_history')
        key_top_right = types.InlineKeyboardButton(text='Priority Changed', callback_data='priority_changed')
        key_middle_right = types.InlineKeyboardButton(text='Correction WB Sent', callback_data='correction_whiteboard_sent')
        key_bottom_right = types.InlineKeyboardButton(text='Back', callback_data='whiteboard_back')
        keyboard.add(key_top_left, key_top_right, key_middle_left, key_middle_right, key_bottom_left, key_bottom_right)

        bot.send_message(call.message.chat.id, msg, reply_markup = keyboard)
    elif call.data == "impact_menu":
        msg = "Here's what we can do with the business impact."
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "teams_menu":
        msg = "Here's what we can do with teams involved."
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "solutions_menu":
        msg = "Here's what we can do with solutions."
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "hypotheses_menu":
        msg = "Here's what we can do with hypotheses."
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "history_menu":
        msg = "Here's what we can do with history."
        bot.send_message(call.message.chat.id, msg)

# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)


