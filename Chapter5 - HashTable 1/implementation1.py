"""
LMAOOOOOO i used to think dictionaries are useless lollll turns out hashtables are called dictionaries in python

So, anyway, here's my first peice of hash table code : a voter system
"""
import time
voters={}
choice=True
while choice:
    name=input("Name : ")
    if name not in voters:
        voters[name]={"voted ": True,"Timestamp ":time.time()}
        print("Vote registration successful")

    else:
        print("You have voted before ")

    print("\n\n\n",voters,"\n\n\n")

    choice=(input("Continue ? (y/n)").lower()=="y")
"""
Only 1 file? Yes, only 1. The book im reading hasn't got a lot of content, it's made for beginners
"""
