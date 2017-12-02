sequence = open("1.txt", "r").read()
sequence += sequence[0]
count = 0
for x in range(len(sequence)-1):
    count += int(sequence[x]) if sequence[x] == sequence[x+1] else 0
print(count)

sequence = open("1.txt", "r").read()
length = len(sequence)
sequence += sequence
count = 0
for x in range(length):
    count += int(sequence[x]) if sequence[x] == sequence[x+int(length/2)] else 0
print(count)