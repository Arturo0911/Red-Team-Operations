#!/usr/bin/python


class Polynomial:
    def __init__(self, *coeffs) -> None:
        self.coeffs = coeffs

    def __repr__(self) -> str:
        return "Polynomial(*{!r})".format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

# def main():
p1 = Polynomial(2, 3, 4) # 2x² + 3x + 4
p2 = Polynomial(3, 3, 3) # 3x² + 3x + 3
