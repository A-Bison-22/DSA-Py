class folder:
    def __init__(self,name:str,contents=[]):
        self.name=name
        self.contents=contents
        for i in contents:
            if type(i) != folder and type (i) != file:
                raise TypeError("contents of a folder can only ever be other folders and files")
    def addContent(self,item):                                                                                              #TO DO 24-07-25 : Add a path of file functionality to rDF() in method 1
        if type(item) != folder and type(item) != file:
            raise TypeError("Contents of a folder can only be other folders and files")    
        self.contents.append(item)
        return +1
class file:
    def __init__(self,name:str):
        self.name =name



a=file("a.png")
space=file("space.png")
f2001=folder("2001",[a,space])  #folder-2001, cuz of the naming rules
odyssey=file("odyssey.png")
pics=folder('pics',[f2001,odyssey])
