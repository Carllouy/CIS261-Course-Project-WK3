#Carl Louy, CIS261, Create and call functions with parameters
 
total_Employees = 0
total_Hours = 0.0
total_Gross_Pay = 0.0
total_Tax = 0.0
total_Net_Pay = 0.0
 
def get_Employee_Name():
     name = input("Enter employee name (or 'End' to finish): ")
     return name
 
def get_Total_Hours():
     while True:
         try:
             hours = float(input("Enter total hours worked: "))
             return hours
         except ValueError:
             print("Invalid input. Please enter a number.")
 
def get_Hourly_Rate():
     while True:
         try:
             rate = float(input("Enter hourly rate: "))
             return rate
         except ValueError:
             print("Invalid input. Please enter a number.")
 
def get_Income_Tax_Rate():
     while True:
         try:
             tax_Rate = float(input("Enter income tax rate (as a decimal, e.g., 0.2 for 20%): "))
             return tax_Rate
         except ValueError:
             print("Invalid input. Please enter a decimal number.")
 
def calculate_Pay(hours, rate, tax_rate):
     gross_Pay = hours * rate
     income_Tax = gross_Pay * tax_rate
     net_Pay = gross_Pay - income_Tax
     return gross_Pay, income_Tax, net_Pay
 
def display_Employee_Info(name, hours, rate, gross, tax_rate, tax, net):
     print("\n--- Employee Pay Details ---")
     print(f"Name: {name}")
     print(f"Hours Worked: {hours}")
     print(f"Hourly Rate: ${rate:.2f}")
     print(f"Gross Pay: ${gross:.2f}")
     print(f"Income Tax Rate: {tax_rate:.2%}")
     print(f"Income Tax: ${tax:.2f}")
     print(f"Net Pay: ${net:.2f}")
     print("-----------------------------\n")
 
def display_Totals(emp_Count, total_Hrs, total_Gross, total_Tax, total_Net):
     print("\n=== Payroll Summary ===")
     print(f"Total Employees: {emp_Count}")
     print(f"Total Hours: {total_Hrs}")
     print(f"Total Gross Pay: ${total_Gross:.2f}")
     print(f"Total Tax: ${total_Tax:.2f}")
     print(f"Total Net Pay: ${total_Net:.2f}")
     print("========================\n")
 
while True:
     name = get_Employee_Name()
     if name.lower() == "end":
         break
 
     hours = get_Total_Hours()
     rate = get_Hourly_Rate()
     tax_Rate = get_Income_Tax_Rate()
 
     gross, tax, net = calculate_Pay(hours, rate, tax_Rate)
     display_Employee_Info(name, hours, rate, gross, tax_Rate, tax, net)
 
     total_Employees += 1
     total_Hours += hours
     total_Gross_Pay += gross
     total_Tax += tax
     total_Net_Pay += net
 
display_Totals(total_Employees, total_Hours, total_Gross_Pay, total_Tax, total_Net_Pay)
