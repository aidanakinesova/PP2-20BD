# Hex Color Code
import re

pattern = r'.(\#[A-Fa-f0-9]{3,6})'

n = int(input())
for i in range(n):
    s = input()
    x = re.findall(pattern, s)
    if x:
        print(*x, sep='\n')  # иуиууиу correct 