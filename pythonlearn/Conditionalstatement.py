#Vote eligibility checker

age=input("Enter your age")

if int(age)<0:
    print("Invalid input")
else:
    if int(age)<18:
        print("Not eligible to vote")   
    else:
        print("Eligible to vote")
         

