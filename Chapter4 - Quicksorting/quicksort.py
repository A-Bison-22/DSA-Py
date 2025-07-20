# My test for quicks0orting
def qsort(arr):
    if len(arr)<2:
        return arr
    low,high=0,len(arr)-1
    mid=(low+high)//2
    pivot=arr[mid]
    copy=arr[:mid]+arr[mid+1:]
    low_arr=[i for i in copy if i <= pivot]
    hgh_arr=[i for i in copy if i > pivot]
    return qsort(low_arr) + [pivot] + qsort(hgh_arr)
print(qsort([4,3,2,1]))

"""

I still don't quite understand the time complexity of the this algorithm,
The book I am learning from sets the pivot = arr[0]
but i've decided that arr[mid] is much more neater and efficient as the array
is immediately divided into two. Which is not only more intuitive, but i also feel 
(yes feel, no mathematical proof yet) that it is better.

"""
