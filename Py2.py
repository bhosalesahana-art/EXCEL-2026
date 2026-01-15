emp_name=input("Enter Emp Name:")
emp_id=int(input("Enter Emp_ID :"))
basic_salary=float(input("Enter Basic Salary:"))
hra=basic_salary*0.20
da=basic_salary*0.10
pf=basic_salary*0.12
net_salary=basic_salary+hra+da-pf
print("Emp_Name:",emp_name)
print("Emp_ID:",emp_id)
print("Basic_salary:",basic_salary)
print("HRA 20%:",hra)
print("DA 10%:",da)
print("PF 12%:",pf)
print("Net_Salary:",net_salary)
           
