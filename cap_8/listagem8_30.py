def soma(*args):
     s = 0
     for x in args:
         s += x
     return s
print(soma(1,2))
soma(2)
soma(5,6,7,8)
print(soma(9,10,20,30,40))
