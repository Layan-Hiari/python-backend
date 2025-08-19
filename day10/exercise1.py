class FibonacciIterator:
    def __init__(self, n):
        self.n = n       
        self.count = 0   
        self.a = 0        
        self.b = 1      

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration

        if self.count == 0:
            self.count += 1
            return self.a
        elif self.count == 1:
            self.count += 1
            return self.b
        else:
            fib = self.a + self.b
            self.a, self.b = self.b, fib
            self.count += 1
            return fib


fib_iter = FibonacciIterator(10)
for num in fib_iter:
    print(num)
