count, even_count = 0, 0
for x in open("2.txt", "r").readlines():
    line = sorted([int(y) for y in x.splitlines()[0].split("\t")])
    count += line[len(line)-1] - line[0]
    for (w,z) in [(x,y) for x in line for y in line]:
        even_count += int(z/w) if z//w == z/w != 1 else 0
print(count, even_count)
