import copy


with open('input8.txt') as fin:
    raw = fin.read()


def parse(raw):
    start = [[x[:3], int(x[4:])] for x in (raw.split('\n'))]
    return start


a = parse(raw)


def part_1(arr):
    indices = set()
    acc = 0
    i = 0
    while i < len(arr):
        pair = arr[i]
        if i in indices:
            break
        indices.add(i)
        if pair[0] == 'acc':
            acc += pair[1]
        elif pair[0] == 'jmp':
            i += (pair[1] - 1)
        else:
            pass
        i += 1
    return acc


def is_infinite(arr):
    indices = set()
    acc = 0
    i = 0
    while True:
        if i in indices:
            return [True]
        indices.add(i)

        if i == len(arr):
            return [False, acc]

        pair = arr[i]

        if pair[0] == 'acc':
            acc += pair[1]
            i += 1
        elif pair[0] == 'jmp':
            i += pair[1]
        else:
            i += 1


def part_2(arr):
    for i, x in enumerate(arr):
        if x[0] == 'jmp':
            test = copy.deepcopy(arr)
            test[i][0] = 'nop'
            if is_infinite(test)[0]:
                pass
            else:
                return is_infinite(test)[1]
        if x[0] == 'nop':
            test = copy.deepcopy(arr)
            test[i][0] = 'jmp'
            if is_infinite(test)[0]:
                pass
            else:
                return is_infinite(test)[1]


print(part_1(a))
print(part_2(a))
