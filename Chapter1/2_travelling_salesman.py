from random import randint
from random import shuffle
#lets take 5 random cities' coordinates
cities=[[1,2],[3,4],[4,3],[2,1],[12,5],[1,1]] # and of course, this list is ordered
# the problem asks us, in what order should we visit the cities so as to cover the minimum distance
# now of course, the plotting these points on a graph would easily let us conclude that 
# the path that kind of traces the boundary of the polygon thus formed
# but that's kinda tough for an algorithm (or maybe im just too pussy to code it)
# regardless, here's our approach in the very infamous O(n!) time

"""

1. Create a randomised list
2. Is this list already checked? if no: 
3. distance += distance of arr[1] from arr[0], arr[2] from arr[1] and so on
    3.1 : The salesman will always start at (0,0) and make a closed path
4. store [random_list,distance] in list dists[]
5. return pair with min(dist)

"""

#first we create the distance finder
def returnListDist(L):
    dist = 0
    start = [0, 0]
    dist += ((L[0][0] - start[0])**2 + (L[0][1] - start[1])**2)**0.5
    for i in range(1, len(L)):
        dist += ((L[i][0] - L[i-1][0])**2 + (L[i][1] - L[i-1][1])**2)**0.5
    dist += ((start[0] - L[-1][0])**2 + (start[1] - L[-1][1])**2)**0.5
    return dist

#then we create the list randomiser
def returnListIterations(L):
    if len(L) == 0:
        return [[]]
    result = []
    for i in range(len(L)):
        rest = L[:i] + L[i+1:]
        for p in returnListIterations(rest):            # Borrowed from ChatGPT, need to make own
            result.append([L[i]] + p)
    return result

# finally
def SalesmanTravels(L):
    pairs=[]
    Perms=returnListIterations(L)
    for i in range(0,len(Perms)):
        pairs.append([Perms[i],returnListDist(Perms[i])])
    min_dist=float('inf')
    min_dist_index=0
    for i in range(0,len(pairs)):
        if pairs[i][1]<min_dist:
            min_dist=pairs[i][1]
            min_dist_index=i
    return pairs[min_dist_index]

print(SalesmanTravels(cities))

