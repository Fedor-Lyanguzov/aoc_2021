from timeit import timeit
data = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
""".strip().split('\n')

with open("input") as f:
    data = f.read().strip().split('\n')

d = {tuple(line.split('-')) for line in data}
small = {x for pair in d for x in pair if x.islower()} - {'start', 'end'}


def make_paths(d, valid_path):
    def f(v, path):
        if path.count('start')>1:
            return
        if not valid_path(path):
            return
        if v=='end':
            yield path
            return
        for next_v in {x for x, y in d if y==v}|{y for x, y in d if x==v}:
            yield from f(next_v, path+[next_v])
    yield from f('start', ['start'])

valid_path = lambda x: all(x.count(v)<=1 for v in small)
print(sum(1 for p in make_paths(d, valid_path)))

def valid_path(path):
    if any(path.count(v)>2 for v in small):
        return False
    if sum(1 for v in small if path.count(v)==2)>1:
        return False
    return True

print(timeit('print(sum(1 for p in make_paths(d, valid_path)))', globals=globals(), number=1))


    

