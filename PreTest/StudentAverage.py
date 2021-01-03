def get_scores(fileName):
    file = open(fileName)
    scores = {}
    for line in file:
        splitLine = line.split()
        scores[splitLine[0]] = scores.get(splitLine[0], []).append(int(splitLine[1]))
    return scores

def find_average(scores, name):
    average = sum(scores[name]) / len(scores[name])
    return 'The average for', name, 'is', average

def run():
    scores = get_scores('studentdata.txt')
    name = input('Enter name: ')
    while name in scores:
        print(find_average(scores, name))
        name = input('Enter name: ')
    print('Goodbye!')

def test_get_scores():
    print(get_scores('avgtest1.txt') == {'Arnold':[90]})
    print(get_scores('avgtest2.txt') == {'Arnold':[90], 'Brown':[84]})
    print(get_scores('avgtest3.txt') == {'Arnold':[90, 80]})
    print(get_scores('studentdata.txt') == {'Arnold':[90, 80], 'Brown':[84], 'Cocher':[77, 100]})

def test_find_average():
    print(find_average({'Arnold':[90]}, 'Arnold') == )
    print(find_average({'Arnold':[90], 'Brown':[84]}, 'Brown') == )
    print(find_average({'Arnold':[90, 80]}, 'Arnold') == )
    print(find_average({'Arnold':[90, 80], 'Brown':[84], 'Cocher':[77, 100]}, 'Cocher') == )

def test():
    test_get_scores()
    test_find_average()

test()
