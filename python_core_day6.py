#Function to check if 2 strings are anagrams
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


#Function to find the first non-repeating character in a string
def NotRepeating(str):
    freq = {}
    for ch in str:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in str:
        if freq[ch] == 1:
            return ch
        

#Function to count character frequency and return it as a dictionary
def CharchterFreq(str):
    freq = {}
    for ch in str:
        freq[ch] = freq.get(ch, 0) + 1
    return freq