#Hierarchical Inheritance
class dada:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def da(self):
        d = self.w * self.h
        print("Property of dada: ", d)

class baba:
    def ba(self):
        b = self.w * self.h
        print("Property of baba:", b)

class nati(dada,baba):
    def na(self):
        n = self.w * self.h
        print("Property of nati: ", n)

obj = nati(10, 10)
obj.da()
obj.ba()
obj.na()














