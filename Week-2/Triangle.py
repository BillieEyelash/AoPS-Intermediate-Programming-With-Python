def tri(n):
    triangle = [0]
    for i in range(1, n + 1):
        triangle.append(triangle[-1] + i)
    return triangle[n]

def test():
    print(tri(0) == 0)
    print(tri(1) == 1)
    print(tri(2) == 3)
    print(tri(3) == 6)
test()
