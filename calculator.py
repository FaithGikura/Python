print("a simple calculator")
num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))

print("\n choose operator")
print("1. Addition(+)")
print("2. Subtraction(-)")
print("3. Multiplication(*)")
print("4. Division(/)")
print("5. Modulus(%)")
print("6. Exponent(^)")
print("7. Floor division(//)")

print("Enter operator of choice")
choice=input("Enter choice (1-7)")

if choice=='1':
    result=num1 + num2
    print(f"{num1} + {num2}= {result}")
if choice == '2':
    result = num1-num2
    print(f"{num1} - {num2}= {result}")
if choice == '3':
    result =-num1 * num2
    print(f"{num1} *{num2}= {result}")
if choice == '4':
    if num2==0:
        print('Error! division by zero is not allowed')
    else:
        result = num1 / num2
        print(f"{num1} / {num2}={result}")
if choice=='5':
     result=num1 % num2
     print(f"{num1} %{num2}={result}")
if choice =='6':
    result=num1 ** num2 
    print(f"{num1} ^{num2}={result}")
if choice=='7':
    result=num1 // num2
    print(f"{num1} // {num2}={result}")
else:
    print("Error! cannot perform floor division by 0")
if choice not in ['1','2','3','4','5','6','7']:
    print("ERROR! pick a choice within range 1-7")



