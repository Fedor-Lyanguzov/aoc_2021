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

def make_field(field):
    def tr(f, n):
        orig = '123456789'
        t = orig[n:]+orig[:n]
        return [line.translate(str.maketrans(orig, t)) for line in field]
    field = [[tr(field, (x+y)%9) for x in range(5)] for y in range(5)]
    res = []
    for y in field:
        res.extend([''.join(line)for line in zip(*y)])
    return res
    

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
statement_field = make_field(statement_field)
x = int(statement_field[0][0])
y = int(statement_field[-1][-1])
assert len(statement_field)==50
assert all(len(line)==50 for line in statement_field)
#print('a1:', timeit('assert find_min_risk(statement_field)-x+y==315'))
print('b1:', timeit('assert find_min_risk_opt1(statement_field)-x+y==315'))
with open("input") as f:
    field = f.read().strip().split('\n')    
field = make_field(field)
x = int(field[0][0])
y = int(field[-1][-1])
print('b3:', timeit('print(find_min_risk_opt1(field)-x+y)'))

