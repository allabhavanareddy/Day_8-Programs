def check_subset(nums,target):
    def backtrack(start,sum,subset):
        if sum==target:
            res.append(subset[:])
            return
        if sum>target or start==len(nums):
            return 
        #if backtrack(start+1,sum+l[start],subset):
        subset.append(nums[start])
        backtrack(start+1,sum+nums[start],subset)
        subset.pop()
        backtrack(start+1,sum,subset)
    res=[]
    backtrack(0,0,[])
    return res
nums=list(map(int,input().split()))
target=int(input())
result=check_subset(nums,target)
if result:
    print(*result)
else:
    print("no sbsets")