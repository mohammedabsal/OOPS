class Student: ##class is the blueprint  methods+data member
    def __init__(self,name=None,number=None): #self - refer to the current object itself // __init__ its automatically runs
        self.name=name
        self.number=number
    def family_detail(self,fathername,mothername):
        self.fathername=fathername
        self.mothername=mothername
s1=Student("Absal",99438) #we can directly pass the arguments to the class 
p1=Student()  # we need  to create the object then pass the arguments 
p1.family_detail("sk","sy")
print(s1.name)
print(p1.fathername)