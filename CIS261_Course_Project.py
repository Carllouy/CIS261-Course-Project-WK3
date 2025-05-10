#Carl Louy, CIS261, Course project WK5
 
from datetime import datetime

employee_records = []
totals_dict = {
    'total_Employees': 0,
    'total_Hours': 0.0,
    'total_Gross_Pay': 0.0,
    'total_Tax': 0.0,
    'total_Net_Pay': 0.0
}


def get_Employee_Name():
    name = input("Enter employee name (or 'End' to finish): ")
    return name

def get_Date_Range():
    while True:
        try:
            from_date = input("Enter FROM date (mm/dd/yyyy): ")
            from_dt = datetime.strptime(from_date, "%m/%d/%Y")
            to_date = input("Enter TO date (mm/dd/yyyy): ")
            to_dt = datetime.strptime(to_date, "%m/%d/%Y")

            if from_dt > to_dt:
                print("FROM date cannot be after TO date.")
                continue

            return from_date, to_date
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy.")

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
            tax_rate = float(input("Enter income tax rate (e.g., 0.2 for 20%): "))
            return tax_rate
        except ValueError:
            print("Invalid input. Please enter a decimal.")


def calculate_Pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_Employee_Info(from_date, to_date, name, hours, rate, gross, tax_rate, tax, net):
    print("\n--- Employee Pay Details ---")
    print(f"Date Range: {from_date} to {to_date}")
    print(f"Name: {name}")
    print(f"Hours Worked: {hours}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross:.2f}")
    print(f"Income Tax Rate: {tax_rate:.2%}")
    print(f"Income Tax: ${tax:.2f}")
    print(f"Net Pay: ${net:.2f}")
    print("-----------------------------\n")

def display_Totals(totals):
    print("\n=== Payroll Summary ===")
    print(f"Total Employees: {totals['total_Employees']}")
    print(f"Total Hours: {totals['total_Hours']}")
    print(f"Total Gross Pay: ${totals['total_Gross_Pay']:.2f}")
    print(f"Total Tax: ${totals['total_Tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_Net_Pay']:.2f}")
    print("========================\n")


while True:
    name = get_Employee_Name()
    if name.lower() == "end":
        break

    from_date, to_date = get_Date_Range()
    hours = get_Total_Hours()
    rate = get_Hourly_Rate()
    tax_rate = get_Income_Tax_Rate()

    employee_records.append({
        'from_date': from_date,
        'to_date': to_date,
        'name': name,
        'hours': hours,
        'rate': rate,
        'tax_rate': tax_rate
    })


if not employee_records:
    print("\nNo employee data was entered.")
else:
    for record in employee_records:
        gross, tax, net = calculate_Pay(record['hours'], record['rate'], record['tax_rate'])

        display_Employee_Info(
            record['from_date'],
            record['to_date'],
            record['name'],
            record['hours'],
            record['rate'],
            gross,
            record['tax_rate'],
            tax,
            net
        )

        totals_dict['total_Employees'] += 1
        totals_dict['total_Hours'] += record['hours']
        totals_dict['total_Gross_Pay'] += gross
        totals_dict['total_Tax'] += tax
        totals_dict['total_Net_Pay'] += net

    display_Totals(totals_dict)