import math


def find_distance(input):
    last_square = math.floor(math.sqrt(input))
    loc = pow(last_square, 2)
    h_pos = math.ceil((last_square-2)/2) * (-1 if last_square % 2 == 0 else 1)
    v_pos = ((last_square-1)-abs(h_pos)) * (-1 if last_square % 2 == 0 else 1)
    if loc != input:
        h_pos += (1 if last_square % 2 == 1 else -1)
        loc += 1
        v_pos += min(input-loc, last_square)
        h_pos += (input-loc)%(last_square)
    print(abs(v_pos) + abs(h_pos))

find_distance(325489)


values = {}
x, y = 0, 0
directions = {"left": (-1, 0), "down": (0, 1), "right": (1,0), "up": (0,-1)}
direction = "right"

while True:
    # calculate value for this x,y
    sum = 0
    for (i, j) in [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]:
        if i != 0 or j != 0:
            try:
                sum += values.get(x+i).get(y+j)
            except Exception:
                continue

    # found it
    if(sum > 325489):
        print(sum)
        break

    # otherwise, store value for this x,y
    if not values.get(x):
        values[x] = {}
    values[x][y] = max(sum, 1)

    # corner? change directions
    if (abs(x) == abs(y) and (x != abs(x) or y != abs(y))) or (y >= 0 and x-y == 1):
        old = list(directions.keys()).index(direction)
        new = (old+1) % len(directions)
        direction = list(directions.keys())[new]

    # move to next x,y
    x += directions[direction][0]
    y += directions[direction][1]