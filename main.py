class Student:
    # Class Variable
    student_count = 0
    
    def __init__(self, Firstname, Lastname, age, courses, salary):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.age = age
        self.courses = courses
        self.pocket_money = 0
        self.salary = salary
        Student.student_count += 1 # ทุกครั้งที่มีการสร้าง Object (student) ขึ้นมาจะเพิ่มทีละ 1
        
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
student1 = Student("Alice","Borer", 20, ["Math", "English"],1000)
student2 = Student("Bob","Mokes", 22, ["Physics", "History"],5000)
# เรียกใช้ค่า
student1.display_info()
student2.display_info()

print(Student.student_count)