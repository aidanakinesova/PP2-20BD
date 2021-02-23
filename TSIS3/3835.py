num = list(map(int, input().split()))
mini = 1001
for i in num:
    if 0 < i < mini:
        mini = i
print(mini)