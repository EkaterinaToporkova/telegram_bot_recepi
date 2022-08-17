import psycopg2
import pymorphy2

# подключаемся к PostgreSQL
conn = psycopg2.connect(dbname='telegram_data', user='postgres', password='katyatopor', host='127.0.0.1')
cursor = conn.cursor()

# настраиваем языка для библиотеки морфологии
morph = pymorphy2.MorphAnalyzer(lang='ru')

# объявляем массив ответов
link_c_id = []
answer = dict()

# получаем из PostgreSQL словарь ответов и проиндексируем их
cursor.execute('SELECT id, link_c from link_table;')
records = cursor.fetchall()
for row in records:
    answer[row[0]] = row[1]

# объявляем массив вопросов
questions = []

# загрузим вопросы и коды ответов
cursor.execute('SELECT ingr, link_c_id FROM ingredients;')
records = cursor.fetchall()

# посчитаем количество вопросов
transform = 0

for row in records:
    # если текст вопроса не пустой
    if row[0] > '':
        # и если нашелся хоть один ответ
        if row[1] > 0:
            phrases = row[0]

            # разбиваем вопрос на слова
            words = phrases.split(', ')
            phrase = ''
            for word in words:
                # каждое слово из вопроса приводим в нормальную словоформу
                word = morph.parse(word)[0].normal_form

                # составляем фразу из нормализированных слов
                phrase = phrase + word + ' '

            # если длина полученной фразы больше 0, добавляем ее в массив вопросов и массив кодов ответов
            if len(phrase) > 0:
                questions.append(phrase.strip())
                link_c_id.append(row[1])
                transform += 1

# print(questions)
# print(answer)
# print(link_c_id)

# закроем подключение к PostgreSQL
cursor.close()
conn.close()
