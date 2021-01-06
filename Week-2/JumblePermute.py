# Python Class 2532
# Lesson 2 Problem 4 (b)
# Author: riatalwar (486154)

def permute(inputWord):
    '''permute(inputList) -> list
    returns list of all permutations of inputList'''
    inputList = list(inputWord)
    # base case
    if len(inputList) == 0:
        return [[]]
    # recursive step
    permutations = []
    for i in range(len(inputList)):
        p = permute(inputList[:i] + (inputList[i + 1:])) # calls permute on a list with all but the ith element
        for j in p:
            permutations.append([inputList[i]] + j) # adds the ith element to each permutation in j so you have all the letters
    return permutations

def check_validity(inputWord):
    '''check_validity(inputWord) -> str
    returns valid word from permutations of inputWord'''
    # uses the file 'wordlist.txt' to create a list of valid words
    file = open('wordlist.txt')
    validWords = set()
    for word in file:
        validWords.add(word.strip())
    # goes through list of permutations and returns the first valid word
    permutations = permute(inputWord) # gets a list of the permutations
    for word in permutations:
        if ''.join(word).lower() in validWords:
            return ''.join(word)

def test():
    print(check_validity('CHWAT') == 'WATCH') # WATCH
    print(check_validity('RAROM') == 'ARMOR') # ARMOR
    print(check_validity('CEPLIN') == 'PENCIL') # PENCIL
    print(check_validity('YAFLIM') == 'FAMILY') # FAMILY
test()
