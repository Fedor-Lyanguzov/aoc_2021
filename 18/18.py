from functools import reduce as freduce
from itertools import permutations

class Regular:
    __slots__ = ['data']
    def __init__(self, x):
        self.data = x
    def __str__(self):
        return f'r{self.data}'
    __repr__ = __str__
    def __eq__(self, other):
        if isinstance(other, Regular):
            return self.data == other.data
        if isinstance(other, int):
            return self.data == other
        return False

def load_file(filename='input'):
    with open(filename) as f:
        for line in f:
            yield line.strip()

def add(x, y):
    return reduce(add_numbers(x, y))

def reduce(x):
    while True:
        if can_explode(x):
            x = explode(x)
            continue
        if can_split(x):
            x = split(x)
            continue
        break
    return x

def can_split(x):
    try:
        return next(filter(lambda k: k.data>=10, numbers(x)))
    except StopIteration:
        return False
    
def is_int(x):
    return isinstance(x, int)

def is_regular(x):
    return isinstance(x, Regular)

def is_pair(x):
    return isinstance(x, list)

def magnitude(x):
    if is_regular(x):
        return x.data
    return 3*magnitude(first(x)) + 2*magnitude(second(x))

def numbers(x):
    if is_regular(x):
        yield x
    elif is_pair(x):
        yield from numbers(first(x))
        yield from numbers(second(x))

def height(x, h=0):
    if is_regular(first(x)) and is_regular(second(x)):
        yield h, x
    if is_pair(first(x)):
        yield from height(first(x), h+1)
    if is_pair(second(x)):
        yield from height(second(x), h+1)

def can_explode(x):
    try:
        return next(filter(lambda k: k[0]==4, height(x)))
    except StopIteration:
        return None

def explode(where):
    what = can_explode(where)[1]
    replace_once(where, what, Regular(-1))
    k = list(numbers(where))
    i = k.index(Regular(-1))
    if i-1>=0:
        k[i-1].data += what[0].data
    if i+1<len(k):
        k[i+1].data += what[1].data
    k[i].data = 0
    update(where, iter(k))
    return where

def update(where, k):
    if where == -1:
        return
    if is_regular(first(where)):
        where[0] = next(k)
    if is_pair(first(where)):
        update(first(where), k)                   
    if is_pair(second(where)):
        update(second(where), k)
    if is_regular(second(where)):
        where[1] = next(k)


def replace_once(where, what, with_):
    def replace(where, what, with_):
        nonlocal found
        if is_pair(where):
            if first(where) is what and not found:
                where[0] = with_
                found = True
            elif second(where) is what and not found:
                where[1] = with_
                found = True
            if not found and is_pair(first(where)):
                replace(first(where), what, with_)
            if not found and is_pair(second(where)):
                replace(second(where), what, with_)
    found = False
    replace(where, what, with_)

def split(where):
    what = can_split(where)
    with_ = [Regular(what.data//2), Regular((what.data+1)//2)]
    replace_once(where, what, with_)
    return where

def first(x):
    return x[0]

def second(x):
    return x[1]

def add_numbers(x, y):
    return [x,y]

def from_string(s):
    return regularize(eval(s))

def regularize(x):
    def rec(x):
        if is_pair(x):
            if is_int(first(x)):
                x[0] = Regular(x[0])
            else:
                regularize(first(x))
            if is_int(second(x)):
                x[1] = Regular(x[1])
            else:
                regularize(second(x))
    rec(x)
    return x
        

def calculate(xs):
    return freduce(add, map(from_string, xs))

def test_magnitude():
    assert magnitude(regularize([9,1]))==29
    assert magnitude(regularize([1,9]))==21
    assert 143==magnitude(regularize([[1,2],[[3,4],5]]))
    assert 1384==magnitude(regularize([[[[0,7],4],[[7,8],[6,0]]],[8,1]]))
    assert 445==magnitude(regularize([[[[1,1],[2,2]],[3,3]],[4,4]]))
    assert 791==magnitude(regularize([[[[3,0],[5,3]],[4,4]],[5,5]]))
    assert 1137==magnitude(regularize([[[[5,0],[7,4]],[5,5]],[6,6]]))
    assert 3488==magnitude(regularize([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]))

def test_can_explode():
    assert can_explode(regularize([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]))
    assert can_explode(regularize([[[[0,7],4],[7,[[8,4],9]]],[1,1]]))
    assert can_explode(regularize([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]))

def test_can_split():
    assert can_split(regularize([[[[0,7],4],[15,[0,13]]],[1,1]]))
    assert can_split(regularize([[[[0,7],4],[[7,8],[0,13]]],[1,1]]))

def test_split():
    assert split(regularize([[[[0,7],4],[15,[0,13]]],[1,1]]))==[[[[0,7],4],[[7,8],[0,13]]],[1,1]]
    assert split(regularize([[[[0,7],4],[[7,8],[0,13]]],[1,1]]))==[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]

def test_explode():
    assert explode(regularize([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]))==[[[[0,7],4],[7,[[8,4],9]]],[1,1]]
    assert explode(regularize([[[[0,7],4],[7,[[8,4],9]]],[1,1]]))==[[[[0,7],4],[15,[0,13]]],[1,1]]
    assert explode(regularize([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]))==[[[[0,7],4],[[7,8],[6,0]]],[8,1]]
    
def test_add_simple():
    t1 = """
[1,1]
[2,2]
[3,3]
[4,4]
""".strip().split('\n')
    assert calculate(t1)==[[[[1,1],[2,2]],[3,3]],[4,4]]  
    t2 = """
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
""".strip().split('\n')
    assert calculate(t2)==[[[[3,0],[5,3]],[4,4]],[5,5]]  
    t3 = """
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
""".strip().split('\n')
    assert calculate(t3)==[[[[5,0],[7,4]],[5,5]],[6,6]]

def test_add_example():
    t = '''
[[[[4,3],4],4],[7,[[8,4],9]]]
[1,1]
'''.strip().split('\n')
    assert calculate(t)==[[[[0,7],4],[[7,8],[6,0]]],[8,1]]
    
def test_add_complex():
    t4 = """
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
""".strip().split('\n')
    assert calculate(t4[:2])==[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
    assert calculate(t4[:3])==[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]], 'похоже, при одинаковых заменах происходит пиздец'
    assert calculate(t4[:4])==[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
    assert calculate(t4[:5])==[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
    assert calculate(t4[:6])==[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
    assert calculate(t4[:7])==[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
    assert calculate(t4[:8])==[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
    assert calculate(t4[:9])==[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
    assert calculate(t4)==[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]  
    
    
if __name__ == '__main__':
    print(magnitude(calculate(load_file())))
    print(max(magnitude(calculate(x)) for x in permutations(load_file(), 2)))
    
