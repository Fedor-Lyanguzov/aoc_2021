from itertools import combinations
with open("input") as f:
    data = f.read().strip().split('\n')
data = [[s.split() for s in d.split('|')] for d in data]

print(sum(sum(1 if len(y) in {2,3,4,7} else 0 for y in x) for _, x in data))

known = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}
s = 0
for digits, number in data:
    real = {}
    for digit in digits:
        if len(digit) in known:
            real[known[len(digit)]] = set(digit)
    for x in combinations(digits, 9):
        base = set('abcdefg')
        for d in x:
            base = base.intersection(set(d))
        if len(base)==1:
            f = next(iter(base))
    real[2] = [d for digit in digits if len(d := set(digit))==5 and f not in d][0]
    real[3] = [d for digit in digits if len(d := set(digit))==5 and len(real[2]-d)==1 and len(d-real[2])==1][0]
    real[5] = [d for digit in digits if len(d := set(digit))==5 and d!=real[2] and d!=real[3]][0]
    real[9] = [d for digit in digits if len(d := set(digit))==6 and d==real[3] | real[4]][0]
    real[0] = [d for digit in digits if len(d := set(digit))==6 and len(d - real[5])==2][0]
    real[6] = [d for digit in digits if len(d := set(digit))==6 and d!=real[0] and d!=real[9]][0]
    real = {frozenset(v): k for k, v in real.items()}
    s += int(''.join(str(real[frozenset(n)]) for n in number))
print(s)
