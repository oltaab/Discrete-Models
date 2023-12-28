import random

def fast_mod_exp(base, exp, n):
    if (exp == 0):
        return 1
    if(exp == 1):
        return base%n 
    if(exp % 2 == 0):
        temp = fast_mod_exp(base, exp//2, n)
        return (temp*temp)%n
    return (base*fast_mod_exp(base, exp-1, n)) % n

def find_k_and_m(n):
    k=0
    m=0
    while(n % 2**k == 0):
        m = n // 2**k
        k += 1
    return k-1,m 

def miller_rabin(n, rounds=5):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    k, m = find_k_and_m(n - 1)

    for _ in range(rounds):
        a = random.randint(2, n - 2)
        x = fast_mod_exp(a, m, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(k - 1):
            x = fast_mod_exp(x, 2, n)
            if x == n - 1:
                break
        else:  
            return False

    return True

print(miller_rabin(7))
