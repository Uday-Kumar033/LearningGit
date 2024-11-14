#here is the program to calculate rent of room where students are living 

persons = int(input("The Total number of person in that room = "))
electricty = int(input("TOtal current deducte from by using electricity = "))
charge = int(input("Total amount of charge per unit = "))
room =  int(input("Room rent per month = "))
water = int(input("Enter rate of water per bottle ="))
noOfWater = int(input("No. of water bottle in a month ="))
food = int(input("Enter amount that are use in snacks ="))
#operation 
total_light = electricty*charge
total_water = water*noOfWater
output =(total_water+total_light+room+food)//persons 
print()
print("Total amount on per person =", end="")
print(output)
print("Total bill in a month = ", end="")
print(output*persons)