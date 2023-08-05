def f(x):
    return ((72%x==0) <= (120%x!=0)) or (A-x > 100)

for A in range(1,200):
    if all(f(x)==1 for x in range(1,10000)):
        print(A)
        break