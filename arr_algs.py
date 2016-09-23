def minimum (arr):
    lit=arr[0]
    for i in arr:
        if i<lit:
            lit=i
    return lit

def midl (arr1):
    sum=0
    for l in arr1:
        sum=sum+l
    mid=sum/len(arr1)
    return mid

arr=[5,2,1,4,7]
lit=minimum(arr)
print(lit)
arr1=[1,2,3]
mid=midl(arr1)
print(mid)

