# about phone number ;)
import re

n = int(input())
for i in range(n):
    x = input()
    a = re.match(r'^[7|8|9]\d{9}$', x)
    if a:
        print('YES')
    else:
        print('NO') # correct