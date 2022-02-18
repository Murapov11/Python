class FilterPrime:
    def filter(self,a):
        self.arr = list(filter(lambda x: x % 2 != 0, a))
        return self.arr
f = FilterPrime()
print(f.filter([1,2,3,4,5,6,7,8,9,10,11,12]))
