# Python Class 2532
# Lesson 2 Problem 5 (b)
# Author: riatalwar (486154)

def coin_count(c1, c2, c3, change):
    coinCount = [0]
    for c in range(1, change + 1):
        minCoins = change
        for coin in (c1, c2, c3):
            if coin <= c:
                count = 1 + coinCount[c - coin]
                if count < minCoins:
                    minCoins = count
        coinCount.append(minCoins)
    return coinCount[-1]

def coin_average(c1, c2, c3):
    coinCount = [0]
    minCoins = 0
    for change in range(100):
        for c in range(1, change + 1):
            minCoins = change
            for coin in (c1, c2, c3):
                if coin <= c:
                    count = 1 + coinCount[c - coin]
                    if count < minCoins:
                        minCoins = count
        coinCount.append(minCoins)
    return sum(coinCount)/len(coinCount)

def best_coins():
    minAvg = 100
    for i in range(2, 51):
        for j in range(2, 51):
            avg = coin_average(i, j, 1)
            if avg < minAvg:
                minAvg = avg
                bestCoins = i, j, 1
    return bestCoins
print(coin_average(12, 19, 1))
#print(best_coins())
# Write a Python program to design better coinage:
#    you're allowed 3 different coin values, and your goal is to minimize the average number of coins given as change
#    (assuming that any value from 0 to 99 cents as change is equally likely).
#    What 3 coin values give the smallest average number of coins?
