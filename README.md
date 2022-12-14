## Телеграм-бот "Каша из топора"
Бот предназначен для поиска рецептов по названию блюда или ингредиентам.
Для поиска рецепта по ингредиентам нужно перечислить через запятую продукты, которые есть дома.

:computer: Файл **telegram_bot.py** - отвечает за логику бота.

:computer: Файл **postgre_bot.py** - отвечает за работу с базой данных.

:computer: Файл **matrix_bot.py** - отвечает за создание матрица данных и за поиск по этой матрице.

В ходе работы использовались:

:scroll: библиотека psycopg2

:scroll: библиотека pymorphy2

:scroll: библиотека scikit-learn

:scroll: библиотека NumPy

:scroll: СУБД PostgreSQL


Когда пользователь открывает чат-бот, он видит сообщение с информацией, чем именно занимается бот.

![](https://github.com/EkaterinaToporkova/telegram_bot_recepi/blob/master/%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C.jpg)

После нажатия на кнопку **Запустить**, бот присылает приветственное сообщение с инструкцией, что необходимо сделать, чтобы получить рецепт.

![](https://github.com/EkaterinaToporkova/telegram_bot_recepi/blob/master/%D1%81%D1%82%D0%B0%D1%80%D1%82.jpg)

Когда пользователь вводит ингредиенты, в ответ бот присылает ссылку на рецепт (в ссылке несколько вариаций рецептов одного блюда).

![](https://github.com/EkaterinaToporkova/telegram_bot_recepi/blob/master/%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82.jpg).

База данных состоит из двух таблиц.

Одна таблица с ингредиентами и порядковым номером соответствущей ссылки на рецепт.
![](https://github.com/EkaterinaToporkova/telegram_bot_recepi/blob/master/ingredients.jpg)

Другая таблица состоит из ссылок.

![](https://github.com/EkaterinaToporkova/telegram_bot_recepi/blob/master/link_table.jpg).

С помощью машинного обучения все ингредиенты трансформируем в матрицу. С помощью этой матрицы будем получать код ссылки, а затем и саму ссылку.
