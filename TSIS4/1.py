import re

# f = open('./data.txt', 'r')
# data = f.read()
f = open('data.txt', 'r', encoding='utf-8')
data = f.readlines()


name = re.search(r'Филиал\sТОО\s\w+\s\w+', data)
bin = re.search(r'\d{12}', data)
items = re.findall(r'\d+\.\n(.*)', data)
cnt = re.findall(r'(\d),\d{3}', data)
price = re.findall(r'x\s([\d\s]+,\d+)', data)
total = re.findall(r'Стоимость\n([\d\s]+,\d+)', data)
address = re.search(r'г\.\s[\w\-]+\,\w+\,\s[\w+\s]+\,\d+\,\s\w\-\d', data)
date = re.search(r'\d{2}\.\d{2}\.\d{4}\s\d{2}\:\d{2}\:\d{2}', data)


print("1. Name of the company: " + name.group())
print("2. BIN number: " + bin.group())

for i in range(len(items)):
    # print(len(items))
    print("1. Title: " + items[i]) 
    print("2. Count: " + cnt[i])
    print("3. Unit price: " + price[i])
    print("4. Total price: " + total[i])

print("4. Date: " + date.group())
print("5. Address: " + address.group())