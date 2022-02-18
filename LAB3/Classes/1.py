class Smth:
    def getstring(self):
        self.s = input()
        self.s = self.s.upper()
    
    def prints(self):
        print(self.s)

a = Smth()
a.getstring()
a.prints()
