import numpy as np
import random
import matplotlib.pyplot as plt
from math import sqrt

np.random.seed(12345)

class AffineTransform:

    """
    Class that creates Barnsley fractals
    """

    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.probability = [0.01, 0.85, 0.07, 0.07]
        self.used_function = 0
        self.x = 0
        self.y = 0
        self.array_new_x = []
        self.array_new_y = []

        """
        calculate the cumulative sum of probabilities
        """

        self.cumProb = np.cumsum(self.probability)
        self.cumProb = np.insert(self.cumProb, 0,0)

    def select_probab(self):
        r = np.random.random()
        for i in range(len(self.cumProb)):
            if self.cumProb[i] <= r <= self.cumProb[i+1]:
                self.used_function = i
                break

    def __call__(self, x, y):
        self.select_probab()
        x_new = self.a[self.used_function] * x + self.b[self.used_function] * y + self.e[self.used_function]
        y_new = self.c[self.used_function] * x + self.d[self.used_function] * y + self.f[self.used_function]
        self.x = x_new
        self.y = y_new
        self.array_new_x.append(x_new)
        self.array_new_y.append(y_new)
        return(self.x, self.y, self.cumProb)

    def iterating(self, N_points):
        for i in range(N_points):
            self.__call__(self.x, self.y)
        return(self.array_new_x, self.array_new_y)

    def gen_image(self):
        plt.scatter(self.array_new_x, self.array_new_y, color='green', s=0.1, marker='.')
        plt.axis('equal')
        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    a = [0, 0.85, 0.2, -0.15]
    b = [0, 0.04, -0.26, 0.28]
    c = [0, -0.04, 0.23, 0.26]
    d = [0.16, 0.85, 0.22, 0.24]
    e = [0, 0, 0, 0]
    f = [0, 1.6, 1.6, 0.44]

    s = AffineTransform(a,b,c,d,e,f)
    print(s(0,0))
    s.iterating(50000)
    s.gen_image()
