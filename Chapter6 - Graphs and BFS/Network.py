"""

i barely know any oop but regardless, here's my implementation of a social network simulator
the main thing i wanted to do is not only test my OOP but also try my hand on BFS by only 
reading the psuedocode

"""
# This model is based on every person having a unique name, add a unique parameter ID if you want to match it to your requirements
class Person:
    def __init__(self,name:str,friends: list):
        
        for i in friends:
            if type(i)!= Person:
                raise TypeError ("All friends must be of type Person, not "+str(type(i)))
            
        self.name=name
        self.friends=friends                                                                

        for i in self.friends:    # make the friendship bi-directional            # i am making some improvements, like, if i make a person Abhyudai=("Abhyudai",[XYZ]), then XYZ=Person("XYZ",[Abhyudai]) will be automatically created. 
            if i not in self.friends: # just making sure                          # Not that i need to, but it feels good to
                i.friends.append(self)
    
# Second degree connections
peggy=Person("peggy",[])
anuj=Person("anuj",[])
thom=Person("thom",[])
jonny=Person("jonny",[])                      # visual : https://postimg.cc/yDqSSq5f

# first degree connections
alice=Person("alice",[peggy])
bob=Person("bob",[anuj,peggy])
claire=Person("claire",[thom,jonny])

# you
you=Person("you",[bob,alice,claire])
                                    # this thing below me in case you want the full ugly class output
def search(you:Person,target:Person,OnlyPrintNames=True):                                                             # the more you know the more you know that you dont know shit
    #make a list of 1st deg connections
    search_q=[(i,[you,i]) for i in you.friends]
    # make a visited lists so we dont double count
    visited=[you]
    min_len=float('inf')
    while len(search_q)>0:
        #remove and check element 0 as tuple ( xx , xx )
        #who the current person of interest is and add the said person's name to current path 
        current_person,path=search_q.pop(0)

        if current_person.name==target.name: #change to person id in the future                   
            ### print("Found ! "," > ".join([p.name for p in path]))
            if len(path) < min_len:
                smallest_path=path
                min_len=len(path)
        
        if current_person not in visited: # this is why (we dont wanna recount people)
            visited.append(current_person)
            
            for friend in current_person.friends: # add that persons friend to the search q 
                if friend not in visited:
                    search_q.append((friend,path+[friend]))
    if OnlyPrintNames:
        return [i.name for i in smallest_path]
    else:
        return smallest_path

print(search(peggy,thom))
