def square(item_list):
    square = []
    for i in item_list:
        square.append(i**2)
    return square

my_list = [17,53,8]
my_result = square(my_list)

print("list before", my_list)
print("list before", my_result)


def sensorDetect(tem):
    for i in tem:
        if i < 30:
            print(f"temperature is {i} turn off AC") 
        else:
            print(f"temperature is {i} turn on AC") 


sensorList = [10,20,30,40,50]
sensorDetect(sensorList)