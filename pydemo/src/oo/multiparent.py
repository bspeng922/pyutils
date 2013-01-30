'''
Created on 2013-1-24

@author: wang_peng
'''
class A:
    name = "I am A"
    
    def __init__(self):
        print "A"
    
    def show(self):
        print self.name
        
class B:
    name = "I am B"
    
    def __init__(self):
        print "B"
    
    def show(self):
        print self.name

class C(A,B):
#    def __init__(self):
#        A.__init__(self)
#        B.__init__(self)
#        print "C"
        
    def show(self):
        print "I am C"
        
if __name__ == "__main__":
    a = A()
    a.show()
    b = B()
    b.show()
    c = C()
    c.show()
    