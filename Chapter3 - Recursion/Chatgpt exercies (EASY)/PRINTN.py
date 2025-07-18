def Print(N):
    if N==1:
        print(N,end="")
        return
    else:
        print(N,end=" ")
    Print(N-1)
Print(10)