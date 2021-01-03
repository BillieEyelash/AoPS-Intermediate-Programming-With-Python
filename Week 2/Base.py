# Python Class 2532
# Lesson 2 Problem 2
# Author: riatalwar (486154)

def get_base_number(num, base):
    '''get_base_number(num, base) -> int
    returns value of num as a base number in the given base'''
    if len(num) == 0:
        return 0
    return get_base_number(num[:-1], base) * base + int(num[-1])

# test cases
def test():
    print(get_base_number('', 2) == 0)
    print(get_base_number('1', 2) == 1)
    print(get_base_number('2', 10) == 2)
    print(get_base_number('10011', 2) == 19)
    print(get_base_number('3202', 5) == 427)
    print(get_base_number('611023',  7) == 103603)

test()
