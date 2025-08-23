# file 10

# school fees breakdown
school_name =str(input("ENTER SCHOOL NAME: "))
tution_fee =float(input("HOW MUCH DO YOU WANT TO PAY FOR TUTION FEE: "))
hostel_fee =float(input("HOW MUCH DO YOU WANT TO PAY FOR HOSTEL FEE: "))
feeding_fee =float(input("HOW DO YOU WANT TO PAY FOR FEEDING FEE: "))
total_fee =(tution_fee + hostel_fee + feeding_fee ) #total fee

# print in receipt format
print(f"\n\t|---{school_name} receipt---|")
print(f"\n\t    TUTION FEE: ₦{tution_fee}    \n\t    HOSTEL FEE: ₦{hostel_fee}    \n\t    FEEDING FEE: ₦{feeding_fee}    \n\t    TOTAL FEE: ₦{total_fee:.2f}    ")
print(f"\n\t|---Thanks for your payment---|")
