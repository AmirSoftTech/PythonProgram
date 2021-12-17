class Phone:
    def call(self):
        print("Call function from Phone class")

    def sms(self):
        print("sms function from Phone class")

    def photo(self):
        print("Photo function from Phone class")

class Samsung(Phone):
    def photo(self):
        super().photo()
        print("Photo function from samsung class")
obj = Samsung()
obj.photo()
obj.call()





