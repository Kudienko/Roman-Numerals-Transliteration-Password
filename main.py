
# Задание №1
# def roman(str):
#     i = 0
#     alfavit = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#     result = 0
#     while i < len(str)-1:
#         if alfavit[str[i+1]] > alfavit[str[i]]:
#             result += alfavit[str[i+1]] - alfavit[str[i]]
#             i += 2
#         else:
#             result += alfavit[str[i]]
#             i += 1
#     if i < len(str):
#         result += alfavit[str[len(str)-1]]
#     return result
#
# str = input('Введите римское число ')
#
# print(roman(str))

# Задание №2
#
def translit(str):

    i = 0
    result = ''
    alfafit ={'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'e', 'ж': 'zh', 'ц': 'ts',
        'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l',
        'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'ъ': 'ie', 'э': 'e',
        'ю': 'iu', 'я': 'ia', 'ь': '', ' ': ' '}
    while i < len(str):
        result+= alfafit[str[i]]
        i += 1
    return result

str = input('Введите ФИО ')
print(translit(str).title())

# Задание №3
# import re
# str = input('Введите пароль ')
# reGexp = '(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])'
# if len(str) > 5 and len(str) < 13 and re.match(reGexp, str) is not None:
#     print('True')
# else:
#     print('False')

# Задание 4
# import re
# str = input('Введите цвет ')
# reGexp = 'rgb\(\s*(?:(\d{1,3})\s*,?){3}\)'
# if re.match(reGexp, str) is not None:
#     print('True')
# else:
#     print('False')

# import re
# import sys
#
# word = input()
# d = re.findall(r"\d{1,3}", word)
# for i in d:
#     if int(i) > 255:
#         print(False)
#         sys.exit()
# if re.search(r"rgb\([0-9]{1,3},[0-9]{1,3},[0-9]{1,3}\)", word) or re.search(r"rgb\([0-9]{1,3}%,[0-9]{1,3}%,[0-9]{1,3}%\)", word) \
#         or re.search(r"rgba\(([0-9]{1,3},[0-9]{1,3},[0-9]{1,3},[0-1])\)|rgba\(([0-9]{1,3},[0-9]{1,3},[0-9]{1,3},0\.\d{1,})\)", word):
#     print(True)
# else:
#     print(False)
