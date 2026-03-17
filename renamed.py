# -*- coding: cp1251 -*-  # Или # -*- coding: windows-1251 -*-
import re
def transliterate(text):
    # Словарь для замены русских букв на английские
    mapping = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e','ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm','н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u','ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch','ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    result = []
    for char in text.lower():  # Приводим все символы к нижнему регистру
        if char in mapping:
            result.append(mapping[char])  # Заменяем русские буквы
        elif char.isalpha() or char.isdigit():
            result.append(char)  # Оставляем английские буквы и цифры
        else:
            result.append('-')  # Заменяем специальные символы на дефис
    
    # Объединяем результат в строку и заменяем multiple дефисы на один
    transliterated = ''.join(result)
    transliterated = re.sub(r'-+', '-', transliterated)  # Заменяем multiple дефисы на один
    
    # Удаляем дефисы в начале и конце строки
    return transliterated.strip('-')

