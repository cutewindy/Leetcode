def majorityElement(nums):
    element = {}
    for num in nums:
        if num not in element:
            element[num] = 0
        else:
            element[num] += 1
        if element[num] >= len(nums) / 2:
            return num
    
print majorityElement([1,2,2,2,2,4,2,2,2,2,2,7,77])