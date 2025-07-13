class Students:
    def __init__(self ,name , age, grade):
        self.name  = name
        self.age   = age
        self.grade = grade

student1 = Students('Pratiksha pandey', 21 , 'A')
student2 = Students('Bob' , 12 , 'B')
student3 = Students('kaplesh' , 20 , 'C')

print(student1.name , student1.age , student1.grade)
print(student2.name , student2.age , student2.grade)
print(student3.name , student3.age , student3.grade)