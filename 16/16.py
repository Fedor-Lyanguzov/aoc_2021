from math import prod
with open("input") as f:
    data = f.read().strip()

trt = {x: list(f'{int(x, base=16):04b}') for x in '0123456789ABCDEF'}

def take(n, rest, tail, tr):
    if not tr:
        l = len(rest)
        return list(rest)+list(tail[:n-l]), [], tail[n-l:]
    head = []
    while n>len(rest) and tail:
        head += rest
        n -= len(rest)
        a, *tail = tail
        rest = trt[a]
    head += rest[:n]
    rest = rest[n:]
    return head, rest, tail

def make_val(r, t, tr):
    val = []
    h, r, t = take(5, r, t, tr)
    while h[0]!='0':
        val.extend(h[1:])
        h, r, t = take(5, r, t, tr)
    val.extend(h[1:])
    val = int(''.join(val), base=2)
    return val, r, t

def make_by_len(r, t, tr):
    res = []
    while t:
        pak, r, t = make_pak(r, t, tr)
        res.append(pak)
    return res

def make_by_count(l, r, t, tr):
    res = []
    for _ in range(l):
        pak, r, t = make_pak(r, t, tr)
        res.append(pak)
    return res, r, t
    
def make_pak(r, t, tr):
    h, r, t = take(3, r, t, tr)
    ver = ''.join(h)
    h, r, t = take(3, r, t, tr)
    typ = ''.join(h)
    if typ=='100':
        val, r, t = make_val(r, t, tr)
        return (ver, typ, val), r, t
    else:
        (ltid,), r, t = take(1, r, t, tr)
        if ltid=='0':
            l, r, t = take(15, r, t, tr)
            l = int(''.join(l), base=2)
            h, r, t = take(l, r, t, tr)
            return (ver, typ, make_by_len([], h, tr=False)), r, t
        else:
            l, r, t = take(11, r, t, tr)
            l = int(''.join(l), base=2)
            paks, r, t = make_by_count(l, r, t, tr)
            return (ver, typ, paks), r, t

def sum_ver(pak):
    ver, typ, val = pak
    if typ=='100':
        return int(ver, base=2)
    else:
        return int(ver, base=2)+sum(sum_ver(pak) for pak in val)

def test_a():
    paks, _ ,_ = make_by_count(1, [], list('D2FE28'), True)
    assert paks[0][2] == 2021
def test_b():
    paks, _ ,_ = make_by_count(1, [], list('38006F45291200'), True)
    p1, p2 = paks[0][2]
    assert p1[2]==10 and p2[2]==20
def test_c():
    paks, _ ,_ = make_by_count(1, [], list('EE00D40C823060'), True)
    p1, p2, p3 = paks[0][2]
    assert p1[2]==1 and p2[2]==2 and p3[2]==3
    
def test_1():
    paks, _ ,_ = make_by_count(1, [], list('8A004A801A8002F478'), True)
    assert sum_ver(paks[0])==16
def test_2():
    paks, _ ,_ = make_by_count(1, [], list('620080001611562C8802118E34'), True)
    sum_ver(paks[0])==12
def test_3():
    paks, _ ,_ = make_by_count(1, [], list('C0015000016115A2E0802F182340'), True)
    sum_ver(paks[0])==23
def test_4():
    paks, _ ,_ = make_by_count(1, [], list('A0016C880162017C3686B18A3D4780'), True)
    sum_ver(paks[0])==31

def test_bug1():
    _, r, t = take(22, [], list('C0015000016115A2E0802F182340'), True)
    _, r, t = take(84, r, t, True)
    assert len(r)==2 and len(t)==1    

def calculate(pak):
    ver, typ, val = pak
    typ = int(typ, base=2)
    if typ==0:
        return sum(calculate(pak) for pak in val)
    elif typ==1:
        return prod(calculate(pak) for pak in val)
    elif typ==2:
        return min(calculate(pak) for pak in val)
    elif typ==3:
        return max(calculate(pak) for pak in val)
    elif typ==4:
        return val
    elif typ==5:
        p1, p2 = val
        return 1 if calculate(p1)>calculate(p2) else 0
    elif typ==6:
        p1, p2 = val
        return 1 if calculate(p1)<calculate(p2) else 0
    elif typ==7:
        p1, p2 = val
        return 1 if calculate(p1)==calculate(p2) else 0
    else:
        raise ValueError('Incorrect packet type')


if __name__ == '__main__':
    paks, _ ,_ = make_by_count(1, [], list(data), True)
    print(sum_ver(paks[0]))
    print(calculate(paks[0]))
    
    
