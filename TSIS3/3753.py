a, b = map(int, input().split())
n = []
m = []
for i in range(a):
    x = int(input())
    n.append(x)
for i in range(b):
    y = int(input())
    m.append(y)
lcom = len(set(n) & set(m))
com = (set(n) & set(m))
print(lcom)
print(*sorted(com))
print(len(n) - lcom)
print(*sorted(set(n) - com))
print(len(m) - lcom)
print(*sorted(set(m) - com))