def Revstr(string):
    if len(string)<=1:
        return string
    return string[-1]+Revstr(string[1:-1])+string[0]
    
print(Revstr('hello'))