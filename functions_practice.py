#Check if a num is prime or not
def PrimeNums(num) :
    if num < 2:
        return False
    
    for i in range(2, num) :
        if num % i == 0:
            return False

    return True


#Reverse a String
def ReverseString(str) :
    if len(str) < 2:
        return str

    list_of_str = list(str)
    list_of_rev_str = []
    for i in range(len(list_of_str) - 1, -1, -1) :
        list_of_rev_str.append(list_of_str[i])

    return ''.join(list_of_rev_str)


#Count word frequency in a sentence
def WordFrequency(sentence) :
    words = sentence.split()
    freq = {}

    for w in words :
        if w in freq:
            freq[w] += 1
        else :
            freq[w] = 1
    
    return freq


#Return Second Largest Num in List
def SecondLargestNum(arr) :
    MAX_ITEM = 0
    for i in arr :
        if i > MAX_ITEM:
            sec_max = MAX_ITEM
            MAX_ITEM = i
        else :
            continue
    return sec_max