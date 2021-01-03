def caesar_shift(string, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    shiftedString = ''
    for c in string:
        index = (alphabet.index(c) + shift) % 26
        shiftedString += alphabet[index]
    return shiftedString

def run():
    string = input('Enter a word. ')
    shift = int(input('Enter the number of letter you want to shift by. '))
    print(caesar_shift(string, shift))

def test():
    print(caesar_shift('example', 1) == 'fybnqmf')
    print(caesar_shift('example', -1) == 'dwzlokd')
    print(caesar_shift('python', 2) == 'ravjqp')
    print(caesar_shift('pecan', 4) == 'tiger')

test()
