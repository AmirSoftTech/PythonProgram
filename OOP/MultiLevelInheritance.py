#Multi Level Inheritance
class dada:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def da(self):
        d = self.w * self.h
        print("Property of dada:", d)

class baba(dada):
    def ba(self):
        b = 0.5 * self.w * self.h
        print("Property of baa:", b)

class nati(baba):
    def na(self):
        super().da()
        super().ba()
        n = 0.5 * 0.5 * self.w * self.h
        print("Property of dada:", n)

obj = nati(10, 10)
obj.na()