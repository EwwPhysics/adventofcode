from itertools import chain

with open('inputs/input16.txt') as fin:
    raw = fin.read()


def parse(data):
    x = [x for x in data.split('\n')]
    x[:x.index('')] = [i.split(':')[1][1:] for i in x[:x.index('')]]
    ranges = x[:x.index('')]
    for a, b in enumerate(ranges):
        ranges[a] = b.split(' or ')
        ranges[a] = [i.split('-') for i in ranges[a]]
        ranges[a] = [int(item) for sublist in ranges[a] for item in sublist]
    x[:x.index('')] = ranges
    near = [i.split(',') for i in x[(x.index('nearby tickets:') + 1):]]
    for a, b in enumerate(near):
        for i, n in enumerate(b):
            near[a][i] = int(n)
    x[x.index('nearby tickets:') + 1:] = near
    return x


a = parse(raw)


def part_1(data):
    v = set()
    for a, b, c, d in data[:data.index('')]:
        v.update(list(chain(range(a, b + 1), range(c, d + 1))))
    near = data[(data.index('nearby tickets:') + 1):]
    valid = [ticket for ticket in near if len(set(ticket).intersection(v)) == len(set(ticket))]
    near = [item for sublist in near for item in sublist if item not in v]
    return sum(near), valid
