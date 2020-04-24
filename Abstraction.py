'''
The purpose of doing the abstraction that suppose you are working on any application you required that every drive conatains
the same methods all the base methods on that condition you will use the abstraction where you will just declare the
methods and not given defination of that methods.

One Most Imp thing to make we can't make the abstract class object.

#drive class must contain all the methods on the base abstract class
'''

from abc import ABC, abstractmethod

class Base(ABC):
    #for make any class as method the abstract method we will use the abstractmethod decorators.
    
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def lastname(self):
        pass
    
    @abstractmethod
    def place(self):
        pass

class Drive_1(Base):
    
    def __init__(self,work, name, lastname, place):
        self.work = work
        self.name = name
        self.lastname = lastname
        self.place = place
    
    def work(self):
        print(f'I am -{self.work}')
    
    def name(self):
        print(f' my name is {self.name}')
        
    def lastname(self):
        print(f'my surname is {self.surname}')
    
    def place(self):
        print(f'my current place -{current_place}')
        
class Drive_2(Base):
    
    def __init__(self,work, name, lastname, place):
        self.work = work
        self.name = name
        self.lastname = lastname
        self.place = place
    
    def work(self):
        print(f'I am -{self.work}')
    
    def name(self):
        print(f' my name is {self.name}')
        
    def lastname(self):
        print(f'my surname is {self.surname}')
    
    def place(self):
        print(f'my current place -{current_place}')
    
class Drive_3(Base):
    
    def __init__(self,work, name, lastname, place):
        self.work = work
        self.name = name
        self.lastname = lastname
        self.place = place
    
    def work(self):
        print(f'I am -{self.work}')
    
    def name(self):
        print(f' my name is {self.name}')
        
    def lastname(self):
        print(f'my surname is {self.surname}')
    
    def place(self):
        print(f'my current place -{current_place}')


def main():
    dd_1 = Drive_1('Develpoer', 'Gagandeep', 'Chawla', 'indore')
    dd_2 = Drive_1('Teacher', 'Ajay',    'Joshi', 'indore')
    dd_3 = Drive_1('Dealer', 'Lalit', 'vishskarma', 'indore')
    for count,obj in enumerate([dd_1,dd_2,dd_3]):
        print(count+1, obj.work, obj.name, obj.lastname, obj.place)

if __name__ == "__main__":
    main()