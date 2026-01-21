#Flattebn a nested list(using reccursion)
def FlattenList(list1):
    result = []
    for item in list1:
        if isinstance(item, list):
            result.extend(FlattenList(item))

        else:
            result.append(item)
    return result


#Flatten a nested list(using stack)
def FlattenList1(list2):
    result = []
    stack = list2[::-1]

    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])
        
        else:
            result.append(item)
    return result


#Removing Duplicates while preserving the order(using sets)
def RemoveDuplicates(nums):
    seen = set()
    result = []

    for x in nums:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


#Removing Duplicates while preserving the order(without using sets)
def RemoveDuplicates1(nums):
    result = []
    for x in nums:
        if x not in result:
            result.appedn(x)
    return result