lMarks =  int(input("Enter theory marks : "))
tMarks = int(input("enter lab marks : "))

avg = (lMarks + tMarks) / 200 * 100

print(avg)


if avg > 85 and  avg <= 100:
    print("congratulations you sccored grade A..")
elif avg > 70 and avg <= 85:
    print("congrats you got grade B..")
elif avg > 60 and avg <= 70:
    print("congrats you scored C..")
elif avg > 50 and avg <= 60:
    print("congrats you scored D..")
else:
    print("fail")