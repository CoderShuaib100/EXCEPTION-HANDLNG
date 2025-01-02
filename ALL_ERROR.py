try:
    print("num1 is the numerator and num2 is the deniminator")
    num1 , num2 = eval(input("Enter two numbers seperated by comma: "))
    print(num1/num2)
except ValueError as Vex:
    print("Excpetion:",Vex)

except ZeroDivisionError:
    print("Exception: Zero division error has occured!")

except SyntaxError as SynEr:
    print("Exception:",SynEr)

else:
    print("No exception hs occured,The program has finished successfully!")

finally:
    print("The division program of two numbers is done!")