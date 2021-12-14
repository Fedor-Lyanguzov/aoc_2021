import csv
from collections import Counter, defaultdict
template, rules = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".strip().split('\n\n')
with open("input") as f:
    template, rules = f.read().strip().split('\n\n')
rules = {k: v for k, v in (line.split(' -> ') for line in rules.split('\n'))}

def f(template):
    for _ in range(5):
        new_template = []
        for a, b in zip(template, template[1:]):
            if a+b in rules:
                new_template.append(a+rules[a+b])
            else:
                new_template.append(a)
        new_template.append(template[-1])
        new_template = ''.join(new_template)
        template = new_template
    return template

c = Counter(f(f(template)))
print(max(c.values()) - min(c.values()))

class MyCounter(Counter):
    def __mul__(self, n):
        return MyCounter({k: v*n for k, v in self.items()})
    
d = MyCounter(zip(template, template[1:]))
for _ in range(8):
    d = sum((MyCounter(zip(l:=f(''.join(x)), l[1:]))*v for x, v in d.items()), start=MyCounter())
res = defaultdict(int)
for (a, b), v in d.items():
    res[b] += v
print((max(res.values()) - min(res.values())))
