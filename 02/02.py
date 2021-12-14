with open("input") as f:
    data = f.read().strip().split('\n')
    data = [x.split() for x in data]

d = 0
x = 0
for com, i in data:
    i = int(i)
    if com=='forward':
        x += i
    elif com=='up':
        d -= i
    elif com=='down':
        d += i
print(d*x)

d = 0
x = 0
aim = 0
for com, i in data:
    i = int(i)
    if com=='forward':
        x += i
        d += aim*i
    elif com=='up':
        aim -= i
    elif com=='down':
        aim += i
print(d*x)

