# using the try and except keywords

try:
    num = int(input("Enter a number: "))
    print("The number entered by the user is:",num)
except ValueError as Vex:
    print("Exception:",Vex)
     