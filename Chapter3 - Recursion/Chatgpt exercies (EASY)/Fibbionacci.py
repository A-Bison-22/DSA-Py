def Fib(N):
    if N==0:
        return 1
    if N==1:
        return 1
    return Fib(N-1)+Fib(N-2)
