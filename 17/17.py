'''
x=143..177, y=-106..-71
'''

target = (143, 177, -71, -106)

places = {
    (1,1,1,1): 'c',
    (1,0,0,1): 'tl',
    (1,1,0,1): 't',
    (0,1,0,1): 'tr',
    (1,0,1,1): 'l',
    (0,1,1,1): 'r',
    (1,0,1,0): 'bl',
    (1,1,1,0): 'b',
    (0,1,1,0): 'br',
}

def place(x, y, l, r, t, b):
    p1 = int(x<=r)
    p2 = int(x>=l)
    p3 = int(y<=t)
    p4 = int(y>=b)
    return places[(p1, p2, p3, p4)]


def sign(x):
    if x!=0:
        return x//abs(x)
    return 0

def step(x, y, dx, dy):
    return x+dx, y+dy, dx-sign(dx), dy-1

def shoot(dx, dy, target):
    state = (0, 0, dx, dy)
    p = place(0, 0, *target)
    best_y = 0
    while p in {'tl', 't', 'l'}:
        state = step(*state)
        best_y = max(state[1], best_y)
        p = place(*state[:2], *target)
    return p, best_y

def test():
    target = (20, 30, -5, -10)
    assert shoot(7, 2, target)[0]=='c'
    assert shoot(6, 3, target)[0]=='c'
    assert shoot(9, 0, target)[0]=='c'
    assert shoot(17, -4, target)[0]!='c'
    assert shoot(6, 9, target)==('c', 45)
    
    
if __name__ == '__main__':
    res = list(filter(lambda x: x[0]=='c', (shoot(dx, dy, target) for dy in range(-1000, 1000) for dx in range(1000))))
    print(max(res, key=lambda x: x[1]))
    print(len(res))
    
