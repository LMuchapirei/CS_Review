This folder contains data structures covered by William Fiset link to video https://www.youtube.com/watch?v=RBSGKlAvoiM
The github repository is https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbWQ0ajE0UGtfOUVpUXk5cTJlOG1Ed3ZDUzNEd3xBQ3Jtc0tseC1QSk5fRUFIc3NWaG5iZENGaF9MbXBpb1h3QzM2ZXdtUFZIWlA4WTB0OU02NXYyRzZIVDFiTkRrYWlIOG1WcFpQV0hMN2xOOUFrbGs4bjRJd2xmWXdBUjRKM3g1R0VHem80cmhYXzNrby1lRjRpOA&q=https%3A%2F%2Fgithub.com%2Fwilliamfiset%2Fdata-structures


What is a data structure?

A data structure DS is a way of organizing data so that it can be used effectively

Why do we need to learn them or why?
-They are essential ingredients in creating fast and powerful algorithms.
-They help to manage and organize data.
-They make code cleaner and easier to understand. 

Abstract Data Types vs Data Structures

Abstract data type ADT is an abstraction of a data structure which provides only the interface to which a data structure must adhere to

(interface contract specifying what ops/values can be exposed by a type satisfying the contract my def)
The interface does not give any specific details about how something should be implemented or in what programming language

Abstraction (ADT)    Implementation (DS)
List                          Dynamic Array Linked List
Queue                Linked List,Array,Stack based Queue implementaion
Map   Tree Map/Hash Map/Hash Table

Vehicle  Golf Cart, bicycle,smart car

List -->Dynamic Array,Linked List both of these offer what we want about a list but the difference is in the actual implementation
add,remove,iterate (List ADT)so on..how we archieve  this (DS)

Computational Complexity Analysis

How much time does this algorithm need to finish?
How much space does this algorithm need for computation?

We can use a standard way that generalizes the time/space that an algorithm uses when it runs

Big-O Notation
This gives an upper bound of the complexity in the worst case,helping to quantify performance as the input size becomes arbitrarily large
Given the largest possible input set how does the alogorithm performs generally
This generalisation gives us insight as how the algorithm will perfom in any case

Given n-The size of the input Complexities ordered in from the smallest to largest

Constant Time: O(1)
Logarithmic Time : O(log(n))
Linear Time: O(n)
Linearithmic Time: O(nlog(n))
Quadric Time: O(n^2)
Cubic Time:O(n^3)
Exponential Time:O(b^n), b>1
Factorial Time :O(n!)

Properties of Big-O
O(n+c)=O(n)
O(cn)=O(n),  c>0

Let f be a function that describes the running time of a particular algorithm for an input of size n
f(n)=7log(n)^3+15n^2+2n^3+8

look at the biggest term
O(f(n))=O(n^3)

Examples of Big-O
The following run in constant time :O(1)
with respect to the input
a:=1                   i:=0
b:=2                   while i < 11 do
c:=a+5*b             i=i+1

The following run in linear time :O(n)

i:=0                                   i:=0
while i<n Do                     while i<n Do
     i=i+1                                   i=i+3

f(n)=n                               f(n)=n/3
O(f(n))=O(n)                     O(f(n))=O(n)

why n/3 in the second we are going to loop 3 times faster since we are incrementing by three in the loop
we do the constant work how man time  well n times therefore thats O(n) for either of the two

Both of the following run in quadratic time
The first may be obvious since n work done n times is n*n=O(n^2)

for(i:=0;i<n;i=i+1)
    for(j:=0;j<n;j=j+1)
   f(n)=n*n=n^2, O(f(n))=O(n^2)

for(i:=0;i<n;i=i+1)
    for(j:=1;j<n;j=j+1)

what l think is n times doing n-1 work each time leads n*n-n--->generalizes to n^2

i goes from [0,n) the amount of looping done is directly determined by what i is.
Remark that if i=0,we do n work ,if i=1 we do n-1 work,if i=2 we do n-2 work

the sum of this is n+(n-1)+(n-2)...+3+2+1?
this turns out to be n(n+1)/2 
O(n(n+1)/2)=-->O(n^2) 

Suppose we have a sorted array and we want to find the index of a particular value in the array,if it exists.What is the time complexity of the following algorithm?

low:=0
high:=n-1
while low<=high Do
       mid:=(low+high)/2
       if array[mid]==value: return mid
       Elese If array[mid]<value:lo=mid+1
       Else If array[mid] >value:hi=mid-1
 return -1

O(log(n)) 

i:=0
while i<n Do
      j=0
      while j<3*n Do
             j=j+1
      j=0
      while j <2*n Do
             j=j+1
      i=i+1
f(n)=n*(3n+2n)=5n^2
O(f(n))=O(n^2)

Multiply the loops on different levels and then add those that are on the same level

i:=0
While i<3*n Do
     j:=10
     while j<=50 Do
            j=j+1
      j=0
     While j<n*n*n Do
            j=j+2
      i=i+1

f(n)=3n*(40+n*3/2)=3n/40+3n^4/2
O(f(n))=)(n^4)
Some Big O Examples

Finding all subsets of a set -O(2^n)
Finding all permutations of a string-O(n!)
Sorting using mergesort-O(nlog(n))
Iterating over all the cells in a matrix of size n by m -O(nm)

Research more on this okay

Static and Dynamic Arrays

Outline
What is an Array?
When and where is a Array used?
Complexity
Static array usage example
Dynamic Array Implementation details 
Code Implementation


What is a static Array?
A static array is a fixed length container containing n elements indexable from the range [0,n-1]
Indexable means that each slot/index in the array can be referenced with a number
Contigous chunk of memory ,adjacent addresses

When we need to use them
1.)Storing and accessing sequential data
2.)Temporarily storing objects
3.)Used by IO routines as buffers
4.)Lookup tables and inverse lookup tables
5)Can be used to return multiple values from a function
6)Used in dynamic programming to cache answers to subproblems

Complexity
                 Static          Dynamic Array
Access       O(1)          O(1)
Search       O(n)          O(n)
Insertion     N/A        O(n)
Appending  N/A        O(1)
Deletion      N/A        O(n)


 Insertion linear in the case of a dynamic array cause we may need to traverse to the end of the array to insert an element,
copy over process etc
Search both linear..the item may be at the end of the array
Appending O(1) dynamic array...we have a handle of the last inserted element,resizing 
Deletion O(n) delete,shift over the elements and copy over

Elements are referenced by their index,and there is no other way to access elements in an array.Array indexing is zero-based,meaning the first element is found in position zero.

Dynamic Array

Implementing a dynamic array...we use a static array!

1.Create a static array with an initial capacity
2.Add elements to the underlying static array,keeping track of the number of elements
3.If adding another elements will exceed the capacity,then create a new static array with twice the capacity and copy the original elements into it.


Dynamic array implementation

done in ArrayDynamic.java file

done part 1 and 2 halfway LinkedLists

done impl
now at stack
@58:0

