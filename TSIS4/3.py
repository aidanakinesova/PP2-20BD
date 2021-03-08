import re

with open('raw.txt', 'r', encoding='utf-8') as f:
    all_lines = ''.join(f.readlines())

company_name = re.search(r'ДУБЛИКАТ\n(.+)', all_lines).group(1)
# print(company_name.group(0)) # 0 вытаскивает все совпадение, а 1 первую группу
# bin_number = re.search(r'БИН\s(\d+)\n', all_lines).group(1)
bin_number = re.search(r'БИН (\d+)', all_lines).group(1)
# items = re.findall(r'\d+\.\n([^\n]+)\n([0-9]+\,|\s[0-9]+ x ([0-9]+\,|\s[0-9]+)\n([0-9]+\,|\s[0-9]+)', all_lines)
# items = re.findall(r'\d+\.\n([^\n]+)\n([0-9, ]+) x ([0-9, ]+)\n([0-9, ]+)', all_lines)
items = re.findall(r'\d+\.\n([^\n]+)\n([0-9, ]+) x ([0-9, ]+)\n([0-9, ]+)', all_lines)
                   # num. nl  name  nl quantity x  quant. nl  sum     
total = re.findall(r'Стоимость\n([0-9, ]+)', all_lines)
date = re.search(r'Время: \d{2}\.\d{2}\.\d{4}\s\d+\:\d+\:\d+', all_lines).group(0)
# address = re.search(r'г\.\s[\w\-]+\,\w+\,\s\[\w ]+\,\d+\,\s\[\w\-\d]+\n)', all_lines).group(0)
address = re.search(r'г\.[^\n]+', all_lines).group(0)
overall_cost = re.search(r'ИТОГО:\n([^\n]+)', all_lines).group(1)
print(f'Company name: {company_name}')
print(f'BIN: {bin_number}')
print(f'Date: {date}')
print(f'Address: {address}')

def prettify(s):
    s = s.replace(' ', '')
    s = s.replace(',', '.')
    return float(s)

check_sum = 0
for index, item in enumerate(items): # одновременно элемент и номер возвращает
    print(f'{index + 1}) Product name: {item[0]}')
    print(f'\t{item[1]} * {item[2]} = {item[3]}')
    check_sum += prettify(item[3])

print(f'Overall sum from check: {overall_cost}')
print(f'Our sum: {check_sum}')

import csv
# comma separated value

csv.excel.delimiter = ';'
csv.excel.lineterminator = '\n'
writer = csv.writer(open('1.csv', 'w', encoding='cp1251'), csv.excel)

writer.writerow([company_name])                                 
writer.writerow([f'BIN: {bin_number}'])
writer.writerow([f'Date: {date}', f'Address: {address}'])
writer.writerows(items)
# OMG what is it

# output:
# Company name: Филиал ТОО EUROPHARMA Астана
# BIN: 080841000761
# Date: Время: 18.04.2019 11:13:58
# Address: г. Нур-султан,Казахстан, Мангилик Ел,19, нп-5
# Product name: Натрия хлорид 0,9%, 200 мл, фл
#         2,000 * 154,00 = 308,00
# Product name: Борный спирт 3%, 20 мл, фл.
#         1,000 * 51,00 = 51,00
# Product name: Шприц 2 мл, 3-х комп. (Bioject)
#         2,000 * 16,00 = 32,00
# Product name: Система для инфузии Vogt Medical
#         2,000 * 60,00 = 120,00
# Product name: Naturella прокладки Классик макси №8
#         1,000 * 310,00 = 310,00
# Product name: AURA Ватные диски №150
#         1,000 * 461,00 = 461,00
# Product name: Чистая линия скраб мягкий 50 мл
#         1,000 * 381,00 = 381,00
# Product name: Чистая линия  скраб очищающийабрикос 50 мл
#         1,000 * 386,00 = 386,00
# Product name: Чистая линия скраб мягкий 50 мл
#         1,000 * 381,00 = 381,00
# Product name: Carefree салфетки Алоэвоздухопроницаемые №20
#         1,000 * 414,00 = 414,00
# Product name: Pro Series Шампунь яркий цвет 500мл
#         1,000 * 841,00 = 841,00
# Product name: Pro Series бальзам-ополаскивательдля длител ухода за окрашеннымиволосами Яркий цвет 500мл
#         1,000 * 841,00 = 841,00
# Product name: Clear шампунь Актив спорт 2в1мужской  400 мл
#         1,000 * 1 200,00 = 1 200,00
# Product name: Bio World (HYDRO THERAPY)Мицеллярная вода 5в1, 445мл
#         1,000 * 1 152,00 = 1 152,00
# Product name: Bio World (HYDRO THERAPY) Гель-муссдля умывания с гиалуроновойкислотой, 250мл
#         1,000 * 1 152,00 = 1 152,00
# Product name: [RX]-Натрия хлорид 0,9%, 100 мл, фл.
#         1,000 * 168,00 = 168,00
# Product name: [RX]-Дисоль р-р 400 мл, фл.
#         1,000 * 163,00 = 163,00
# Product name: Тагансорбент с иономи серебра №30,пор.
#         1,000 * 1 526,00 = 1 526,00
# Product name: [RX]-Церукал 2%, 2 мл, №10, амп.
#         2,000 * 396,00 = 792,00
# Product name: [RX]-Андазол 200 мг, №40, табл.
#         1,000 * 7 330,00 = 7 330,00

