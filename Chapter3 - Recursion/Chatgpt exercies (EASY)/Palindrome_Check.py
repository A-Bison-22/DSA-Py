def isPal(string):
    if len(string)<=1:
        return True
    if string[0] != string[-1]:
        return False
    return isPal(string[1:-1])
print(isPal("madam"))
print(isPal("Hello"))
