sum = 0
for i in range(1, 20, 4):
    sum += 4 / i
for i in range(3, 20, 4):
    sum += -(4 / i)
print(sum)