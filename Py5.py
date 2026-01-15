emp_name=input("Enter Emp Name:")
salary=float(input("Enter Salary :"))
print("\n Performance Rate(1-5): ")
rating=int(input("Enter Rating: "))
if(rating==5):
    bonus=salary*0.20
elif(rating==4):
    bonus=salary*0.15
elif(rating==3):
    bonus=salary*0.10
else:
    print("\nNo Bonus")
final_salary=salary+bonus
print("Employee Name: ",emp_name)
print("Performance rating: ",rating)
print("Bonus Amount: ",bonus)
print("Final Salary:",final_salary)
    
