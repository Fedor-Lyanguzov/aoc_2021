with open("input") as f:
    data = list(map(int, f.read().strip().split(',')))

print(min(sum(abs(y-x) for y in data) for x in range(min(data), max(data)+1)))
print(min(sum(abs(y-x)*(abs(y-x)+1)//2 for y in data) for x in range(min(data), max(data)+1)))

    

