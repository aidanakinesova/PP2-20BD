# Re.start() & Re.end() ;)
import re

s = input()
k = input()
x = re.finditer(r'(?=('+k+'))', s)
if x:
    for i in x:
        print(i.start(1), i.end(1) - 1)
else:
    print(-1, -1)

# text = "походный налог, доход"
# match = re.findall(r'\b(?:прибыль|обретение|доход)\b', text)
# print(match)
