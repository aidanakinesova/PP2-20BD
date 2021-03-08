# Validating and Parsing Email Addresses  ;)
import re

list = []
n = int(input())
pattern = r'\<[A-Za-z][0-9A-Za-z-._]*\@[a-zA-Z]+\.[a-zA-Z]{1,4}\>'
for i in range(n):
    s = input()
    if re.search(pattern, s):
        print(s) # correct yo!