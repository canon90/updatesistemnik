# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import errorcode
import renamed
import markdown
import lmstudio as lms
from bs4 import BeautifulSoup
import unicodedata
model = lms.llm("mlabonne/gemma-3-27b-it-abliterated-GGUF")
def md_to_html(md_text, extensions=None):
    if extensions is None:
        extensions = ['extra']
    
    return markdown.markdown(
        md_text,
        extensions=extensions,
        output_format='html5'
    )




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
        query = "SELECT *  FROM `wp_posts` WHERE `ID` = 365 AND `post_title` LIKE '%Ремонт%';"  # Простой запрос для проверки подключения
        cursor.execute(query)
        for row in cursor:
            #cleantext = unicodedata.normalize("NFC", row[4])
            #s2 = re.sub(r"<.*?>", "", row[4])# Выводит каждую строку в виде кортежа
            #s2=re.sub(r"^\xb2", "", row[4])
            #print(re.sub(r"^\xb2", "", row[4]))
            result = model.respond("улучши текст. не надо выводить список улучшений"+row[4])
            html_text = md_to_html(result)
            print(html_text)
            
            print(result)
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

