# Python Class 2532
# Lesson 1 Problem 5
# Author: riatalwar (486154)

def remove_letter(string, letter):
    '''remove_letter(string,letter) -> str
    returns string with all occurrences of letter removed'''
    newString = ''
    for c in string:
        if c != letter:
            newString += c
    return newString

def test():
    '''Runs several test cases.'''
    print(remove_letter('a','a') == '')
    print(remove_letter('a','b') == 'a')
    print(remove_letter('','t') == '')
    print(remove_letter('This is a test','t') == 'This is a es')
    print(remove_letter('Hello World!','l') == 'Heo Word!')
    print(remove_letter('I like Python','q') == 'I like Python')

test()
