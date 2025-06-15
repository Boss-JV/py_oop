class Student:
    def __init__(self, Firstname, Lastname, age, courses, pocket_money):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.age = age
        self.courses = courses
        self.pocket_money = pocket_money
        
    def get_fullname(self):
        return f"{self.Firstname} {self.Lastname}"
            

    def display_info(self): # function ที่อยู่ใน class เรียกว่า method
        print("First Name:", self.Firstname)
        print("Last Name:", self.Lastname)
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print("Pocket money:",self.pocket_money)
        print("-" * 20)

# กำหนดค่า
student1 = Student("Alice","Borer", 20, ["Math", "English"],100)
student2 = Student("Bob","Mokes", 22, ["Physics", "History"],500)
# เรียกใช้ค่า
student1.display_info()
student2.display_info()

print(student1.get_fullname())