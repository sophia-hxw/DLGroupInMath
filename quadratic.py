import math


def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
    return x1, x2

x1, x2 = quadratic(5, 12, 7)
print(x1, x2)



