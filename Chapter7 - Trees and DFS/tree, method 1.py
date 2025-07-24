"""
trees are a type of graph where a node can hold at most two edges, a child and a parent
update:
    trees are a connected, acyclic graph. check these for examples.

[1]

[2]<---[3]--->[4]
               ^
               |
               |
               |
              [5]


NOT A TREE, 1 IS DISCONNECTED

[1]
 ^  \ 
 |   \ 
 |    \  
 |     >
[2]<---[3]---->[4]
                ^
                |
                |   
               [5]
NOT A TREE, 123 ARE CYCLIC

[1]
^
|
|
[2]<---[3]--->[4]
               ^
               |
               |
               |
              [5]
this is a tree 👍🏻

"""
from examplestructureoftree import *
# First problem of today, modelling a folder and file system and listing all the files present within a folder



#                         <pics>                  <- called a root node
#                        /      \                 <- edges of a graph/tree
#             odyssey.png        <2001>           <- parent node of a.png, child of pics
#                                 /   \   
#                             a.png   space.png           <- leaf nodes (no further children (South Korean))
                        

# let's build the name lister
# almost the same as BFS
def returnDirFiles(F:folder,iHave2returnObject=False):
    search_q=[F] #search queue, without the unimportant ueue
                 #Only folders allowed in this guy
    
    files_found=[] # i wonder what this could be
    while len(search_q) > 0: 
        element_folder=search_q.pop(0) # pick an element from the search q
        for element in element_folder.contents: #check the contents
            
            if type(element)==file and element:  
                files_found.append(element)
            else:                                       #which is why i implemented the raise in line 12
                
                    search_q.append(element)
            
    if iHave2returnObject:
        return files_found
    
    return [i.name for i in files_found]
print(returnDirFiles(pics))            

# turns out that due to the way tree traversing works, we dont need to check if a folder or file has already been visited.
# neato
