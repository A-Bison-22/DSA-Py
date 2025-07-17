"""
Here's how a selection sort works (from what i've understood)
{
    1. Find the min in the arr[0:len],
        Swap the found min with the arr[0]
    3. Find the next smallest min in the arr[1:len],
        Swap the found min with the arr[1]
    .
    .
    .
    n. Find the nth smallest min in the arr[len-1:len]  (only one el)
        Swap the found with arr[len-1]
}

Dry Running { 

    First Example:
        [5,4,3,2,1]
            smallest: 1, swap at 0
        [1,4,3,2,5]
            Smallest: 2, swap at 1
        [1,2,3,4,5]
            SORTED!

    Second Example:
        [5,3,8,1] ↖
                    check 0:4, smallest: 1, swap @ 0
        [1,3,8,5] ↖
                    check 1:4, smallest: 3, swap @ 1
        [1,3,8,5] ↖
                    check 2:4, smallest: 5, swap @ 2 
        [1,3,5,8] ↖
                    Check 3:4, smallest: 8, swap @ 3
        Sorted!        
}
Finding complexity 
{
    1st Iteration : Checks N-0 elements in arr[0,N]
    2nd Iteration : Checks N-1 elements in arr[1,N]
    .
    .
    .
    Nth Iteration : Checks N-(N-1) elements in arr[N-1,N]

    Hence net ops : Σ (j) {j = 1 -> N-1} = N(N-1)/2   
    and O(N^2/2 - N/2) = O(N^2)
}

Proof that it will always work {
    Do we really need one?
    I mean come on, this is simple enough
}
"""
L=[5,3,1,8,0,0,0,0]
def SelectionSort(L):
    N=len(L)
    #first we set the check ranges
    st=0 #start index
    # swp_indx=0
    while st<N-1:
        #then we check for the smallest in the range [st,Len)
        temp=st
        smallest=float("inf")
        smallest_indx=None
        for i in range(st,N):
            if L[i]<smallest:
                smallest=L[i]
                smallest_indx=i
        # now that we have the smallest in the set range
        # we swap it with the set swp_indx

        # L[swp_indx],L[smallest_indx]=L[smallest_indx],L[swp_indx]
        L[st],L[smallest_indx]=L[smallest_indx],L[st]
            
        st+=1
        # swp_indx+=1  # observation : swp_indx=st at all points so we can just replace swp_indx with st
    return L
print(SelectionSort(L))


