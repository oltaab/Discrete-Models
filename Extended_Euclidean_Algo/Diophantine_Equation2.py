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

def countSolutions2(a1, b1, h1, c1, a2, b2, h2, c2):
    a = a1 + (h1 * -a2)
    b = b1 + (h1 * -b2)
    c = c1 - (h1 * c2)
    
    m = 0
    d = gcd(a, b)

    if c % d == 0:
        m = c // d
    else:
        return 0
    
    d, x_prime, y_prime = xgcd(a, b)
    
    x = x_prime * m
    y = y_prime * m

    z = (c2 - x - y)
    solutions = 0

    if x >= 0 and y >= 0 and z >= 0:
        solutions = 1
    
    k = -1
    
    while y > 0:
        x = x_prime * m + k * (b // d)
        y = y_prime * m - k * (a // d)
        z = (c2 - x - y)

        if x >= 0 and y >= 0 and z >= 0:
            solutions += 1 
        k -= 1 

    return solutions

solutions = countSolutions2(70, 130, 150, 5000, 1, 1, 1, 50)
print(solutions)
