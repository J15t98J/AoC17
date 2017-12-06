import copy
banks = list(map(int, open("6.txt", "r").read().splitlines()[0].split("\t")))
bank_history = []
while True:
    if banks in bank_history:
        print(len(bank_history), len(bank_history) - bank_history.index(banks))
        break
    bank_history.append(copy.deepcopy(banks))
    value = list(reversed(sorted(banks)))[0]
    index = banks.index(value)
    banks[index] = 0
    for x in range(index+1, index+value+1):
        banks[x%len(banks)] += 1
