def longest_word(string):
    value = {}
    for i in string.split():
            value[len(i)] = i

    return value[max(value.keys())] 

"""def freq_char(string):
    words = {}
    for i in string:
        words[string.count(i)] = i
    #print(words[max(words.keys())])
    print(word)
    print()"""

def freq_char(string):
    count = dict()
    words = string
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    print(count)
    print()

def palindrom(string):
    ns = string[::-1]
    if ns == string:
        print("given string is palindrome")
    else:
        print("given string is not a palindrome")
    print()

def substr(string):
    k = input("enter the sub string to find its index : ")
    if k in string:
        print("the index of sub string is : ", string.find(k))
    else:
        print("you entered wrong substring")
    print()

def word_count(string):
    count = dict()
    words = string.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
    
k = input("enter a string : ")
print()

word = longest_word(k)
print("word with maximum length is : ",word)
print()

#displaying character with frequencies
freq_char(k)

#checking if the string is palindrome or not
palindrom(k)

#checking the index of the substring in string
substr(k)

#checking the occurance of each word in the string
print("occurance of each word in the string is : ",end="")
print(word_count(k))





