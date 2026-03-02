
def algorithm1(seed, n):
    i = 1
    l = []
    x = []
    l.append(seed)
    while i <= n:
        l.append(((7**5) * l[i-1]) % 2147483647) #2^31 - 1 = 2147483647
        x.append(l[i] / 2147483647)
        i = i+1
    return x
    
