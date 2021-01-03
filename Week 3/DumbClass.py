class Dumbclass:

    def __init__(self, x):
        self.y = x
        self.z = 2

    def __str__(self):
        return str(self.y)+str(self.z)

    def foo(self, y):
        self.y += y
        self.z = y*self.y

    def garble(self, other):
        self.z = other.y

a = Dumbclass(2) # a.y = 2, a.z = 2
b = Dumbclass(3) # b.y = 3, b.z = 2
a.foo(9)         # a.y = 11, a.z = 99
print(a)         # 1199
b.garble(a)      # b.y = 3, b.z = 11
print(b)         # 311
b.foo(4)         # b.y = 7, b.z = 28
print(b)         # 728

# will print: 1199, 311, 728
