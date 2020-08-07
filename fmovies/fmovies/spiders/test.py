

global variable 
variable = 10
def test():
    # global variable
    print('my variable is ',variable)

def test2():
    print('variable is',variable)

test()
test2()

print('my variable is ',variable)


class Myclass():

    classvar=0

    # model =load()
    def load():
        model =''
    def __init__(self):
        self.var1=0
    
    def myprint(self):
        print('my var is ',self.var1)
    
    def myprint2():
        print('class var is ',Myclass.classvar)

    def detection(self):
        pass