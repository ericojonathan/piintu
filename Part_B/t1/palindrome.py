import math
import string

def palindrome(word):
	
    word = word.lower()
    words = []

    for w in word:
        if w != ' ':
            words.append(w)

    wLen = len(words)
    if wLen == 0:
        return False

    isEven = False
    
    #even
    if wLen % 2 == 0:
	    isEven = True
	
    center = 0
    if isEven:
	    center = int(wLen / 2)
    else:
        center = int(math.floor(wLen / 2 + 1))

    lIdx = wLen-1
    for i in range(0, center):
        word1 = words[i]
        word2 = words[lIdx-i]
        if word1 != word2:
            return False
        
    return True

def testPalindrome():
    words = [
		"Anna",
        "Civic",
        "Kayak",
        "Level",
        "Hello",
        "World",
        "A nna",
        " "
    ]
    for word in words:
        print(word,'\t:', palindrome(word))


testPalindrome()
