# Linear Diophantine Equations

## Overview
The linear Diophantine equation is expressed as `ax + by = c`, where `a`, `b`, `c` are fixed integers (ℤ).

A solution pair `x`, `y` (both integers) exists if and only if `gcd(a, b) = d` divides `c` (notated as `d | c`), meaning `c = d * m` for some integer `m`.

## Finding a Solution
A pair of solutions can be found using the Extended Euclidean Algorithm. If `d = ax' + by'`, then `c = dm = a(x'm) + b(y'm)`. Thus, we can set `x = x'm` and `y = y'm`.

Every solution takes the form:
x = x' * m + k * (b / d) and y = y' * m - k * (a / d)

for all `k` in ℤ.

## Problem 1
How many ways we can pay 10^5 credits when we have only coins of value 47 and 79?

## Problem 2
In a shop, they sell different types of chocolates for 70, 130 and 150 credits. How many different ways you can buy 50 chocolates for 5000 credit?


