fact(n=5):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input(enter))
fact(5)
