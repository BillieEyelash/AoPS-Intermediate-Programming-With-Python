def move(start, mid, goal):
    goal.append(start.pop())
    print(start, mid, goal)

def hanoi(n, start, mid, goal):
    if n == 1:
        move(start, mid, goal)
        return

    hanoi(n - 1, start, goal, mid)
    move(start, mid, goal)
    hanoi(n - 1, mid, start, goal)

#hanoi(1, [1], [], [])
#hanoi(2, [2, 1], [], [])
#hanoi(3, [3, 2, 1], [], [])
hanoi(8, [8, 7, 6, 5, 4, 3, 2, 1], [], [])
