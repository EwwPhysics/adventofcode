with open('inputs/input25.txt') as fin:
    raw = fin.read()


def parse(raw):
    x = [int(x) for x in raw.splitlines()]
    return x


a = parse(raw)


def loop(public):
    i = 1
    val = 1
    while True:
        val = (val * 7) % 20201227
        if val == public:
            return i
        i += 1


def part_1(card, key):
    val = 1
    for i in range(key):
        val = (val * card) % 20201227
    return val


print(part_1(a[0], loop(a[1])))
