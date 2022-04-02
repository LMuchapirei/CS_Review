





def insertionSort(array):

    for i in range(len(array)):
        for j in range(0 ,i+1):
            if array[i] < array[j]:
                swap(i,j,array)
    return array
def swap(i,j,array):
    array[i],array[j]=array[j],array[i]


print(insertionSort([8,5,2,9,5,6,3]))



def inserstionSort1(array):
    for i in range(1,len(array)):
        j=i
        while j > 0 and array[j] < array[j-1]:
            swap(j,j-1,array)
            j-=1
    return array

print(inserstionSort1([8,5,2,9,5,6,3]))
