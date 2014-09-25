class Test(object):
    def __init__(self,x):
        self.x = x
    
    def f(self):
        print self.x
        


testowanie = Test('3')        
chamowa = testowanie.f()        
