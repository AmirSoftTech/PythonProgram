class Phone:
    def __init__(self):
        print("I am in a Phone class")

class Samsung(Phone):
    def __init__(self):
        super().__init__()
        print("I am in a Samsung class")

s = Samsung()