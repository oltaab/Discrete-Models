def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def countSolutions(a, b, c):
    m = 0
    d = gcd(a, b)

    if c % d == 0:
        m = c // d
    else:
        return 0

    d, x_prime, y_prime = xgcd(a, b)

    x = x_prime * m
    y = y_prime * m

    solutions = 0
    k = -1

    if x >= 0 and y >= 0 and a * x + b * y == c:
        solutions = 1

    if a * x + b * y == c:
        while x >= 0:
            x = x + k * (b // d)
            y = y - k * (a // d)

            if x >= 0 and y >= 0:
                solutions += 1
        k -= 1

    return solutions

solutions = countSolutions(47, 79, 10**5)
print(solutions)
