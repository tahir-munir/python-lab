class student:

    count = 0
    def __init__(self, rollNum, Fname, cnic, address):
        self.rollNum = rollNum
        self.Fname = Fname
        self.cnic = cnic
        self.address = address
        student.count += 1

    def displayEmploy(self):
        print("Name :", self.rollNum , ",", self.Fname , ",", self.cnic  )

    def displaycount():
        print("total Employ:", student.count)
    
while student.count <= 10:
    print("Enter student")
    rollNum = input("Enter roll ")
    Fname = input("Enter Fname ")
    cnic = input("Enter cnic ")
    address = input("Enter address ")
    student1 = student(rollNum , Fname, cnic, address)
    student1.displayEmploy()
    a = int(input("would you like to add new student if yes press 1 other wise press 0 :"))

    if a == 1:
        continue
    else:
        student.displaycount()
        break
    


