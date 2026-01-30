#Function to remove duplicates from a sorted list
def RemoveDuplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k-1]:
            nums[k] = nums[i]
            k += 1
        else:
            nums[k] = 0
    return k, nums


#Function Reverse words in a sentence
def ReverseSentence(sen):
    words = sen.split()
    rev_list = words[::-1]
    rev_sen = " ".join(rev_list)
    return rev_sen


#Function to reverse words in a sentence(Pointer Approach)
def ReverseSen(sen):
    words = sen.split()
    left, right = 0, len(words) - 1

    while left < right:
        words[left] = words[right]
        words[right] = words[left]
        left += 1
        right -= 1
    return " ".join(words)


#Function to check if two strings are anagrams(Using Dictionary)
def Anagrams(s, t):
    if len(s) != len(t):
        return False
    
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] == 0:
            del freq[ch]

    return len(freq) == 0