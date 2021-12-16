from timeit import timeit as _timeit
timeit = lambda x: _timeit(x, globals=globals(), number=1)
from collections import defaultdict

def find_min_risk(field):
    M = len(field[0])
    N = len(field)
    field = defaultdict(lambda: float("+inf"), {(i,j): int(x) for i, line in enumerate(field) for j,x in enumerate(line)})
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = []
    def f(i, j, s):
        stack.append((i,j,s))
        if d[(i,j)] <= s:
            return
        d[(i,j)] = s
        if (i, j) == (N-1, M-1):
            return
        for di, dj in directions:
            f(i+di, j+dj, s+field[(i,j)])
    d = defaultdict(lambda: float("+inf"))
    f(0,0,0)
    return d[(N-1, M-1)]

def find_min_risk_opt1(field):
    M = len(field[0])
    N = len(field)
    field = defaultdict(lambda: float("+inf"), {(i,j): int(x) for i, line in enumerate(field) for j,x in enumerate(line)})
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(0,0,0)]
    d = defaultdict(lambda: float("+inf"))
    while stack:
        i, j, s = stack.pop()
        if d[(i,j)] <= s:
            continue
        d[(i,j)] = s
        if (i, j) == (N-1, M-1):
            continue
        stack.extend([(i+di, j+dj, s+field[(i,j)]) for di, dj in directions][::-1])
    return d[(N-1, M-1)]

statement_field = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".strip().split('\n')
print('a1:', timeit('assert find_min_risk(statement_field)==40'))
print('b1:', timeit('assert find_min_risk_opt1(statement_field)==40'))

statement_field = """
1163751742
1381373672
2135511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944582
""".strip().split('\n')
x = int(statement_field[0][0])
y = int(statement_field[-1][-1])
print('a2:', timeit('assert find_min_risk(statement_field)-x+y==40'))
print('b2:', timeit('assert find_min_risk_opt1(statement_field)-x+y==40'))

with open("input") as f:
    field = f.read().strip().split('\n')
    
x = int(field[0][0])
y = int(field[-1][-1])
print('b3:', timeit('print(find_min_risk_opt1(field)-x+y)'))



