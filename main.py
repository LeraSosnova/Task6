class Polynom:
    def init(self):
        self.data = {}  

    def processline(self, line):  
        try:
            v, c = map(int, line.split())  
            if v < 0 or v in self.data:
                raise ValueError  
            self.data[v] = c
        except ValueError:
            print("Skipping this line.")

    def readfile(self, filename):  
        self.data = {}
        with open(filename) as f:
            for line in f:
                self.processline(line.strip())

    def keyboard(self):  
        self.data = {}
        print("Line to stop")
        while True:
            line = input()
            if not line:
                break
            self.processline(line)

    def show(self):
        print(self.data)  

    def evaluate(self, x):
        result = 0
        for v, c in self.data.items():
            result += c * (x**v)  
        return result

    def resultc(self, v):  
        return self.data.get(v, 0.0)  

    def putc(self, coefs_dict):  
        if not isinstance(coefs_dict, dict):
            raise TypeError("Argument must be a file")
        self.data = coefs_dict.copy()

    def resultv(self):  
        return self.data.keys()

 
    def add(p1, p2):
        result = {}
        for v in set(p1.resultv() | p2.resultv()):
            result[v] = p1.resultc(v) + p2.resultc(v)
        return Polynom(result)  


    def subtract(p1, p2):
        result = {}
        for v in set(p1.resultv() | p2.resultv()):
            result[v] = p1.resultc(v) - p2.resultc(v)
        return Polynom(result)

    
    def multiply(p1, p2):
        result = {}
        for p1v in p1.resultv():
            for p2v in p2.resultv():
                newv = p1v + p2v
                newc = p1.resultc(p1v) * p2.resultc(p2v)
                result[newv] = result.get(newv, 0.0) + newc
        return Polynom(result)

P1 = Polynom()
P1.readfile('input01.txt')

P2 = Polynom()
P2.readfile('input02.txt')

Sum = Polynom.add(P1, P2)  
Pr = Polynom.multiply(P1, P2)  
Min = Polynom.subtract(P1, P2)  

Q = Polynom.add(Min, Pr)  
H = Polynom.multiply(P2, Polynom.multiply(Min, Min))  

print("Please enter a real number:")
while True:
    try:
        x = float(input())
        l = Q.evaluate(x)
        n = H.evaluate(x)
        print(l)
        print(n)

        with open("output.txt", "w") as f:
            print(l, file=f)
            print(n, file=f)
        break
    except ValueError:
