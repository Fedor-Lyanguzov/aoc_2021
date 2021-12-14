from collections import defaultdict
data = '''
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''.strip().split('\n')
with open("input") as f:
    data = f.read().strip().split('\n')
data = [list(map(int, line)) for line in data]
N = len(data)*len(data[0])
d = defaultdict(lambda: -100000)
d.update({(i,j): x for i, row in enumerate(data) for j, x in enumerate(row)})

directions = {(x,y) for x in [-1,0,1] for y in [-1,0,1]}-{(0,0)}

s = 0
for _ in range(100):
    for c, x in d.items():
        d[c] = x+1
    ready = set()
    flashed = {c for c, x in d.items() if x>9 and c not in ready}
    while flashed:
        s += len(flashed)
        ready = ready | flashed
        for i, j in flashed:
            for di, dj in directions:
                d[(i+di, j+dj)] += 1
        flashed = {c for c, x in d.items() if x>9 and c not in ready}
    for c in ready:
        d[c] = 0

print(s)        

step = 0
ready = set()
flashed = {c for c, x in d.items() if x>9 and c not in ready}
while flashed:
    ready = ready | flashed
    for i, j in flashed:
        for di, dj in directions:
            d[(i+di, j+dj)] += 1
    flashed = {c for c, x in d.items() if x>9 and c not in ready}
while len(ready)!=N:
    for c in ready:
        d[c] = 0
    step += 1
    for c, x in d.items():
        d[c] = x+1
    ready = set()
    flashed = {c for c, x in d.items() if x>9 and c not in ready}
    while flashed:
        ready = ready | flashed
        for i, j in flashed:
            for di, dj in directions:
                d[(i+di, j+dj)] += 1
        flashed = {c for c, x in d.items() if x>9 and c not in ready}
print(step+100)
