

import re


def twoSumHashing(num_arr, pair_sum):
    sums = []
    hashTable = {}
    items=[]
    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
            print("Pair with sum", pair_sum,"is: (", num_arr[i],",",complement,")")
            items.append([num_arr[i],complement])
        hashTable[num_arr[i]] = num_arr[i]
    return items

# Driver Code
num_arr = [4, 5, 1, 8]
pair_sum = 9    
  
# Calling function
# print(twoSumHashing(num_arr, pair_sum))

def threeSum(nums):
    result=[]
    for index in range(len(nums)):
        target=0-nums[index]
        res=twoSumHashing(nums[index+1:],target)
        if len(res) >0:
            i,j=res


            res=[]
        # for index in range(len(nums)):   
        #     b=0-nums[index]
        #     # perform two sum on b on the remainder of j,k  
        #     numsMap={}
        #     twoSums=[]
        #     for index1 in range(index+1,len(nums)):              
        #         complement=b-nums[index1]
        #         if complement in numsMap:
        #             twoSums.append([complement,nums[index1]])
        #         numsMap[nums[index1]]=complement
        #     for val in twoSums:
        #         j,k=val
        #         res.append([nums[index],j,k])
        # return res


print(threeSum([-1,0,1,2,-1,-4]))