#implementing the private methods and single under_score is used for the private variable


class Base:

    def __init__(self):
        self._a = 'Gagan'
        self.__c = 'Private'
        print('self.__c -{}'.format(self.__c))

    def setvalues(self, *args):
        self._a, self.__c = args

    def getvalue(self):
        return self._a, self.__c


class Drive(Base):

    def __init__(self):
        Base.__init__(self)
        self.test = 'Testing'
        self._drive_a = 'proto'
        #this cause the error because it private variable of Base class
        try:
            print('self.__c -{}'.format(self.__c))
        except:
            print("except block can'nt accces the base private elements")
        #this will print because it Protected
        print('Printing the base class protocated methods')
        print('self._a -{}'.format(self._a))

    def setvalue(self, *args):
        self.test, self._drive_a = args
        self._a = 'override with drive class'

    def getvalue(self):
        return self.test, self._drive_a, isinstance(self._a, Base), self._a


def main():
    obj = Base()
    obj.setvalues('pro', 'pri')
    print(obj.getvalue())
    try:
        print('printing the protocated method')
        print(obj.a)
    except:
        print("protocated can'nt be called outside of class")
    try:
        print('printing the private method')
        print(obj.c)
    except:
        print("private can'nt be called outside of class")
    
    print('-------Drive-----------')
    drive = Drive()
    drive.setvalue('test', 'drive proto')
    print(drive.getvalue())

if __name__ == "__main__":
    main()
