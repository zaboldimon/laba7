import telebot
from telebot import types
token ='5914702230:AAGxyrCJMu2svLtYAm05ZBp_U9xrLeunaEs'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", "/mtuci")
    bot.send_message(message.chat.id, 'Здравствуйте! Хотите узнать свежую информацию о МТУСИ?', reply_markup=keyboard)
@bot.message_handler(content_types=['want'])
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, ' /Switch_Week_even - переключить неделю на чётную \n /Switch_Week - переключить неделю на нечётную \n /mtuci - Сайт университета \n Далее запросы выбираются спомощью плиток, что достаточно удобно. Если у вас пропали плитки просто свичните недели. Приятного пользования, также не забывайте проверять актуальность рассписания на сайте: https://mtuci.ru/')
@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, 'Держите ссылку на сайт mtuci: https://mtuci.ru/')
@bot.message_handler(commands=['Switch_Week'])
def Switch_Week(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b_1 = types.KeyboardButton("Monday")
    b_2 = types.KeyboardButton("Tuesday")
    b_3 = types.KeyboardButton("Wednesday")
    b_4 = types.KeyboardButton("Thursday")
    b_5 = types.KeyboardButton("Friday")
    b_6 = types.KeyboardButton("All_Week")
    b_7 = types.KeyboardButton("Switch_Week_even")
    b_8 = types.KeyboardButton("Help")
    markup.add(b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8)
    bot.send_message(message.chat.id, text="{0.first_name}, Вы переключили кнопки на нечётную неделю.".format(message.from_user), reply_markup=markup)
@bot.message_handler(commands=['Switch_Week_even'])
def Switch_Week_even(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b_1 = types.KeyboardButton("Monday_even")
    b_2 = types.KeyboardButton("Tuesday_even")
    b_3 = types.KeyboardButton("Wednesday_even")
    b_4 = types.KeyboardButton("Thursday_even")
    b_5 = types.KeyboardButton("Friday_even")
    b_6 = types.KeyboardButton("All_Week_even")
    b_7 = types.KeyboardButton("Switch_Week")
    b_8 = types.KeyboardButton("Help")
    markup.add(b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8)
    bot.send_message(message.chat.id, text="{0.first_name}, Вы переключили кнопки на чётную неделю.".format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Хочу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b_1 = types.KeyboardButton("Monday_even")
        b_2 = types.KeyboardButton("Tuesday_even")
        b_3 = types.KeyboardButton("Wednesday_even")
        b_4 = types.KeyboardButton("Thursday_even")
        b_5 = types.KeyboardButton("Friday_even")
        b_6 = types.KeyboardButton("All_Week_even")
        b_7 = types.KeyboardButton("Switch_Week")
        b_8 = types.KeyboardButton("Help")
        markup.add(b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8)
        bot.send_message(message.chat.id, text="{0.first_name}. Я умею выводить расписание  группы БИН2201.".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="{0.first_name}. Для более подробной информации о работе со мной пишите /help или используйте плитки автоматических запросов.".format(message.from_user), reply_markup=markup)
    if (message.text == "Switch_Week"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b_1 = types.KeyboardButton("Monday")
        b_2 = types.KeyboardButton("Tuesday")
        b_3 = types.KeyboardButton("Wednesday")
        b_4 = types.KeyboardButton("Thursday")
        b_5 = types.KeyboardButton("Friday")
        b_6 = types.KeyboardButton("All_Week")
        b_7 = types.KeyboardButton("Switch_Week_even")
        b_8 = types.KeyboardButton("Help")
        markup.add(b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8)
        bot.send_message(message.chat.id, text="{0.first_name}, Вы переключили кнопки на нечётную неделю.".format(message.from_user), reply_markup=markup)
    elif (message.text == "Monday"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Нечётный Понедельник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Высшая математика(л) | Н-526 | 9:30 | Пискарёв С. И. \n ВВИТ(пр) | Н-324 | 11:20 | Колесников О. В. \n ВВИТ(пр) | Н-324 | 13:10 | Колесников О. В. \n   ".format(message.from_user), reply_markup=markup)
    elif (message.text == "Tuesday"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Нечётный Вторник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Высшая математика(пр) | Н-526 | 9:30 | Пискарёв С. И. \n Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С. В. \n Иностранный язык(пр) | Н-420 | 13:10 | Мальцева С. Н. \n   ".format(message.from_user), reply_markup=markup)
    elif (message.text == "Wednesday"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Нечётная Среда".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Русский язык(пр) | Н-310 | 13:10 | Горшкова Д. И. \n Физика(л) | Н-347 | 15:25 | Карпов И. А. \n   ".format(message.from_user), reply_markup=markup)
    elif (message.text == "Thursday"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Нечётный Четверг".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Русский язык(л) | Н-514 | 11:20 | Горшкова Д. И. \n История(пр) | Н-424 | 13:10 | Скляр Л. Н. \n   ".format(message.from_user), reply_markup=markup)
    elif (message.text == "Friday"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Нечётная Пятница".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Физика(лаб) | Н-342 | 9:30 | Нескоромная А. В. \n Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С. В. \n   ".format(message.from_user), reply_markup=markup)
    elif (message.text == "All_Week"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Нечётный Понедельник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Высшая математика(л) | Н-526 | 9:30 | Пискарёв С. И. \n ВВИТ(пр) | Н-324 | 11:20 | Колесников О. В. \n ВВИТ(пр) | Н-324 | 13:10 | Колесников О. В. \n   ".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Нечётный Вторник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Высшая математика(пр) | Н-526 | 9:30 | Пискарёв С. И. \n Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С. В. \n Иностранный язык(пр) | Н-420 | 13:10 | Мальцева С. Н. \n   ".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Нечётная Среда".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Русский язык(пр) | Н-310 | 13:10 | Горшкова Д. И. \n Физика(л) | Н-347 | 15:25 | Карпов И. А. \n   ".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Нечётный Четверг".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Русский язык(л) | Н-514 | 11:20 | Горшкова Д. И. \n История(пр) | Н-424 | 13:10 | Скляр Л. Н. \n   ".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Нечётная Пятница".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Физика(лаб) | Н-342 | 9:30 | Нескоромная А. В. \n Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С. В. \n   ".format(message.from_user), reply_markup=markup)
    elif (message.text == "Help"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Ок".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, ' /Switch_Week_even - переключить неделю на чётную \n /Switch_Week переключить неделю на нечётную \n /mtuci - Сайт университета \n Далее запросы выбираются спомощью плиток, что достаточно удобно. Если у вас пропали плитки просто свичните недели. Приятного пользования, также не забывайте проверять актуальность рассписания на сайте: https://mtuci.ru/')
    elif (message.text == "Switch_Week_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b_1 = types.KeyboardButton("Monday_even")
        b_2 = types.KeyboardButton("Tuesday_even")
        b_3 = types.KeyboardButton("Wednesday_even")
        b_4 = types.KeyboardButton("Thursday_even")
        b_5 = types.KeyboardButton("Friday_even")
        b_6 = types.KeyboardButton("All_Week_even")
        b_7 = types.KeyboardButton("Switch_Week")
        b_8 = types.KeyboardButton("Help")
        markup.add(b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8)
        bot.send_message(message.chat.id, text="{0.first_name}, Вы переключили кнопки на чётную неделю.".format(message.from_user), reply_markup=markup)
    elif (message.text == "Monday_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Чётный Понедельник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Физика(л) | Н-226 | 9:30 | Карпов И. А. \n Высшая математика(л) | Н-514 | 11:20 | Пискарёв С. И. \n Иностранный язык(пр) | Н-328 | 13:10 | Мальцева С. Н. \n История(пр) | Н-401 | 15:25 | Скляр Л. Н. \n   ".format(message.from_user), reply_markup=markup)
    elif (message.text == "Tuesday_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Чётный Вторник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Высшая математика(пр) | Н-515 | 9:30 | Пискарёв С. И. \n Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С. В. \n ВВИТ(лаб) | Н-515 | 13:10 | Воронкова М. Н. \n   ".format(message.from_user), reply_markup=markup)
    elif (message.text == "Wednesday_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Чётная Среда".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Введение в профессию(л) | А-222 | 9:30 | Маликова Е. Е. \n ВВИТ(л) | А-222 | 11:20 | Машковцева Л. С. \n   ".format(message.from_user), reply_markup=markup)
    elif (message.text == "Thursday_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Чётный Четверг".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n ВВИТ(пр) | Н-515 | 9:30 | Машковцева Л. С. \n Физика(пр) | Н-515 | 11:20 | Оборотов В. А. \n Физкультура(пр) | Н-С/Зал-2 | 13:10 | Волохова С. В. \n История(л) | Н-526 | 15:25 | Скляр Л. Н. \n   ".format(message.from_user), reply_markup=markup)
    elif (message.text == "Friday_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Чётная Пятница".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Нет пар \n   ".format(message.from_user), reply_markup=markup)
    elif (message.text == "All_Week_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Чётный Понедельник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Физика(л) | Н-226 | 9:30 | Карпов И. А. \n Высшая математика(л) | Н-514 | 11:20 | Пискарёв С. И. \n Иностранный язык(пр) | Н-328 | 13:10 | Мальцева С. Н. \n История(пр) | Н-401 | 15:25 | Скляр Л. Н. \n   ".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Чётный Вторник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Высшая математика(пр) | Н-515 | 9:30 | Пискарёв С. И. \n Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С. В. \n ВВИТ(лаб) | Н-515 | 13:10 | Воронкова М. Н. \n   ".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Чётная Среда".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Введение в профессию(л) | А-222 | 9:30 | Маликова Е. Е. \n ВВИТ(л) | А-222 | 11:20 | Машковцева Л. С. \n   ".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Чётный Четверг".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n ВВИТ(пр) | Н-515 | 9:30 | Машковцева Л. С. \n Физика(пр) | Н-515 | 11:20 | Оборотов В. А. \n Физкультура(пр) | Н-С/Зал-2 | 13:10 | Волохова С. В. \n История(л) | Н-526 | 15:25 | Скляр Л. Н. \n   ".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Чётная Пятница".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Нет пар \n   ".format(message.from_user), reply_markup=markup)
bot.infinity_polling()
