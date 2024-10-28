
# parent class
class Person(object):
    __Time=None
    _NoTImeToDie=None
# __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        
# child class
class Employee(Person):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
# invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
        Person._NoTImeToDie="Why"
        Person.__Time=10
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
        print("Salary : {}".format(self.salary) )
        print("No Time To DIe", Person._NoTImeToDie)
        
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
# calling a function of the class Person using
# its instance
a.display()
a.details()
a.__init__('Rahul', 886012, 200000, "Intern")
