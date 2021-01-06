# Python Class 2532
# Lesson 2 Problem 5 (a)
# Author: riatalwar (486154)
def coin_count(c1, c2, c3, change):
    #if change == 0:
    #    return 0
    #if change < 0:
    #    return 100
    #count1 = coin_count(c1, c2, c3, change - c1) + 1
    #count2 = coin_count(c1, c2, c3, change - c2) + 1
    #count3 = coin_count(c1, c2, c3, change - c3) + 1
    #return min(count1, count2, count3)

    coinCount = [0]
    for c in range(1, change + 1):
        minCoins = change
        for coin in [c1, c2, c3]:
            if coin <= c:
                count = 1 + coinCount[c - coin]
                if count < minCoins:
                    minCoins = count
        coinCount.append(minCoins)
    return coinCount[-1]


def coin_average(c1, c2, c3):
    coinCount = [0]
    for change in range(100):
        count = coin_count(c1, c2, c3, change)
        coinCount.append(count)
    return sum(coinCount)/len(coinCount)

print(coin_average(1, 10, 25))

def test():
    print(coin_count(1, 10, 25, 0) == 0)
    print(coin_count(1, 10, 25, 0))
    print(coin_count(1, 10, 25, 1) == 1)
    print(coin_count(1, 10, 25, 1))
    print(coin_count(1, 10, 25, 10) == 1)
    print(coin_count(1, 10, 25, 10))
    print(coin_count(1, 10, 25, 25) == 1)
    print(coin_count(1, 10, 25, 25))
    print(coin_count(1, 10, 25, 50) == 2)
    print(coin_count(1, 10, 25, 50))
    print(coin_count(1, 10, 25, 31) == 4)
    print(coin_count(1, 10, 25, 31))
test()
