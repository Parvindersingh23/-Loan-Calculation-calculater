def lone(principal, rate, time, downepaymentz,):
    simple_interest = (principal * rate * time)/100
    total_amount = principal + simple_interest - downepaymentz
    return simple_interest,total_amount


def userinput ():
    while True:
        try:
            principal = float(input("Enter your principal amount in (₹)"))
            downepaymentz = float(input("Enter your  downepaymentz (if existe)"))
            rate = float(input("Enter your interest rate in (% per month)"))
            time = float(input("Enter your time in (months)"))
           # downepaymentz = float(input("Enter your  downepaymentz (if existe)"))


            if principal > 0 and rate > 0 and time > 0 and  downepaymentz >= 0 :
                return principal, rate, time, downepaymentz
            else :
                print("Values must be positive. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def result (principal, rate, time, downepaymentz,simple_interest, total_amount ):
    print("Loan Calculation Results")
    print(f"Loan Amount (₹): {principal}")
    print(f"Interest Rate (% per month): {rate}")
    print(f"Loan Duration (months): {time}")
    print(f" downepaymentz: {downepaymentz}")
    print(f"Simple Interest (₹): {simple_interest}")
    print(f"Total Amount to be Paid (₹): {total_amount}")
    print("Thank you for using the Loan Interest Calculator!")

def main():
    while True :
        print("=== Loan Calculation calculater ===")
        principal, rate, time, downepaymentz = userinput ()
        simple_interest,total_amount = lone(principal, rate, time, downepaymentz,)
        result (principal, rate, time, downepaymentz,simple_interest, total_amount )

        choice = input("Would you like to calculate another loan? (yes/no): ").strip().lower()
        if choice not in ("yes", "y"):
            print("Goodbye! Have a great day!")
            break
 
if __name__ =="__main__":
    main()
        