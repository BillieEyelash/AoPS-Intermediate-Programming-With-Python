# Python Class 2532
# Lesson 2 Problem 4 (a)
# Author: riatalwar (486154)

def permute(inputList):
    '''permute(inputList) -> list
    returns list of all permutations of inputList'''
    if len(inputList) == 0:
        return [[]]

    permutations = []
    for i in range(len(inputList)):
        p = permute(inputList[:i] + (inputList[i + 1:]))
        for j in p:
            permutations.append([inputList[i]] + j)
    return permutations

# test cases
def test():
    print(permute([]) == [[]])
    print(permute([1]) == [[1]])
    print(permute([1, 2]) == [[1, 2], [2, 1]])
    print(permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

test()
