"""

i barely know any oop but regardless, here's my implementation of a social network simulator
the main thing i wanted to do is not only test my OOP but also try my hand on BFS by only 
reading the psuedocode

"""
class person:
    def __init__(self,name:str,friends: list):

        for i in friends:
            if type(i)!= person:
                raise TypeError ("All friends must be of type person, not "+str(type(i)))
        
        self.name=name
        self.friends=friends

        for i in self.friends: #make sure that i am my friends' friend
            i.friends.append(self)
    
# Second degree connections
peggy=person("peggy",[])
anuj=person("anuj",[])                                                                               # visual : https://postimg.cc/yDqSSq5f
thom=person("thom",[])
jonny=person("jonny",[])

# first degree connections
alice=person("alice",[peggy])
bob=person("bob",[anuj,peggy])
claire=person("claire",[thom,jonny])

# you
you=person("you",[bob,alice,claire])

def search(you:person,target:person):
    #make a list of 1st deg connections                                                                # the more you know the more you know that you dont know shit
    search_q=[(i,[you,i]) for i in you.friends]
    # make a visited lists so we dont double count
    visited=[you]
    all_possible_paths=[]
    while len(search_q)>0:
        #remove and check element 0 as tuple ( xx , xx )
        #who the current person of interests is and add the said person's name to current path 
        current_person,path=search_q.pop(0)

        if current_person==target:
            ### print("Found ! "," > ".join([p.name for p in path]))
            all_possible_paths+=[path]
        
        if current_person not in visited: # this is why line #38 (we dont wanna recount people)
            visited.append(current_person)
            
            for friend in current_person.friends: # add that persons friend to the search q 
                if friend not in visited:
                    search_q.append((friend,path+[friend]))

    min_len=float("inf")
    smallest_path=[]
    for i in all_possible_paths:
        if len(i)<min_len:
            min_len=len(i)
            smallest_path=i
    return [i.name for i in smallest_path]

print(search(peggy,thom))
