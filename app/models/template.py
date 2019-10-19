# -*- coding: utf-8 -*-
from random import randint

class template():

    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def printMatrix(self, m):
        a = ""
        for line in m:
            print(m[line])
            # a = a + ",".join(m[line]) + "\n"
        return a


    def generate(self):
        m={}
        for i in range(10):
            m[str(i)] =  self.generateLevel()
        return m

    def generateLevel(self):
        level=[]
        for i in [1,2,3]:
            level.append(str(randint(1, 100)))
        if (randint(1,6) > 3):
            level.append("SELL")
        else:
            level.append("BUY")
        return ','.join(level)


t = template(1,2)
print(t.generate())