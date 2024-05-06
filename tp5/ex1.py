from math import pow 

class Maclasse:
    def f1(self,x):
        return pow(x,2)+1

    def f2(self,x):

        if (x>0):
            return -x*x
        else:
            return 4*x
    def f3(self,x):
        return 2*self.f2(pow(x,2))
    
ins = Maclasse()
print(ins.f1(2))
print(ins.f2(ins.f2(3)))
print(ins.f2(ins.f3(1)))