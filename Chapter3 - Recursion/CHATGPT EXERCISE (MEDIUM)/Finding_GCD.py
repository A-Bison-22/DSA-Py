def GCD(a,b):
    rem= a%b
    if rem==0:
        return b
    return GCD(b,rem)

"""
Euclidean GCD Algorithm: 

GCD(39,42)
39 mod 42 = 39
42 mod 39 =  3
39 mod  3 =  0
        ^
        gcd


"""
print(GCD(1680,640))