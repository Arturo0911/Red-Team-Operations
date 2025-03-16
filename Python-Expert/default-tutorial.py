#!/usr/bin/python3


from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().split())
    values = defaultdict(list)

    for x in range(0, n):
        value = input()
        values["A"].append(value)

    for xx in range(0, m):
        value2 = input()
        values["B"].append(value2)

for i in values.items():
    print(i)
