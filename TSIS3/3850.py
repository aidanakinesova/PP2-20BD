# 4 0 5 0 3 0 0 5
# 4 5 3 5 0 0 0 0

num = list(map(int, input().split()))
x = 0
for i in num:
    if i != 0:
        print(i, end=' ')
    else:
        x += 1
print('0 ' * x)

