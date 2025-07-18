def CountDigits(N,i=0):
    rem=N%10**i
    if rem == N:
        return i
    return CountDigits(N,i+1)
print(CountDigits(1345))
