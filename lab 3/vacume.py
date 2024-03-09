def reflexVacume( location, status):
    if status == "dirty":
        print("suckkk")
        if location == "A":
            print("turn rigt")
        elif location == "B":
            print("turn left")
    else:
        print("do nothing")


reflexVacume("A","dirty")