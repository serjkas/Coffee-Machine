class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        if self.c ** 2 == (self.a ** 2 + self.b ** 2):
            print(0.5 * (self.a * self.b))
        else:
            print("Not right")


a, b, c = input().split()
RightTriangle(int(a), int(b), int(c))
