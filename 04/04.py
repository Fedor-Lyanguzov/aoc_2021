from itertools import compress, chain
from collections import defaultdict
data = '''
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''.strip().split('\n', 1)

with open("input") as f:
    data = f.read().strip().split('\n', 1)
numbers = list(map(int, data[0].split(',')))
tables = data[1].strip().split('\n\n')
tables = [[list(map(int, x.split())) for x in t.split('\n')] for t in tables]

table_hits = [0]*len(tables)
index = defaultdict(list)
for i, table in enumerate(tables):
    for y, row in enumerate(table):
        for x, number in enumerate(row):
            index[number].append((i,x,y))

def find_sum(winner):
    t = tables[winner]
    w = bin(table_hits[winner])[2:][::-1]
    w = w + '0'*(25-len(w))
    w = list(map(lambda x: 1 if x=='0' else 0, w))
    return sum(compress(chain(*t), w))

row = 0b11111
column = 0b0000100001000010000100001
def win(i):
    for shift in range(5):
        if table_hits[i] & (row << shift*5)== row << shift*5:
            return True
    for shift in range(5):
        if table_hits[i] & (column << shift)== column << shift:
            return True
    return False

winners = []
w = set()
for number in numbers:
    for i, x, y in index[number]:
        table_hits[i] |= 1 << (y*5+x)
        if win(i) and i not in w:
            winners.append(number*find_sum(i))
            w.add(i)
            
print(winners[0])
print(winners[-1])
