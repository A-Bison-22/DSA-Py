# this method uss recursion to list out the files
from examplestructureoftree import *
def printfiles(F:folder):
    for f in F.contents:                # funny thing here is that there is no base case, it kind of just does it's thing
        path=f                          # it's kind of how a person would list out all the files yknow
        if type(f) == file:
            print(f.name)
        if type(f) == folder:
            printfiles(f)
printfiles(pics)

"""
in the first method, the order of output is:
    odyssey, a, space
but in the recursive method it is:
    a,space,odyssey

simple explanation, in the first bfs-like method, we prioritise on the file input,
we just add the folders to the search q and wait for python to do it's thing
so, from <pics>, python takes out odyssey first, while putting f2001 in the uhhhhhhh
search q, and when it gets to that, it outputs a and space

but in the recursive bit, the code prioritises exploring the folders first. Hence, 
when it sees the folder <f2001> popping up in <pics>, it doesn't care for the 
adjacent file, it goes in and prints out the inner files a and space, comes back 
from the call stack and then looks over to the next content.

"""
