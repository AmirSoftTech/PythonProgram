#Method overloading example 1, method name is same output is different:
'''
class Math:
    def Product(self, x=None,y=None, z=None):

        if x!=None and y!=None and z!=None:
            sum = x+y+z
            print(sum)

        elif x != None and y != None:
            sum = x + y
            print(sum)

        elif x != None:
            sum = x
            print(sum)

obj = Math()
obj.product(10,10,10)
obj.product(10,10)
obj.product(10)
'''

#Method overloading example 2, method name is same output is different:
class Math:
    def Product(self, x=0, y=0, z=0):
            sum = x + y + z
            print(sum)
obj = Math()
obj.Product(10, 10, 10)
obj.Product(10, 10)
obj.Product(10)


