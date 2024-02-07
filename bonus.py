#calculate salary received in the tv
print("Salary")
salary = float(input("Enter Salary: "))
print("Years worked")
years = int(input("Enter years worked: "))
if years >=10:
    bonus = 0.1* salary
    net_salary =bonus+ salary
    print ("bonus is: ", bonus)
    print ("net_salary: ", net_salary)

elif  years >=6 and years <= 10:
    bonus = 0.08* salary
    net_salary =bonus+ salary
    print ("bonus is: ", bonus)
    print ("net_salary: ", net_salary)   

elif  years <6:
    bonus = 0.06* salary
    net_salary =bonus+ salary
    print ("bonus is: ", bonus)
    print ("net_salary: ", net_salary) 

else:
    print("Invalid")
