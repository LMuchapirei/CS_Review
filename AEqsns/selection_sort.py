"""
Given an array of numbers give us back a sorted list using the selection sort algorithm
"""




from cgitb import small


def selectionSort(array):
    for i in range(len(array)):
        smallest=array[i] 
        for j in range(i+1,len(array)):
            if smallest > array[j]:
                tmp=array[j]
                array[j]=smallest
                array[i]=tmp
                smallest=tmp
    return array

print(selectionSort([8,5,2,9,5,6,3]))
  



def selectionSort1(array):
    currentIdx=0

    while currentIdx <len(array)-1:
        smallestIdx=currentIdx
        for i in range(currentIdx+1,len(array)):
            # find the index with the smallest index
            if array[smallestIdx] > array[i]:
                smallestIdx=i # update the smallest index
        swap(currentIdx,smallestIdx,array)
        currentIdx+=1
    return array


def swap(i,j,array):
    array[i],array[j]=array[j],array[i]



print(selectionSort1([8,5,2,9,5,6,3]))