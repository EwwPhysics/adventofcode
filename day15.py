with open('inputs/input15.txt') as fin:
    raw = fin.read()


def parse(raw):
    a = [int(x) for x in raw.split(',')]
    return a


a = parse(raw)


def solve(data, number):
    loc = {index: value for value, index in enumerate(data[:-1])}
    val = [data[-1], 1]
    while val[1] < (number - 2):
        num = val[0]
        index = val[1]
        if num in loc:
            val = [index - loc[num] + 1, index + 1]
            loc[num] = index + 1
        else:
            loc[num] = index + 1
            val = [0, index + 1]
    return val[0]


print(solve(a, 2020))
print(solve(a, 30000000))
