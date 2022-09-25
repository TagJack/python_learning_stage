import re
## Материал на сайте https://habr.com/ru/post/349860/


# ## Еще немного регулярки.
# line = 'asdf gto wfo fjdk;afed,fjek,asdf,foo'
# result = re.findall(r'\b\w{3}\b', line)
# print(result)


# line = 'Москва: 777, 999, 797. Тула: 071, 950, 112'
# m = re.findall("\d+", line, re.IGNORECASE)
# print(m)
#
# line2 = "Летучий голландец."
# m = re.findall('летучий', line2, re.IGNORECASE)
# print(m)


# line = "Привидение прошуршало и исчезло в углу."
# m = re.findall(r'\w+ло', line, re.IGNORECASE)
# print(m)

# string = "В современном мире информатика и информационные системы " \
#          "будут игрыть решающую роль. Поэтому, информатика важная наука."
# result = re.findall(r'\bинф\w+', string, re.MULTILINE)
# print(result)


# result = re.findall(r"\b\w.", 'AV is largest Analytics community of India')
# print(result)


# line = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'
# result = re.findall(r'\w+.\w+@\w+.\w+', line) ### Извлечение домена.
# print(result)
# result = re.findall(r'@\w+.(\w+)', line) # Извлечение домена верхнего уровня.
# print(result)
#
#
# Вывод даты из строки
# line = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
# result = re.findall(r'\d{2}-\d{2}-\d{4}|\d+\D\d+', line) # чтобы извлечь только года помогут скобки.
# print(result)
#
# # Извлечение слов начинающихся на глусную или на согласную.
# • [..] Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
# line = 'AV is largest Analytics community of India'
# result = re.findall(r'\b[^ auiouAUIOU]\w+', line) # чтобы инверсировать поиск гласных на поиск согласных
# print(result) # можно использовать знак ^


# Проверка формата телефонного номера.
# li = ['9999999999', '999999-999', '99999x9999']

# for val in li:
#     if re.match(r"[8-9]{1}[0-9]{9}", val) and len(val) == 10:
#         print('Yes')
#     else:
#         print('No')


# Разбиваем строку по нескольким разделителям
# line = 'asdf fjdk;afed,fjek,asdf,foo'
# result = re.split(r'[,;\s]', line)
# print(result)

## метод re.sub() для замены всех разделителей пробелами
# line = 'asdf fjdk;afed,fjek,asdf,foo'
# result = re.sub(r'[;,\s]', ' ', line)
# print(result)




# string = """Вот текст, с номерами (вида 111-11- * 11, или ва232-34-34фы, или 555-77-77.
# Вообще, с) (учетом вида регулярки, номера могут содержать 5-7 и больше цифр
# и все равно распознаваться и приводиться к красивому) виду, смотри 7-77-77 или 5-22-22.
# Почувствуйте мощь регулярок! БАЗАР, дождСИЛЬНЫЙмокрый.
# Предложение где в * cлове еc5ть англ буквы, иногда и цифры. Cлово. Строчка * где есть знак"""

# # Найдите все натуральные числа (возможно, окружённые буквами).
# m = re.findall(r'\d{0,3}-\d{2}-\d{2}|\d{1,2}-\d{1,2}|\s\d+?\s', string, re.MULTILINE) # только цифры.
## Вариант 2.
# res = re.sub(r'\D', '', string)
# print(re.sub(r'(?<=\d)(?=\d)', ' ', res))


# # Найдите все «слова», написанные капсом (то есть строго заглавными), возможно внутри настоящих слов (аааБББввв);
# #. в фиг. скобках поручение сколько должно быть букв в слове.
# m = re.findall(r'[А-Я]{2,}', string, re.MULTILINE)


# # Найдите слова, в которых есть англ буква, а когда-нибудь за ней цифра;
# m = re.findall(r'\w+[a-zA-Z]\d+\w+|\b[a-zA-Z]\w+', string, re.MULTILINE)
# print(re.findall(r'(?:\w+)?[a-zA-Z]+\w+', string))

# # Найдите все слова, начинающиеся с англ буквы (\b — граница слова);
# m = re.findall(r'\b[a-z]\w+', string, re.IGNORECASE)



# # Найдите все натуральные числа, не находящиеся внутри или на границе слова;
# m = re.findall(r'\W+(\d+)\W+', string, re.MULTILINE)


