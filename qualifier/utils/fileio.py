#import csv
from pathlib import Path

def load_csv(csvpath):
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
        print(data)
    return data
# As a lender,
# I want to calculate the monthly debt-to-income ratio
# so that we can assess the ability to pay of the borrower
def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    print(f"This is the monthly debt ratio", monthly_debt_ratio)
    return monthly_debt_ratio


# As a lender,
# I want to calculate the loan-to-value ratio
# so that we can evaluate the risk of lending money to the borrower
def calculate_loan_to_value_ratio(loan_amount, home_value):
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    print(f"This is the Loan to Value (LTV) ratio", loan_to_value_ratio)
    return loan_to_value_ratio