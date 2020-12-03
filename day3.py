with open('input3.txt') as fin:
    puzzleinput = fin.read()


def parse(data):
    x = [x for x in data.split('\n')]
    return x


a = parse(puzzleinput)


def part_1(L):
    num = 0
    count = 0
    for i in range(len(L)):
        num = num % 31
        if L[i][num] == '#':
            count += 1
        num += 3
    return count


def part_2(L, a):
    count = 0
    num = 0
    for i in range(len(L)):
        num = num % 31
        if L[i][num] == '#':
            count += 1
        num += a
    return count


def solution():
    result = 1
    for i in range(1, 8, 2):
        result *= part_2(a, i)
    b = [x for i, x in enumerate(a) if i % 2 == 0]
    result *= part_2(b, 1)
    return result
