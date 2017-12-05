import re

count = 0
for line in open("4.txt", "r").readlines():
    count += 0 if re.compile(r"^.*?\b(\S+?)\b.+?\b(\1)\b.*?$").search(line) else 1
print(count)