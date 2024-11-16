import telebot
import info
from telebot import types

token = '6764129980:AAG5MOeBgF5G8GQ3cdjBhuGHNVng7r8ycug'
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Хобби персонажа")
    btn2 = types.KeyboardButton("Про персонажа")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Привет! Меня зовут шрек, и этот бот расскажет все обо мне по твоим запросам.\n"
                                      "Ты можешь узнать о функциях этого бота по команде /help.\n", reply_markup=markup)


@bot.message_handler(commands=['help'])
def say_help(message):
    bot.send_message(message.chat.id, "Вот все те команды, которыми обладает этот бот:\n"
                                      "/start - приветствует пользователя, вкраце рассказывает о себе.\n"
                                      "/help - предоставляет все возможности бота.\n"
                                      "/about - основные сведения о персонаже.\n"
                                      "/family - информация про семейную жизнь персонажа.\n"
                                      "/hobby - любимые занятия персонажа, его рутина.\n"
                                      "/friends - лучший друг персонажа.\n"
                                      "/foods - предпочтения персонажа в еде.\n"
                                      "/fav_photo - личный фотосет персонажа.\n")


@bot.message_handler(commands=['about'])
def say_about(message):
    bot.send_message(message.chat.id, info.about_me())


@bot.message_handler(commands=['family'])
def say_family(message):
    bot.send_message(message.chat.id, info.family_me())
    bot.send_message(message.chat.id, "<b>Вот моя  семья</b>", parse_mode='html')
    photo = open('shrek.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['hobby'])
def say_hobby(message):
    bot.send_message(message.chat.id, info.hobby_me())


@bot.message_handler(commands=['friends'])
def say_friends(message):
    bot.send_message(message.chat.id, info.friends_me())
    bot.send_message(message.chat.id, "<b>Ну и конечно же наша совместная фотка⬇️⬇️⬇️</b>", parse_mode='html')
    photo = open('shrek3.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['foods'])
def say_hobby(message):
    bot.send_message(message.chat.id, info.foods_me())


@bot.message_handler(commands=['fav_photo'])
def say_photo(message):
    bot.send_message(message.chat.id, "<b>Моя зубатка</b>", parse_mode='html')
    photo = open('shrek4.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "<em>напиши дальше, если хочешь продолжить</em>", parse_mode='html')


def filter_password(message1):
    password = "дальше"
    return password in message1.text.lower()


@bot.message_handler(content_types=['text'], func=filter_password)
def say_go(message):
    bot.send_message(message.chat.id, "<b>Это я злой👹👹👹.</b>", parse_mode='html')
    photo1 = open('shrek5.png', 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_message(message.chat.id, "<em>напиши еще, если хочешь продолжить</em>", parse_mode='html')


def filter_password2(message):
    password = "еще"
    return password in message.text.lower()


@bot.message_handler(content_types=['text'], func=filter_password2)
def say_go2(message):
    bot.send_message(message.chat.id, "<b>Это я удивлен😮😮😮.</b>", parse_mode='html')
    photo2 = open('shrek6.png', 'rb')
    bot.send_photo(message.chat.id, photo2)
    bot.send_message(message.chat.id, "<em>ну вот и всё</em>", parse_mode='html')


@bot.message_handler(content_types=['photo', 'audio'])
def say_not(message):
    bot.send_message(message.chat.id, 'Эту команду я не знаю\n'
                                      'Список команд /help')


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Хобби персонажа":
        bot.send_message(message.chat.id, info.hobby_me())
    elif message.text == "Про персонажа":
        bot.send_message(message.chat.id, info.about_me())


bot.polling()
