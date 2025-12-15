##leetcode question - 1437
def kLengthApart(k,nums):
    prev = -1
    for i in range(0,len(nums)):
        if(nums[i]==1):
            if(prev!=-1 and i-prev-1<k):
                return False
            prev = i
    return True
nums = [1,0,0,0,1,0,0,1]
if(kLengthApart(3,nums)):
    print("Yes they are apart")
else:
    print("No they are not")