#This python code calculate and convert temperature Fahrenheit to Celsius Formula and vese versa

des = ("Choice temperature calcuation you would like to do:")
print (des)
choice  = input ("Select 1) F to C or 2) C to F: ")

# print = (choice1)
if choice == ('1'):
    fah  = (float(input("Enter Fahrenheit temperature? ")))
    confah = (fah-32)/1.8
    print ("You entered", fah)
    print ("The Celsius temperature", confah)

else:
    cel  = (float(input("Enter Celsisu temperature? ")))
    concel = (cel*1.8)+32
    print ("You entered ", cel)
    print ("The Fahrenheit temperature", concel)