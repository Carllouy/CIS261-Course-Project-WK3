#Carl Louy, CIS261, Course project WK7
 
import csv
from datetime import datetime

FILE_NAME = 'employee_data.txt'

totals_Dict = {
    'total_Employees': 0,
    'total_Hours': 0.0,
    'total_Gross_Pay': 0.0,
    'total_Tax': 0.0,
    'total_Net_Pay': 0.0
}

def get_From_Date():
    while True:
        from_date = input("Enter FROM date (mm/dd/yyyy) for report, or 'All' for all records: ")
        if from_date.lower() == 'all':
            return 'all'
        try:
            datetime.strptime(from_date, "%m/%d/%Y")
            return from_date
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy.")

def read_employee_records(from_date):
    """Read employee records from the text file."""
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            record_from_date = row[0]
            if from_date == 'all' or record_from_date == from_date:
                yield row

def display_employee_info(record, gross, tax, net):
    print("\n--- Employee Pay Details ---")
    print(f"From Date: {record[0]}")
    print(f"To Date: {record[1]}")
    print(f"Name: {record[2]}")
    print(f"Hours Worked: {record[3]}")
    print(f"Hourly Rate: {record[4]}")
    print(f"Gross Pay: ${gross:.2f}")
    print(f"Income Tax Rate: {record[5]}")
    print(f"Income Tax: ${tax:.2f}")
    print(f"Net Pay: ${net:.2f}")
    print("-----------------------------\n")

def display_totals():
    print("\n=== Payroll Summary ===")
    print(f"Total Employees: {totals_Dict['total_Employees']}")
    print(f"Total Hours: {totals_Dict['total_Hours']}")
    print(f"Total Gross Pay: ${totals_Dict['total_Gross_Pay']:.2f}")
    print(f"Total Tax: ${totals_Dict['total_Tax']:.2f}")
    print(f"Total Net Pay: ${totals_Dict['total_Net_Pay']:.2f}")
    print("========================\n")

def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def main():
    while True:
        name = input("Enter employee name (or 'End' to finish): ")
        if name.lower() == 'end':
            break
        from_date = input("Enter FROM date (mm/dd/yyyy): ")
        to_date = input("Enter TO date (mm/dd/yyyy): ")
        hours = float(input("Enter total hours worked: "))
        rate = float(input("Enter hourly rate: "))
        tax_rate = float(input("Enter income tax rate (e.g., 0.2 for 20%): "))

        with open(FILE_NAME, 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow([from_date, to_date, name, hours, rate, tax_rate])

    from_date = get_From_Date()
    for record in read_employee_records(from_date):
        hours = float(record[3])
        rate = float(record[4])
        tax_rate = float(record[5])
        gross, tax, net = calculate_pay(hours, rate, tax_rate)

        display_employee_info(record, gross, tax, net)

        totals_Dict['total_Employees'] += 1
        totals_Dict['total_Hours'] += hours
        totals_Dict['total_Gross_Pay'] += gross
        totals_Dict['total_Tax'] += tax
        totals_Dict['total_Net_Pay'] += net

    display_totals()

if __name__ == "__main__":
    main()