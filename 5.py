lines = list(map(int, open("5.txt", "r").readlines()))
pos, count = 0, 0
while pos < len(lines):
    count += 1
    mov = lines[pos]
    lines[pos] += 1 if lines[pos] < 3 else -1
    pos += mov
print("#", pos+1, "after", count, "moves")