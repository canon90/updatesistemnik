# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import errorcode
import renamed
import markdown
import lmstudio as lms
from bs4 import BeautifulSoup
import unicodedata
from datetime import date
from datetime import datetime
from datetime import datetime as dt
model = lms.llm("mlabonne/gemma-3-27b-it-abliterated-GGUF")
def md_to_html(md_text, extensions=None):
    if extensions is None:
        extensions = ['extra']
    
    return markdown.markdown(
        md_text,
        extensions=extensions,
        output_format='html'
    )

def html_to_md(html5, extensions=None):
    if extensions is None:
        extensions = ['extra']
    
    return markdown.markdown(
        html5,
        extensions=extensions,
        output_format='html'
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
        cursor = cnx.cursor(buffered=True)
        query = "SELECT *  FROM `wp_posts` WHERE  `post_title` LIKE 'Ремонт%' and `post_status` LIKE 'publish' and `post_type` LIKE 'product'  ;"  # Простой запрос для проверки подключения
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            md_text=html_to_md(row[4])
            result = model.respond("улучши текст. не надо выводить список улучшений. не надо выводить Вот улучшенный текст:"+md_text)
            result=html_to_md(result.content)
            #print(result)
            print(row[2], row[3], row[14],row[15], ) # Если у вас два столбца
            
            #post_date=dt.strptime(row[2], '%Y-%m-%d %H:%M:%S')
            today_date = datetime.now()
            #formatted_date = today_date.strftime("%Y-%m-%d %H:%M:%S")
            #if (row[2]<today_date):
            #    print(today_date.strftime("%Y-%m-%d %H:%M:%S"))
             
            # print(row['имя_столбца']) # Если вы использовали namedtuple
            # Пример использования
            post_date=today_date.strftime("%Y-%m-%d %H:%M:%S") 
            sql = f"UPDATE `sistemnik`.`wp_posts` SET `post_date` ='{post_date}' , `post_date_gmt`= '{post_date}', `post_modified`= '{post_date}', `post_modified_gmt`= '{post_date}',`post_content`='{result}' WHERE `wp_posts`.`ID` = '{row[0]}'"
            print(sql)
            cursor.execute(sql)
            cnx.commit()
        cnx.close()
        cursor.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Ошибка: Неверное имя пользователя или пароль")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Ошибка: База данных не существует")
    elif err.errno == errorcode.ER_HOST_IS_BLOCKED:
        print("Ошибка: Хост заблокирован для подключения")
    else:
        print(f"Ошибка подключения: {err}")

