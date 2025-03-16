

from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)
for i in range(n):
    word = input()
    d[word].append(i + 1)

for j in range(m):
    word = input()
    if len(d[word]) > 0:
        print(' '.join([str(s) for s in d[word]]))
    else:
        print(-1)