# output после enumerate и пробел:
# Company name: Филиал ТОО EUROPHARMA Астана
# BIN: 080841000761
# Date: Время: 18.04.2019 11:13:58
# Address: г. Нур-султан,Казахстан, Мангилик Ел,19, нп-5

# 1) Product name: Натрия хлорид 0,9%, 200 мл, фл
#         2,000 * 154,00 = 308,00
# 2) Product name: Борный спирт 3%, 20 мл, фл.
#         1,000 * 51,00 = 51,00
# 3) Product name: Шприц 2 мл, 3-х комп. (Bioject)
#         2,000 * 16,00 = 32,00
# 4) Product name: Система для инфузии Vogt Medical
#         2,000 * 60,00 = 120,00
# 5) Product name: Naturella прокладки Классик макси №8
#         1,000 * 310,00 = 310,00
# 6) Product name: AURA Ватные диски №150
#         1,000 * 461,00 = 461,00
# 7) Product name: Чистая линия скраб мягкий 50 мл
#         1,000 * 381,00 = 381,00
# 8) Product name: Чистая линия  скраб очищающийабрикос 50 мл
#         1,000 * 386,00 = 386,00
# 9) Product name: Чистая линия скраб мягкий 50 мл
#         1,000 * 381,00 = 381,00
# 10) Product name: Carefree салфетки Алоэвоздухопроницаемые №20
#         1,000 * 414,00 = 414,00
# 11) Product name: Pro Series Шампунь яркий цвет 500мл
#         1,000 * 841,00 = 841,00
# 12) Product name: Pro Series бальзам-ополаскивательдля длител ухода за окрашенными волосами Яркий цвет 500мл
#         1,000 * 841,00 = 841,00
# 13) Product name: Clear шампунь Актив спорт 2в1мужской  400 мл
#         1,000 * 1 200,00 = 1 200,00
# 14) Product name: Bio World (HYDRO THERAPY)Мицеллярная вода 5в1, 445мл
#         1,000 * 1 152,00 = 1 152,00
# 15) Product name: Bio World (HYDRO THERAPY) Гель-муссдля умывания с гиалуроновой кислотой, 250мл
#         1,000 * 1 152,00 = 1 152,00
# 16) Product name: [RX]-Натрия хлорид 0,9%, 100 мл, фл.
#         1,000 * 168,00 = 168,00
# 17) Product name: [RX]-Дисоль р-р 400 мл, фл.
#         1,000 * 163,00 = 163,00
# 18) Product name: Тагансорбент с иономи серебра №30,пор.
#         1,000 * 1 526,00 = 1 526,00
# 19) Product name: [RX]-Церукал 2%, 2 мл, №10, амп.
#         2,000 * 396,00 = 792,00
# 20) Product name: [RX]-Андазол 200 мг, №40, табл.
#         1,000 * 7 330,00 = 7 330,00