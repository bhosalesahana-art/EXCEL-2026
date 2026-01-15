name=input("Enter Intern Name")
age=int(input("Enter Age"))
email=input("Enter Email ID")
contact=input("Enter contact Number")
percentage=float(input("Enter Graduation Percentage"))

if(age>=18):
    if(percentage>60):
        if(len(contact)==10):
           print("Intern Is Eligible")
        else:
            print("Contact number must be equal to 10")
    else:
        print("percentage must be Greater than 60")
else:
    print("Age must be Greater than 18")




    
        
