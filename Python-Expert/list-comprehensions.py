#!/usr/bin/python3

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    elements = [[i, ii, iii] for i in range(0, x+1) for ii in range(0, y+1) for iii in range(0, z+1)]

    new_elements = [element for element in elements if sum(element) != n]

    print(f"Before {elements}")

    print(f"After {new_elements}")
