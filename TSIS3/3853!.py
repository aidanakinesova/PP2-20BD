# 5 3 7 4 6
# 3
# output
# 7 4 6 5 3

num, k = list(map(int, input().split())), int(input())
k = k % len(num)
if k > 0:
    print(*(list[-k:]+list[:-k]))
else:
    k = abs(k)
    print(*(list[:-k] + list[-k:]))