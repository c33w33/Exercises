#to run exercise7 module and get car age

import exercise7 as e7


# year = int(input("Input Car Year:"))
# make = input("Input Car Make:")
# model = input("Input Car Model:")
car1 = e7.Car(20,'make','model')
print("Age is " + str(car1.age()))
