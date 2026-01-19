def Hehe(str) :
    list_of_str = str.split()
    freq = {}

    for i in list_of_str:
        if i in freq:
            freq[i] += 1

        else :
            freq[i] = 1

    for i, c in freq.items():
        print(i, ":", c)

    return -1
Hehe("mango apple orange apple mango")