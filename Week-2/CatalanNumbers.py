# Python Class 2532
# Lesson 2 Problem 3
# Author: riatalwar (486154)
def find_next_catalan(n, catalanList):
        total = 0
        first = 0
        last = n
        for j in range(n + 1):
            total += catalanList[first] * catalanList[last]
            first += 1
            last -= 1
        return total

def catalan(n):
    '''Compute the nth catalan number'''
    catalanList = [1]
    for i in range(n):
        catalanList.append(find_next_catalan(i, catalanList))
    return catalanList[n]

def test():
    print(catalan(1) == 1)
    print(catalan(1))
    print(catalan(2) == 2)
    print(catalan(2))
    print(catalan(3) == 5)
    print(catalan(3))
    print(catalan(4) == 14)
    print(catalan(4))

print(catalan(30))
test()
