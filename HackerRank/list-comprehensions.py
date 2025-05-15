#!/usr/bin/python3


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


    values = [[i, ii, iii] for i in range(x+1) for ii in range(y+1) for iii in range(z+1) if sum([i, ii, iii]) != n]
    # print(values)
    # values = [x for x in values if sum(x) != n]

    print(values)

