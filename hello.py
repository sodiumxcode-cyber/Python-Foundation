#Leetcode 217 Contain Duplicates

#My Approach
def ContainDuplicate(nums):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else :
            freq[i] = 1
    
    for key in freq:
        if freq[key] > 1:
            return True
    
    return False


#Optimized Approach
def ContainsDuplicate(nums) :
    seen = set()
    for num in nums:
        if num in set:
            return True
        seen.add(num)
    return False