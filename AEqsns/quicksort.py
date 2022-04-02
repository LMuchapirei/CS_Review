


def quicksort(array):
    quickSortHelper(array,0,len(array)-1)
    return array

# O(nlog(n)) time and O(log(n)) space
def quickSortHelper(array,startIdx,endIdx):
    if startIdx >= endIdx:
        return 
    pivotIdx=startIdx
    leftIdx=startIdx+1
    rightIdx=endIdx

    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx,rightIdx,array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx+=1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx-=1

    swap(pivotIdx,rightIdx,array)
    leftSubarrayIsSmaller=rightIdx-1-startIdx < endIdx-(rightIdx+1)   # the left subarray starts at startIdx and ends at rightIdx-1  ,the right sub array starts at rightIdx+1 and ends at endIdx
    if leftSubarrayIsSmaller:
        quickSortHelper(array,startIdx,rightIdx-1)
        quickSortHelper(array,rightIdx+1,endIdx)
    else:
        quickSortHelper(array,rightIdx+1,endIdx)
        quickSortHelper(array,startIdx,rightIdx-1)


def swap(i,j,array):
    array[i],array[j]=array[j],array[i]

# Research on what they call tail recursion


# Recursive simple approach to quick sort
# think of base cases
# [] -> []
# [1] -> []
# then if we get a bigger array we just partition it into two subarrays that are [L] and [R]
# they are partioned using a pivot such that [L] + pivot + [R] we get sorted array
# partioning is just puting any element less than pivot in L and element greater than pivot in R
# once we are done we just determin the starting and end positions of these arrays and then call quicksot on them then combine the results
# 


def recursiveQuickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i <= pivot]
        greater=[j for j in array[1:] if j> pivot]
        return recursiveQuickSort(less)+[pivot]+recursiveQuickSort(greater)