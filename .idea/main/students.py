class Students:
    def __init__(self , name , age , major , gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def is_eligible(self):
         if self.age>18 :
             return True
         else :
             return False

