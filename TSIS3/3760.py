n = int(input())
dict = {}
for i in range(n):
    key, value = input().split()
    dict[key] = value
s = input()
# for i in dict:
#     if s == i:
#         print(dict[i])
#     elif s == dict[i]:
#         print(i)
# 2 solution
for key, value in dict.items():
    if s == key:
        print(dict[s])
    elif s == dict[key]:
        print(key)