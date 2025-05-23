#Carl Louy, CIS261, Course project WK7
 

import csv
from datetime import datetime

# Constants
FILE_NAME = 'employee_data.txt'
TAX_RATE_PROMPT = "Enter income tax rate (e.g., 0.2 for 20%): "

# Data Structures
totals = {
    'total_employees': 0,
    'total_hours': 0.0,
    'total_gross_pay': 0.0,
    'total_tax': 0.0,
    'total_net_pay': 0.0
}

# Functions
def get_employee_name():
    """Prompt user to enter employee name."""
    return input("Enter employee name (or 'End' to finish): ")

def get_date_range():
    """Prompt user to enter a valid date range."""
    while True:
        try:
            from_date = input("Enter FROM date (mm/dd/yyyy): ")
            to_date = input("Enter TO date (mm/dd/yyyy): ")
            from_dt = datetime.strptime(from_date, "%m/%d/%Y")
            to_dt = datetime.strptime(to_date, "%m/%d/%Y")
            if from_dt > to_dt:
                print("FROM date cannot be after TO date.")
                continue
            return from_date, to_date
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy.")

def get_float_input(prompt):
    """Prompt user to enter a valid float value."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_pay(hours, rate, tax_rate):
    """Calculate gross pay, tax, and net pay."""
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def write_employee_record(record):
    """Append employee record to the text file."""
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(record)

def display_employee_info(from_date, to_date, name, hours, rate, gross, tax_rate, tax, net):
    """Display detailed information for an employee."""
    print(f"\n--- Employee Pay Details ---")
    print(f"Date Range: {from_date} to {to_date}")
    print(f"Name: {name}")
    print(f"Hours Worked: {hours}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross:.2f}")
    print(f"Income Tax Rate: {tax_rate:.2%}")
    print(f"Income Tax: ${tax:.2f}")
    print(f"Net Pay: ${net:.2f}")
    print("-----------------------------\n")

def display_totals(totals):
    """Display payroll summary."""
    print("\n=== Payroll Summary ===")
    print(f"Total Employees: {totals['total_employees']}")
    print(f"Total Hours: {totals['total_hours']}")
    print(f"Total Gross Pay: ${totals['total_gross_pay']:.2f}")
    print(f"Total Tax: ${totals['total_tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_net_pay']:.2f}")
    print("========================\n")

def read_employee_records(from_date):
    """Read employee records from the text file."""
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            record_from_date = row[0]
            if from_date == "All" or record_from_date == from_date:
                yield row

# Main Program
while True:
    name = get_employee_name()
    if name.lower() == 'end':
        break

    from_date, to_date = get_date_range()
    hours = get_float_input("Enter total hours worked: ")
    rate = get_float_input("Enter hourly rate: ")
    tax_rate = get_float_input(TAX_RATE_PROMPT)

    record = [from_date, to_date, name, hours, rate, tax_rate]
    write_employee_record(record)

if input("\nWould you like to generate a report? (y/n): ").lower() == 'y':
    while True:
        from_date_input = input("Enter the 'From Date' for the report (mm/dd/yyyy) or 'All' for all records: ")
        try:
            if from_date_input != "All":
                datetime.strptime(from_date_input, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy.")

    for row in read_employee_records(from_date_input):
        from_date, to_date, name, hours, rate, tax_rate = row
        hours = float(hours)
        rate = float(rate)
        tax_rate = float(tax_rate)
        gross, tax, net = calculate_pay(hours, rate, tax_rate)

        display_employee_info(from_date, to_date, name, hours, rate, gross, tax_rate, tax, net)

        totals['total_employees'] += 1
        totals['total_hours'] += hours
        totals['total_gross_pay'] += gross
        totals['total_tax'] += tax
        totals['total_net_pay'] += net

    display_totals(totals)