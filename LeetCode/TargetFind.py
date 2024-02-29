class Solution(object):
    def twoSum(self, nums, target):
        index = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in index:
                #if found then return the indices
                return [index[complement],i]
            index[num] = i
        return []

nums = []
n = int(input("Enter the number of elements: "))
for _ in range(n):
    nums.append(int(input("Enter a number: ")))
print(nums)
target = int(input("Enter target: "))

obj = Solution()
result = obj.twoSum(nums,target)
print(result)
