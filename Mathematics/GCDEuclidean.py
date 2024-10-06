def gcd(a,b):
    if b == 0:
        print(a)
        return a
    gcd(b,a%b)

gcd(25,60)
