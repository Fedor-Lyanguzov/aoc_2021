from collections import defaultdict
with open("input") as f:
    data = f.read().strip().split('\n')

data = [tuple(tuple(map(int, point.split(','))) for point in line.split(' -> ')) for line in data]
data1 = list(filter(lambda x: x[0][0]==x[1][0] or x[0][1]==x[1][1], data))

d = defaultdict(int)
for (x1,y1), (x2,y2) in data1:
    if x1==x2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            d[(x1, y)] += 1
    else:
        for x in range(min(x1,x2), max(x1,x2)+1):
            d[(x, y1)] += 1
k = sum(1 for (x, y), c in d.items() if c>1)
print(k)

d = defaultdict(int)
for (x1,y1), (x2,y2) in data:
    if x1==x2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            d[(x1, y)] += 1
    elif y1==y2:
        for x in range(min(x1,x2), max(x1,x2)+1):
            d[(x, y1)] += 1
    else:
        if x1>x2:
            x1,x2 = x2,x1
            y1,y2 = y2,y1
        y = 1 if y1<y2 else -1
        for x in range(x1, x2+1):
            d[(x, y1+(x-x1)*y)] += 1
k = sum(1 for (x, y), c in d.items() if c>1)
print(k)
