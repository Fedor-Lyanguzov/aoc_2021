with open("input") as f:
    data, folds = f.read().strip().split('\n\n')
data = {tuple(map(int, line.split(','))) for line in data.split('\n')}
folds = [(d[0], d[1]) for x in folds.split('\n') if (y := x.split('=')) and (d := (y[0][-1], int(y[1])))]

def print_data(data):
    for y in range(max(a[1] for a in data)+1):
        for x in range(max(a[0] for a in data), -1, -1):
            if (x, y) in data:
                print('#', end='')
            else:
                print('.', end='')
        print()

def make_fold(data, fold):
    d, n = fold
    if d=='x':
        first_pred = lambda x: x[0]<n
        second_pred = lambda x: x[0]>n
    else:
        first_pred = lambda x: x[1]<n
        second_pred = lambda x: x[1]>n

    first = set(filter(first_pred, data))
    second = set(filter(second_pred, data))
    if d=='y':
        second = {(x, n-(y-n)) for x, y in second}
    else:
        second = {(x-n-1, y) for x, y in second}
        first = {(-x+n-1, y) for x, y in first}
    return first | second

for fold in folds[:1]:
    data = make_fold(data, fold)
print(len(data))
for fold in folds[1:]:
    data = make_fold(data, fold)
print_data(data)
