
# Better way to design class is using Oops concept
# Encapsulation  (Data hiding)

class BankAccount:

    # constructor
    def __init__(self,account,balance):
        self._account_number = account
        self._balance = balance

    def deposit(self,amount):
        self._balance = self._balance + amount

    def withdrawl(self,amount):
        if(self.balance > amount):
            self._balance = self._balance - amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self._balance
    
amol = BankAccount(123,1000)
print(amol.get_balance())
    
# Abstraction (Hiding implementation details)

from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print('car starting ........')
    def start():
        print("start .....")
    def stop():
        print("stop .....")
    
a = Car()
a.start_engine()
a.start()
a.stop()







# Inheritance(Reusability)
# single inheritance
# multiple inheritance 
# mullti level
# herarchical 
class Student:
    def __init__(self,fn,ln,age):
        self.firstName = fn 
        self.lastName = ln 
        self.age = age 

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self, fn, ln, age,salary):
        super().__init__(fn, ln, age)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

amit = Teacher("amol","rao",23,44000)
print(amit.firstName)
print(amit.lastName)
print(amit.age)
print(amit.salary)
amit.displayName()
amit.displaySalary()

# amit = Student("amit","chitke",23)
# amit.displayName()
        

# Polymorphism(Multiple forms)
# overloading 
# overriding 
# Duck typing 
# Operator 

class Bird:
    def fly(self):
        print("some birds can fly")

class Sparrow(Bird):
    def fly(self):
        print('sparrow can fly to medium heights')

class Ortrisch(Bird):
    def fly(self):
        print('Ortrisch cannot fly')

sp1 = Sparrow()
oc1 = Ortrisch()
sp1.fly()
oc1.fly()


# Duck typing
class Human:
    def talk(self):
        print("hello hi")
class Dog:
    def talk(self):
        print("bow bow ")

def Call_talk(obj):
    obj.talk()

a = Human()
b = Dog()
Call_talk(a)
Call_talk(b)




