with open("input") as f:
    data = f.read().strip().split('\n')

l = len(data)
gamma = [round(sum(map(int, x))/l) for x in zip(*data)]
epsilon = [0 if x==1 else 1 for x in gamma]
_gamma = int(''.join(map(str, gamma)), base=2)
_epsilon = int(''.join(map(str, epsilon)), base=2)
print(_gamma*_epsilon)

def f(g):
    i = 0
    x = data
    while len(x)>1:
        a = list(zip(*x))[i]
        b = a.count("1") >= a.count("0")
        x = [z for z in x if z[i]==g(b)]
        i += 1
    return int(x[0], base=2)


o2 = f(lambda b: "1" if b else "0")
co2 = f(lambda b: "0" if b else "1")

print(o2*co2)
