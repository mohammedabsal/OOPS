class Student:
    def __init__(self,name=None,number=None):
        self.name=name
        self.number=number
    def family_detail(self,fathername,mothername):
        self.fathername=fathername
        self.mothername=mothername
p1=Student()
s1=Student("Absal",9943816710)
p1.family_detail("sk","sy")
print(s1.name)
print(p1.fathername)