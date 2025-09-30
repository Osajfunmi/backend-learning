age= int(input("enter your age:"))
if age<0:
    print ("invalid age")
elif 0<= age <= 12:
    print ("your ticket price is #500")
elif 13<= age <= 17:
    print ("your ticket price is #1000")
elif 18<= age <= 59:
    print ("your ticket price is #2000")
else:
    print ("your ticket price is #1000, (discount for seniors)")