import telebot  # импортируем модуль pyTelegramBotAPI
import conf     # импортируем наш секретный токен
import markov_model
from telebot import types
bot = telebot.TeleBot(conf.TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Овен")
    btn2 = types.KeyboardButton("Телец")
    btn3 = types.KeyboardButton("Близнецы")
    btn4 = types.KeyboardButton("Рак")
    btn5 = types.KeyboardButton("Лев")
    btn6 = types.KeyboardButton("Дева")
    btn7 = types.KeyboardButton("Весы")
    btn8 = types.KeyboardButton("Скорпион")
    btn9 = types.KeyboardButton("Стрелец")
    btn10 = types.KeyboardButton("Козерог")
    btn11 = types.KeyboardButton("Водолей")
    btn12 = types.KeyboardButton("Рыбы")
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12)
    bot.send_message(message.chat.id,
                     text="Я приветствую всех, желающих узнать свою судьбу. Каков твой знак гороскопа?", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Овен"):
        bot.send_message(message.chat.id, text="Привет.. Если честно, Овен мой любимый знак зодиака, Овны так стремятся к победе. Вот мое предсказание для тебя:")
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
    elif (message.text == "Телец"):
        bot.send_message(message.chat.id,
                             text="Привет.. Если честно, Телец мой любимый знак зодиака, Тельцы такие волевые. Вот мое предсказание для тебя:")
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
    elif (message.text == "Близнецы"):
        bot.send_message(message.chat.id,
                             text="Привет.. Если честно, Близнецы мой любимый знак зодиака, Близнецы так любят узнавать что-то новое. Вот мое предсказание для тебя:")
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
    elif (message.text == "Рак"):
        bot.send_message(message.chat.id,
                             text="Привет.. Если честно, Рак мой любимый знак зодиака, Раки так стремятся защитить своих близких. Вот мое предсказание для тебя:")
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
    elif (message.text == "Лев"):
        bot.send_message(message.chat.id,
                             text="Привет.. Если честно, Лев мой любимый знак зодиака, Львы такие верные. Вот мое предсказание для тебя:")
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
    elif (message.text == "Дева"):
        bot.send_message(message.chat.id,
                             text="Привет.. Если честно, Дева мой любимый знак зодиака, Девы действительно умеют ценить красоту. Вот мое предсказание для тебя:")
        bbot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
    elif (message.text == "Весы"):
        bot.send_message(message.chat.id,
                             text="Привет.. Если честно, Весы мой любимый знак зодиака, Весы такие дружелюбные. Вот мое предсказание для тебя:")
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
    elif (message.text == "Скорпион"):
        bot.send_message(message.chat.id,
                             text="Привет.. Если честно, Скорпион мой любимый знак зодиака, у Скорпионов такая мощная интуиция. Вот мое предсказание для тебя:")
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
    elif (message.text == "Стрелец"):
        bot.send_message(message.chat.id,
                             text="Привет.. Если честно, Стрелец мой любимый знак зодиака, Стрельцы такие красноречивые. Вот мое предсказание для тебя:")
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
    elif (message.text == "Козерог"):
        bot.send_message(message.chat.id,
                             text="Привет.. Если честно, Козерог мой любимый знак зодиака, Козероги совсем не боятся сложностей. Вот мое предсказание для тебя:")
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
    elif (message.text == "Водолей"):
        bot.send_message(message.chat.id,
                             text="Привет.. Если честно, Водолей мой любимый знак зодиака, Водолеи так нестандартно мыслят. Вот мое предсказание для тебя:")
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
    elif (message.text == "Рыбы"):
        bot.send_message(message.chat.id,
                             text="Привет.. Если честно, Рыбы мой любимый знак зодиака, Рыбы так хорошо шутят. Вот мое предсказание для тебя:")
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
        bot.send_message(message.chat.id, markov_model.model.make_short_sentence(400))
if __name__ == '__main__':
    bot.polling(none_stop=True)