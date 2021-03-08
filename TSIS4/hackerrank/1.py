# defect floating point number
import re

n = int(input())
for i in range(n):
    x = input()
    print(bool(re.match(r'^[+-]?[0-9]*\.[0-9]+$', x))) # coRRect!