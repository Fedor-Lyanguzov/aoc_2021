with open("input") as f:
    data = f.read().strip().split('\n')
    data = [int(x) for x in data]

print(sum([1 for x,y in zip(data, data[1:]) if y-x>0]))
d2 = [a+b+c for a,b,c in zip(data, data[1:], data[2:])]
print(sum([1 for x,y in zip(d2, d2[1:]) if y-x>0]))
