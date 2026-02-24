History=[]
def Add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    if b==0:
        return " error:cannot divide by zero"
    return a/b
def Power(a,b):
    return a**b
while True:
    print("--------project_Calculater--------")
    print("1.Add")
    print("2.Subtract")
    print("3.Miltiply") 
    print("4.Divide")
    print("5.Power")
    print("6.Show_History")
    print("7.Exit")
    choice=input("enter your choice(1-7):")
    if choice=="7":
        print("Thank you!")
        break
    if choice=="6":
        print("-----Calulation_History-----")
        for item in History:
            print(item)
        continue
    try:
        num1=float(input("enter first number:"))
        num2=float(input("enter secomd number:"))
    except ValueError:
        print("Invalid input! please enter numbers only.")
        continue
    if choice=="1":
        result=Add(num1,num2)
        operation=f"{num1}+{num2}={result}"
    elif choice=="2":
        result=Subtract(num1,num2)
        operation=f"{num1}-{num2}={result}"
    elif choice=="3":
        result=Multiply(num1,num2)
        operation=f"{num1}*{num2}={result}"
    
    elif choice=="4":
        result=Divide(num1,num2)
        operation=f"{num1}/{num2}={result}"
    elif choice=="5":
        result=Power(num1,num2)
        operation=f"{num1}^{num2}={result}"
    else:
        print("Invalid choice")
        continue
    print("result:",result)
    History.append(operation)    