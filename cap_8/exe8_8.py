def mdc(a,b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a,b):
    return abs(a*b) / mdc(a,b)

print("MMC 10 e 5 --> %d" % mmc(10,5))
print("MMC 32 e 24 --> %d" % mmc(32,24))
print("MMC 5 e 3 --> %d" % mmc(5,3))
