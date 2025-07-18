def Sum(N):
    if N==0:
        return 0
    return N+(Sum(N-1))
print(Sum(10))