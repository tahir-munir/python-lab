class Employ:
    
    count = 0
    def __init__(self, Eid, Ename, Esalary, Erank):
        self.Eid = Eid
        self.Ename = Ename
        self.Esalary = Esalary
        self.Erank = Erank
        Employ.count += 1

    
    def displayEmploy(self):
        print("Name :", self.Ename , ",", self.Esalary , ",", self.Erank  )

    def displaycount():
        print("total Employ:", Employ.count)


while Employ.count <= 10:
    print("Enter student")
    id = input("Enter id")
    name = input("Enter name")
    sal = input("Enter salary")
    rank = input("Enter rank")
    student = Employ(id,name,sal,rank)
    


obj1 = Employ(1,"ali",300,"18 Grade")
obj2 = Employ(2,"ali",300,"18 Grade")
obj3 = Employ(2,"ali",300,"18 Grade")

obj1.displayEmploy()
obj2.displayEmploy()
obj3.displayEmploy()
Employ.displaycount()