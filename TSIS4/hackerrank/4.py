# Re.findall() & Re.finditer() ;)

# import re

# x = re.findall(r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]([AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]', input())
# if x:
#     for i in x:
#         print(i)
# else:
#     print(-1)



text = 'ул. Карпинского, дом № 5, корпус 3, квартира 98'
import re
match = re.finditer(r'\d+', text)
for i in match:
    print(i.start(), i.end())

# 23 24
# 33 34
# 45 47