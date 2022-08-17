import telebot
import re
import gc
import postgre_bot as pb
import matrix_bot as mb
import token_file as t

bot = telebot.TeleBot(t.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id,
                     f'👋 Добрый день, {message.from_user.first_name}. Вы находитесь в чат-боте Каша из топора.\n'
                     '✔ введите список продуктов, через запятую.\n'
                     '✔ в любой момент вы можете перезапустить программу, набрав команду /start.')


@bot.message_handler(func=lambda message: True)
def get_text_messages(message):
    request = message.text
    words = re.split('\W', request)
    phrase = ''
    for word in words:
        word = pb.morph.parse(word)[0].normal_form
        phrase = phrase + word + ' '
        # получим код ответа вызывая нашу функцию
    reply_id = int(mb.pipe_q.predict([phrase.strip()]))
    # отправим ответа
    bot.send_message(message.from_user.id, pb.answer[reply_id])
    print("Запрос:", request, " \n\tНормализованный: ", phrase, " \n\t\tОтвет :", pb.answer[reply_id])


gc.collect()
bot.infinity_polling(none_stop=True)

# отработка в консоле
# print("Пишите ваш вопрос, слова exit или выход для выхода: ")
# request=""
# while request not in ['exit', 'выход']:
#     request=input()
#     words= re.split('\W',request)
#     print(words)
#     phrase=""
#     for word in words:
#         print(word)
#         word = morph.parse(word)[0].normal_form
#         phrase = phrase + word + " "
#         print(phrase)
#     reply_id = int(pipe_q.predict([phrase.strip()]))
#     print(reply_id)
#     print(answer[reply_id])