# # Найдите строчки, в которых есть символ * (. — это точно не конец строки!);
# m = re.findall(r'\w*[\s\S]\*[\s\S]\w*', string, re.MULTILINE)


# # Найдите строчки, в которых есть открaывающая и когда-нибудь потом закрывающая скобки;
# # Если есть перенос то регулярка не работает с переносом, придется указать [\s\S]*
# m = re.findall(r'\([\s\S]*\)', string, re.IGNORECASE)


# print(m)
# # #Задача 01. Регистрационные знаки транспортных средств
# import re
#
# lst = ['С227НА777', 'КУ22777', 'Т22В7477', 'М227К19У9', ' С227НА777']
# for n in lst:
#     if re.findall(r'^[АВЕКМНОРСТУХ][0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}$', n):
#         print('Private.')
#     elif re.findall(r'^[АВЕКМНОРСТУХ]{2}[0-9]{5,6}$', n):
#         print('Taxi.')
#     else:
#         print('Fail.')


## ##Задача 02. Количество слов
# string = """Он --- серо-буро-малиновая редиска!!
# >>>:->
# А не кот.
# www.kot.ru"""
# m = re.findall(r'\w+[.]\w+[.]\w+|\b\w+\b', string)
# print(len(m))


##Задача 04. Замена времени
string = '''Уважаемые! Если вы к 09:00 не вернёте
чемодан, то уже в 09:00:01 я за себя не отвечаю.
PS. С отношением 25:50 всё нормально!'''


# m = re.sub(r'(?:[0-1][0-9]|2[0-5])[:][0-5][0-9](?:[:][0-5][0-9])?', 'TBD', string)
# print(m)


### пример шаблона для вычисления MAC - адресов.
# r'[0-9a-fA-F]{2}(?:[:-][0-9a-fA-F]{2}){4}



####Задача 06. Аббревиатуры
# string = 'Это курс информатики соответствует ФГОС и ПООП, это подтверждено ФГУ ФНЦ НИИСИ РАН'
# m = re.findall(r'(?:[А-Я]{2,})(?:[\s][А-Я]{2,})*', string)
# print(m)


### Пример с группировков и функцией re.search(pattern, string)
# string = r'---   Опять45   ---'
# match= re.search(r'\s*([А-Яа-яЁё]+)(\d+)\s*', string)
# print(f'Найдена подстрока >{match[0]}< с позиции {match.start(0)} до {match.end(0)}')
# print(f'Группа букв >{match[1]}< с позиции {match.start(1)} до {match.end(1)}')
# print(f'Группа цифр >{match[2]}< с позиции {match.start(2)} до {match.end(2)}')


### Внутри группирующих скобок могут быть и другие группирующие скобки.
### В этом случае их нумерация производится в соответствии с номером появления открывающей скобки с шаблоне.
# pattern = r'((\d)(\d))((\d)(\d))'
# string = r'123456789'
# match = re.search(pattern, string)
# print(f'Найдена подстрока >{match[0]}< с позиции {match.start(0)} до {match.end(0)}')
# for i in range(1, 7):
#     print(f'Группа №{i} >{match[i]}< с позиции {match.start(i)} до {match.end(i)}')
# ###
# ## -> Найдена подстрока >1234< с позиции 0 до 4


#### Использование групп при заменах.
# import re
# text = "We arrive on 03/25/2018. So you are welcome after 04/01/2018."
# print(re.sub(r'(\d\d)/(\d\d)/(\d{4})', r'\2.\1.\3', text))
## -> We arrive on 25.03.2018. So you are welcome after 01.04.2018.


### Задача 07. Шифровка
# import re
# def repl(m):
#     return str(int(m[0]) ** 3)
# Действия совершаются не с >m< а с его содержимым >m[0]<
# На выходе функции должен быть тип данных str()
# # text = 'Было закуплено 12 единиц техники по 410.37 рублей.'
# # print(re.sub(r'\d+', repl, text))


# ####Задача 08. То ли акростих, то ли акроним, то ли апроним
# import re
# string = 'Московский государственный институт международных отношений'
# string2 = 'микоян авиацию снабдил алкоголем, народ доволен работой авиаконструктора'
# line = re.findall(r'(\b\w)', string2)
# print(''.join(line).upper())


