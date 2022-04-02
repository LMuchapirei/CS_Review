

def swap(i,j,array):
    array[i],array[j]=array[j],array[i]
def bubbleSort(array):
    
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                swap(i,j,array)
    return array


print(bubbleSort([8,5,2,9,5,6,3]))




def bubbleSort1(array):
    isSorted=False

    while not isSorted:
        isSorted=True
        counter=0
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                swap(i,i+1,array)
                isSorted=False
        counter+=1
    return array