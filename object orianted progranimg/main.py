#object oriented porgraming
#step 1-creating a class-a class is a blueprint of the object wewant to create,it includs properties and functions.
#step 2-creating object useing the class created in step 1

class Student():
    #creating properties
    self.name = ""
    self.age = 12
    self.grade = 7
    self.home_room_teacher = "mrs jones"

    #creating functions 
    #creating constructor function
    def __init__(self):
        print("this function is responsable for creating student objet")