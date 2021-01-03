# Python Class 2532
# Lesson 1 Problem 6a
# Author: riatalwar (486154)

file = open('wordlist.txt')
def count_10_letter_words():
    count = 0
    for word in file:
        if len(word.strip()) == 10:
            count += 1
    return count

print(count_10_letter_words())
