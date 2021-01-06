# Python Class 2532
# Lesson 1 Problem 7
# Author: riatalwar (486154)

def encipher_fence(plaintext, numRails):
    '''encipher_fence(plaintext,numRails) -> str
    encodes plaintext using the railfence cipher
    numRails is the number of rails'''
    rails = ''
    for i in range(numRails):
        start = numRails - (i + 1)             # creates the start of the rail
        rails += plaintext[start::numRails]    # adds the rail to rails
    return rails

def decipher_fence(ciphertext, numRails):
    '''decipher_fence(ciphertext,numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''
    plaintext = [''] * len(ciphertext)          # list of empty strings -- one for c in ciphertext

    railStart = 0                               # tracks the start of the rails
    for i in range(numRails):
        plaintextIndex = numRails - (i + 1)     # sets index of first character in rail
        count = 0                               # keeps track of the # of letters in a rail
        for c in ciphertext[railStart:]:
            if plaintextIndex >= len(plaintext):
                railStart += count
                break
            plaintext[plaintextIndex] = c       # puts c into its correct index
            plaintextIndex += numRails
            count += 1

    return ''.join(plaintext)

def count_real_words(deciphered, words):
    '''Count the number of real words in deciphered'''
    count = 0                                                          # tracks # of real words
    for word in deciphered.strip('.,;:"?!@#$%^&*/-_').lower().split(): # strips decipher of punctuation and makes it a list of words
        if word in words:                                              # checks if each word is in the list of valid words
            count += 1
    return count

def decode_text(ciphertext, wordfilename):
    '''decode_text(ciphertext,wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words'''
    # uses wordlist.txt to create a list of valid words
    file = open(wordfilename)
    words = []
    for line in file:
        words.append(line.strip())

    # deciphers ciphertext with 1 through 10 rails
    mostRealWords = (None, 0)                   # keeps track of the best deciphered text and its realWordCount 
    for i in range(10):
        deciphered = decipher_fence(ciphertext, i + 1)
        realWordCount = count_real_words(deciphered, words)
        if realWordCount > mostRealWords[1]:    # checks if the number of real words is > the current greatest
            mostRealWords = deciphered, realWordCount

    return mostRealWords[0]

def encipher_fence_test():
    '''Tests the encipher_fence function'''
    print(encipher_fence('', 1) == '')
    print(encipher_fence('a', 1) == 'a')
    print(encipher_fence('a', 2) == 'a')
    print(encipher_fence('ab', 1) == 'ab')
    print(encipher_fence('ab', 2) == 'ba')
    print(encipher_fence('ab', 3) == 'ba')
    print(encipher_fence('abc', 2) == 'bac')
    print(encipher_fence("abcdefghi", 3) == 'cfibehadg')
    print(encipher_fence("This is a test.", 2) == 'hsi  etTi sats.')
    print(encipher_fence("This is a test.", 3) == 'iiae.h  ttTss s')
    print(encipher_fence("Happy birthday to you!", 4) == 'pidtopbh ya ty !Hyraou')

def decipher_fence_test():
    '''Tests the decipher_fence function'''
    print(encipher_fence('', 1) == '')
    print(encipher_fence('a', 1) == 'a')
    print(encipher_fence('a', 2) == 'a')
    print(encipher_fence('ab', 1) == 'ab')
    print(encipher_fence('ba', 2) == 'ab')
    print(encipher_fence('ba', 3) == 'ab')
    print(encipher_fence('bac', 2) == 'abc')
    print(decipher_fence("hsi  etTi sats.",2) == 'This is a test.')
    print(decipher_fence("iiae.h  ttTss s",3) == 'This is a test.')
    print(decipher_fence("pidtopbh ya ty !Hyraou",4) == 'Happy birthday to you!')

def decode_text_test():
    '''Tests the decode_text function'''
    print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt') ==
        'the quick brown fox jumps over the lazy dog')
    print(decode_text("unt S.frynPs aPiosse  Aa'lgn lt noncIniha ", 'wordlist.txt') ==
        "It's fun learning Python in an AoPS class.")
    print(decode_text('hsi  etTi sats.', 'wordlist.txt') == 'This is a test.')
    print(decode_text('iiae.h  ttTss s', 'wordlist.txt') == 'This is a test.')
    print(decode_text('pidtopbh ya ty !Hyraou', 'wordlist.txt') == 'Happy birthday to you!')

def test():
    '''Runs all test code'''
    encipher_fence_test()
    print()
    decipher_fence_test()
    print()
    decode_text_test()

test()
