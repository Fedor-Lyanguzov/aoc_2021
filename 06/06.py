from collections import Counter
with open("input") as f:
    data = f.read().strip().split(',')
data = list(map(int, data))

_data = data
for _ in range(80):
    if _%80==0:
        print(_)
    new_data = []
    new_fish = []
    for x in _data:
        if x==0:
            new_fish.append(8)
            new_data.append(6)
        else:
            new_data.append(x-1)
    _data = new_data + new_fish

print(len(_data))

_data = [0]+[y for x, y in sorted(Counter(data).items(), key=lambda x: x[0])]+[0,0,0]
for _ in range(256):
    x = _data[0]
    _data = _data[1:] + [_data[0]]
    _data[6] += x
print(sum(_data))
    

