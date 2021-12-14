from math import prod
with open("input") as f:
    data = [[int(x) for x in line] for line in f.read().strip().split('\n')]
data = [[9]*len(data[0])] + data + [[9]*len(data[0])]
data = [[9]+line+[9] for line in data]

print(sum(1+data[i][j] for i in range(1, len(data)-1) for j in range(1, len(data[0])-1) if all(data[i][j]<data[i+di][j+dj] for di, dj in [(1,0), (0, 1), (-1, 0), (0, -1)])))

low = [(i,j) for i in range(1, len(data)-1) for j in range(1, len(data[0])-1) if all(data[i][j]<data[i+di][j+dj] for di, dj in [(1,0), (0, 1), (-1, 0), (0, -1)])]
directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
def basin_area(i, j):
    s = 0
    visited = set()
    def find_basin(i, j):
        nonlocal s
        if (i, j) in visited or data[i][j]==9:
            return
        visited.add((i,j))
        s += 1
        for di, dj in directions:
            find_basin(i+di, j+dj)
    find_basin(i, j)
    return s
print(prod(sorted([basin_area(*l) for l in low], reverse=True)[:3]))


    

