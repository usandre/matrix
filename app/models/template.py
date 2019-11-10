# -*- coding: utf-8 -*-
from random import randint

class template():

    def __init__(self, var1, var2):
        self.var1 = float(var1)
        self.var2 = float(var2)

        self.range = abs(float(var2) - float(var1))
        self.limit_min = 0.36666
        self.limit_max = 3.6


        self.fibo =[1.618, 1.5,
               1.382, 1.236, 1.145, 1,
               0.855, 0.764, 0.618, 0.5,
               0.382, 0.236, 0.145, 0,
               -0.145, -0.236, -0.382, -0.5, -0.618]
        self.price_levels = []
        self.open_points = []

        self.matrix = []

    def generate_price_levels(self):
        for number in self.fibo:
            level = round(number * self.range + self.var1, 4)
            self.price_levels.append(level)
        return self.price_levels


    def generate_position_points(self):
        lim = len(self.price_levels) - 1
        for idx in range(0, lim):
                thiselem = self.price_levels[idx]
                nextelem = self.price_levels[idx + 1]
                pos1 = round((thiselem - nextelem) * 0.764 + nextelem, 5)
                pos2 = round((thiselem - nextelem) * 0.236 + nextelem, 5)

                self.open_points.append(pos1)
                self.open_points.append(pos2)

                self.matrix.append(self.construct_line(pos1,thiselem,self.limit_min, 'BUY'))
                self.matrix.append(self.construct_line(pos1,self.limit_max,pos2, 'SELL'))
                self.matrix.append(self.construct_line(pos2,pos1,self.limit_min, 'BUY'))
                self.matrix.append(self.construct_line(pos2,self.limit_max,nextelem, 'SELL'))


        return self.open_points

    def construct_line(self, pos, tp, sl, type):
        return ','.join([str(pos), str(tp), str(sl), str(type)])

    def printMatrix(self, m):
        a = ""
        for line in m:
            print(m[line])
            # a = a + ",".join(m[line]) + "\n"
        return a


    def generate(self):
        matrix = self.generateLevel()
        return matrix
        m= ''
        for line in matrix:
            m += line + "\n "
        return m

    def generateLevel(self):
        self.generate_price_levels()
        self.generate_position_points()
        return self.matrix


t = template('1.1','1.2')
# print(t.generateLevel())
print(t.generate())
