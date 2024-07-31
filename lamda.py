x=lambda a:a*20
print(x(2))

m=lambda a,b:a*b
print(m(2,5))

def myfunction(n):
    return lambda a:a*n
nithin=myfunction(3)
print(nithin(1200000))


def myfunction(n):
    return lambda a:a*n
nithin=myfunction(3)
nithi=myfunction(6)
print(nithin(1200000))
print(nithi(1200000))