def factorial(N):
    if N==1:
        return 1
    if N==0:
        return 0   
    if N<0:
        return "Nice Try"
    return N*factorial(N-1)

"""
The “pile of boxes” is saved on the stack! This is a stack of halfcompleted function calls, each with its own half-complete list of boxes
to look through. Using the stack is convenient because you don’t have to
keep track of a pile of boxes yourself—the stack does it for you.
Using the stack is convenient, but there’s a cost: saving all that info can
take up a lot of memory. Each of those function calls takes up some
memory, and when your stack is too tall, that means your computer is
saving information for many function calls. At that point, you have two
options:
• You can rewrite your code to use a loop instead.
• You can use something called tail recursion. That’s an advanced
recursion topic that is out of the scope of this book. It’s also only
supported by some languages, not all.

"""