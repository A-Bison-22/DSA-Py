"""
trees are a type of graph where a node can hold at most two edges, a child and a parent

"""
# First problem of today, modelling a folder and file system and listing all the files present within a folder
class folder:
    def __init__(self,name:str,contents=[]):
        self.name=name
        self.contents=contents
        for i in contents:
            if type(i) != folder and type (i) != file:
                raise TypeError("contents of a folder can only ever be other folders and files")
    def addContent(self,item):                                                                                              #TO DO 24-07-25 : Add a path of file functionality to rDF()
        if type(item) != folder and type(item) != file:
            raise TypeError("Contents of a folder can only be other folders and files")    
        self.contents.append(item)
        return +1
class file:
    def __init__(self,name:str):
        self.name =name


#hello hello hello hello white america assassinate my character
#money matrimony yeah they trynna break the marriage up

a=file("a.png")
space=file("space.png")
f2001=folder("2001",[a,space])  #folder-2001, cuz of the naming rules
odyssey=file("odyssey.png")
pics=folder('pics',[f2001,odyssey])

"""
                        <pics>                  <- called a root node
                       /      \                 <- edges of a graph/tree
            odyssey.png        <2001>           <- parent node of a.png, child of pics
                                /   \   
                            a.png   space.png           <- leaf nodes (no further children (South Korean))
                        
"""

# let's build the name lister
# almost the same as BFS
def returnDirFiles(F:folder,iHave2returnObject=False):
    search_q=[F] #search queue, without the unimportant ueue
                 #Only folders allowed in this guy
    
    files_found=[] # i wonder what this could be
    while len(search_q) > 0: 
        element_folder=search_q.pop(0) # pick an element from the search q
        for element in element_folder.contents: #check the contents
            
            if type(element)==file and element not in files_found:  
                files_found.append(element)
            else:                                       #which is why i implemented the raise in line 12
                if element not in search_q:
                    search_q.append(element)
            
    if iHave2returnObject:
        return files_found
    
    return [i.name for i in files_found]
print(returnDirFiles(pics))            
