
print("Course Avaliable:\n")
print("1.Python Programming\n 2.Data Analytics\n 3.AI & ML\n")
course=input("Enter Course Name:")
if(course=="Python"):
    fee=5000
elif(course=="Data Analytics"):
    fee=8000
elif(course=="AI&ML"):
    fee=12000
else:
    print("invalid course selected")
discount=fee*0.10
early_discount=fee*0.5
total_discount=discount+early_discount
final_amount=fee-total_discount
print("Course Name:",course)
print("Fee:",fee)
print("Total Discount:",total_discount)
print("Payable Amount:",final_amount)

