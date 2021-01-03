# Python Class 2532
# Lesson 1 Problem 6b
# Author: riatalwar (486154)

def find_7_letter_words():
    '''Makes a list with all the 7 letter words with no z's'''
    words = []
    file = open('wordlist.txt')
    for word in file:
        if len(word.strip()) == 7 and 'z' not in word:
            words.append(word.strip())
    return words

def find_highest_score(words):
    '''Finds the score for all the words and then finds the highest score'''
    values = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,
            'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,
            'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
    highest = (None, 0)
    for word in words:
        wordScore = 0
        for c in word:
            wordScore += values[c.upper()]
        if wordScore > highest[1]:
            highest = (word, wordScore)
    return highest

print(find_highest_score(find_7_letter_words()))

# answer = 'jukebox', 27
