def checksort(arr):
    if len(arr)<=1:
        return True
    if arr[0]<=arr[1]:
        return checksort(arr[1:])
    else:
        return False
def checksort2(arr,i=0):
    if i>=len(arr)-1:
        return True
    if arr[i]>arr[i+1]:
        return False
    return checksort2(arr,i+1)
print(checksort2([1,3,4,5,6]))

