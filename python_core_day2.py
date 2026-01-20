#Function to check if the string is Palindrome
def IsPalindrome(string):
    list_of_str = list(string)
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


#Function to Merge 2 Dictionaries
def MergeDict(dict1, dict2):
    result = {}
    for k, v in dict1.items():
        result[k] = v
    for k, v in dict2.items():
        result[k] = v
    return result


#Function to Flatten a nested List(any deapth)
def Flatten(list1):
    result = []

    for item in list1:
        try:
            result.extend(Flatten(item))
        except TypeError:
            result.append(item)
        
    return result


#Function to remove duplicates from a list while preserving the order
def RemoveDuplicates(list1):
    stack = list1[::-1]
    result = []

    while stack:
        item = stack.pop()

        try:
            for x in reversed(item):
                stack.append(x)
        
        except TypeError:
            result.append(item)
        
    return result