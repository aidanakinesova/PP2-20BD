import re
 
# text = "подоходный налог"
# match = re.findall(r"прибыль|обретение|доход", text)
# print(match)
# output:
# ['доход']

# text = "подоходный налог"
# match = re.findall(r"прибыль|обретение|\bдоход\b", text)
# print(match)
# output:
# []

# text = "подоходный налог, доход"
# match = re.findall(r"прибыль|обретение|\bдоход\b", text)
# print(match)
# output:
# ['доход']

# text = "подоходный налог"
# match = re.findall(r"\b(?:прибыль|обретение|доход)\b", text) # match = re.findall(r"\bприбыль\b|\bобретение\b|\bдоход\b", text)
# print(match)


# import re
# S = input()
# k = input()
# anymatch = 'No'
# for m in re.finditer(r'(?=('+k+'))',S):
#     anymatch = 'Yes'
#     print (m.start(1),m.end(1)-1)
# if anymatch == 'No':
#     print (-1, -1)

string = 'Javaaaascript'
comp = re.compile('[Jj]ava')
re_obj = comp.match(string)

if re_obj:
    print('Pattern found!') # you need to give a pattern if you use 're', and if you use 'compile' you don`t need to use pattern
else:
    print('Pattern not found!')
