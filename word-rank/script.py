import sys

# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


# Good luck! You can write all the code in this file.

text = ""
for i in sentences:
    text += i
    text += " "
text = text.lower()
text = text.split()

rank_one = 0
rank_two = 0
rank_three = 0

text_one = ""
text_two = ""
text_three = ""

for i in text:
    words_num = text.count(i)

    if words_num >= rank_one and i != text_one:

        rank_three = rank_two
        rank_two = rank_one
        rank_one = words_num
        
        text_three = text_two
        text_two = text_one
        text_one = i

    elif words_num >= rank_two and i != text_two and i != text_one:

        rank_three = rank_two
        rank_two = words_num

        text_three = text_two
        text_two = i

    elif words_num >= rank_three and i != text_three and i != text_two and i != text_one:

        rank_three = words_num
        text_three = i
    
    else:
        continue

print(f'1. "{text_one}" - {rank_one}')
print(f'2. "{text_two}" - {rank_two}')
print(f'3. "{text_three}" - {rank_three}')

sys.exit()