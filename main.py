# -*- coding: cp1251 -*-  # Или # -*- coding: windows-1251 -*-
import mysql.connector
from mysql.connector import errorcode
import renamed
import lmstudio as lms

with lms.Client() as client:
    model = client.llm.model("qwen/qwen3-4b-2507")
    result = model.respond("What is the meaning of life?")

    print(result)

from renamed import *
try:
    with mysql.connector.connect(
        user='sistemnik',
        password='0Q8VjOiB[ujG29Nz',
        host='192.168.1.58',
        database='sistemnik',
        port='3306'
    ) as cnx:
        print('Подключение к базе данных успешно установлено!')

        # Работа с базой данных (например, создание курсора и выполнение запроса)
        cursor = cnx.cursor()
        query = "SELECT * FROM `wp_posts` WHERE `post_status` LIKE 'publish' and `post_content` LIKE '%Ремонт%';"  # Простой запрос для проверки подключения
        cursor.execute(query)
        for row in cursor:
            print(row[5]+'|||'+row[11]+'||||'+ transliterate(row[5]))  # Выводит каждую строку в виде кортежа
            # Или можно получить значения по индексу или имени столбца:
            # print(row[0], row[1]) # Если у вас два столбца
            # print(row['имя_столбца']) # Если вы использовали namedtuple
            # Пример использования
            #sql = f"UPDATE `sistemnik`.`wp_posts` SET `post_name` ='{transliterate(row[5])}' WHERE `wp_posts`.`ID` = '{row[0]}'"
            #print(sql)
            #val = (transliterate(row[5]),row[0])
            #cursor.execute(sql, val)
            #cursor.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Ошибка: Неверное имя пользователя или пароль")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Ошибка: База данных не существует")
    elif err.errno == errorcode.ER_HOST_IS_BLOCKED:
        print("Ошибка: Хост заблокирован для подключения")
    else:
        print(f"Ошибка подключения: {err}")

