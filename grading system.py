#a grading system
Data_comm= float(input("Enter Data_comm grade: "))
Networking= float(input("Enter Networking grade: "))
Graphics= float(input("Enter Graphics grade: "))
#formula
Total = (Data_comm + Networking + Graphics) /3
print ("Total Score: ", Total)
if Total >=70 and Total <=100:
    print(" GRADE IS A")
elif Total >=60 and Total <=69:
    print(" GRADE IS B")
elif Total >=50 and Total <=59:
    print(" GRADE IS C")
elif Total >=40 and Total <=49:
    print(" GRADE IS D")
elif Total >=0 and Total <=39:
    print(" FAIL")
else:
    print("Invalid marks entered")

