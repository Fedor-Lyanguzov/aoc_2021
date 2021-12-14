with open("input") as f:
    data = f.read().strip().split('\n')

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    }
opens = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}
closings = {v: k for k, v in opens.items()}
second_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
    }


s = 0
ss = []
for line in data:
    parens = []
    for c in line:
        if c in scores:
            if opens[c] != parens[-1]:
                s += scores[c]
                break
            else:
                parens.pop()
        else:
            parens.append(c)
    else:
        if parens:
            x = 0
            for p in reversed(parens):
                x = x*5 + second_scores[closings[p]]
            ss.append(x)
                    
print(s)
print(sorted(ss)[len(ss)//2])
    

