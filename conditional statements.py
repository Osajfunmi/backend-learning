age= int(input("Enter your age:"))
if age<0: 
    print ("invalid age!")
elif 0<= age<=12:
    print ("you're a child")
elif 13<= age <= 19:
    print ("you're a teenager")
elif 20<= age <= 59:
    print ("you're an adult")
else:
    print ("you're a senior citizen")