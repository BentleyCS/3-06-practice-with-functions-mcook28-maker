import math
def root(n):
    return math.sqrt(n)
def semiPerimeter(a, b, c):
    return (a + b + c) / 2
def multiplyDifferences(a, b, c, d):
    return a * (a - b) * (a - c) * (a - d)
def herons(a, b, c):
    s = semiPerimeter(a, b, c)
    area_squared = multiplyDifferences(s, a, b, c)
    return root(area_squared)
def denominator(a):
    return a * 2
def plusMinus(a, b):
    return (-a + b, -a - b)
def mainCalc(a, b, c):
    return (b ** 2) - (4 * a * c)
def quadratic(a, b, c):
    discriminant = mainCalc(a, b, c)
    sqrt_disc = root(discriminant)
    numerator_plus, numerator_minus = plusMinus(b, sqrt_disc)
    denom = denominator(a)
    return (numerator_plus / denom, numerator_minus / denom)
# ---- TEST ----
print("Heron's triangle area (3,4,5):", herons(3, 4, 5))
print("Quadratic roots (a=1, b=-3, c=2):", quadratic(1, -3, 2))