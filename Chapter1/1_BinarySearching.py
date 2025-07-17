def Bin_Search(arr,target):
    low=0
    high=len(arr)-1
    steps=0
    while (low<=high):
        mid=(low+high)//2
        # print("current mid : ",mid)
        if arr[mid]>target:
            # print(arr[mid],"Overstepping\n")
            high=mid-1
        elif arr[mid]<target:
            # print(arr[mid],"Under\n")
            low=mid+1
        else:
            # print("found! steps required: ",steps+1)
            # print(arr[mid],"matches search query, index = ",mid)
            return [mid,arr[mid],steps]
        steps+=1
    return [None,None,None]
print(Bin_Search(list(range(1,5+1)),1))

    