###Задача 09. Хайку
# import re
# lst = ['on codeforces', 'beta round is running', 'a rustling of keys']
# res = [len(re.findall(r'[aieou]', item)) for item in lst]
# print(["NO", "YES"][res == [5,7,5]])


####Задача 10. CamelCase -> under_score
# string = 'MyVar17 = OtherVar + YetAnother2Var TheAnswerToLifeTheUniverseAndEverything = 42'
# print(re.sub(r'(?<!\b)(?=[A-Z])','_', string).lower())

# ## Задача 11. Удаление повторов
# line = 'Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод.'
# эта регулярка значит слово, пробел сколько есть, и такое же слово, столько сколько есть."""
# r'\1' - заменяет найденное со
# впадение единичным экземпляром найденного слова (значение подмаски №1)
# print(re.sub(r'\b(\w+)(\s+\1)+\b', r'\1', line))


## Задача 12. Близкие слова
# line = 'Да он олень, а не заяц!'
# print(re.findall(r'(?<=он).+(?=\W)', line))


### Задача 13. Форматирование больших чисел
# def f(m):
#     return str('{:,}'.format(int(m[0])))
#
# line = '''12 мало
# лучше 123
# 1234 почти
# 12354 хорошо
# стало 123456
# супер 1334567'''
#
# print(re.sub(r'\d+', f, line))




### Разделение текста на предложения с файла.
# import re
#
# with open("блаблабла.txt", "r") as f:
#     s = re.sub(r'\s+', ' ', f.read().decode('WINDOWS-1251'), flags=re.M)
# for s in re.split(r'(?<=[.!?…]) ', s):
#     print(s)

# ####Задача 14. Разделить текст на предложения.
# line = '''В        этом
# предложении разрывы строки... Но это
# не так важно! Совсем? Да, совсем! И это
#
# не    должно мешать.'''

# line = re.sub(r'(\s)(\s+)', r'\1', line)
# for i in re.split(r'(?<=[.?!:…])', line):
#     print(i)


####Задача 15. Форматирование номера телефона
# import re
#
# lst = ["+7 123 456-78-90", "8(123)456-78-90", "7(123) 456-78-90", "1234567890", "123456789", "+9 123 456-78-90",
#        "+7 123 456+78=90", "+7(123 45678-90", "8(123  456-78-90"]
#
# with open('list_of_numbers.txt', 'w') as f:
#     f.writelines(i+'\n' for i in lst)

# with open('list_of_numbers.txt', 'r') as f:
#     lst_nums = [i.strip() for i in f.readlines()]
#
# for item in lst_nums:
#     if re.fullmatch(r'\+?[7-8]?[\(\s]?\d{3}\)?\s?\d{3}[-\s]?\d{2}[\-]?\d{2}', item):
#         item = item.replace('(', '').replace(')', '').replace(' ', '').replace('+', '').replace('-', '')
#         if len(item) < 11: item = '7' + item
#         if item[0] != '7': item = item[0].replace(item[0], '7') + item[1:]
#
#         print(f'+{item[0]} {item[0:4]} {item[4:7]} {item[7:9]} {item[9:]}')
#
#     else: print('Fail.')


# ####Задача 16. Поиск e-mail'ов — 2
# examp = """Иван Иванович!
# Нужен ответ на письмо от ivanoff@ivan-chai.ru.
# Не забудьте поставить в копию
# serge'o-lupin@mail.ru- это важно."""
#
# examp2 = """NO: foo.@ya.ru, foo@.ya.ru, foo@foo@foo
# NO: +foo1@ya.ru, foo2@ya-ru
# NO: foo@ya_ru, -foo3@ya.ru-, foo4@ya.ru+
# NO: foo..foo7@ya.ru
# YES: (boo1@ya.ru), boo2@ya.ru!, boo3@ya.ru"""
#
# # print(re.findall(r'(?<![\+-.])\w+?\d?[\'._+-]?\w+?\d?[\'._+-]?[a-z]+\d?@\w+[\'_+-]?\w+?\.\w{2,3}(?![\+])', examp))
# print(re.findall(r'\b(?<![+.\-])\w+(?:\'.\-\w+)?@\w+(?:[-.]\w+)?\.\w+(?![+])\b', examp2))
## В (?:) тоже работает как [] (либо, либо).


str = '<div class="card__price">                Фарап                <span class="card__price-number">20000 TMT</span></div>'
city = re.findall(r'(?<=>).+(?=<)', str)
print(city)