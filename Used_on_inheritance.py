#an example for python private method and variable

class Base:
    
    class_instance = 0
    
    def  __init__(self):
        self.name = 'Gagan'
        self.__privateVariable = 'Private'
    
    def print_instance(self):
        print('self.name -{},self__privateVariable-{}'.format(self.name,self._Base__privateVariable))
    
    def setValues(self, name_instanace, private_instance):
        self.name = name_instance if name_instanace else self.name
        self.__privateVariable = private_instance if private_instance else self.__privateVariable
        
    def __privateMethod(self):
        self._Base__privateVariable = Base.class_instance
        print('')
        print('Base class_instance -{}'.format(Base.class_instance))
        
        
class Drived(Base):
    
    def __init__(self ,x):
        Base.__init__(self)
        self.derived_name = 'Chawla'
        self.lambdas = lambda x:x**2
        
    def print_instance(self):
        print('this belongs to the drived class')
        print('self.derived_name -{},self.lambda-{}'.format(self.derived_name,self.lambdas(3)))
        print('-------------------------------------')
        print('this belongs to Base class')
        print('self._Base__privateVariable)-{}'.format(self._Base__privateVariable))

        
    def set_values(self, name, private_variable, derived_name, lambdas):
        self.name = name
        self.derived_name = derived_name
        print(self.lambdas(lambdas))
        self._Base__privateVariable = private_variable
    
def main():
    bb = Base()
    dd = Drived(2)
    dd.print_instance()
    dd.print_instance()
    dd.set_values('Test','Derived_private_Value____','testing_derived_value',5)
    print(bb._Base__privateVariable)
    print(dd._Base__privateVariable)
    print(bb.name)
    print(dd.name)
    bb._Base__privateMethod()
    dd._Base__privateMethod()

if __name__ == "__main__":
    main()