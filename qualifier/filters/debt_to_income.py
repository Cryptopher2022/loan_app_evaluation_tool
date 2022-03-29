"""
This module evaluates the monthly debt payments currently being made
by the applicant as compared to their monthly total income.  It then takes
the debt to income and compares it to the criteria provided by a collection
of Lenders and filters the available loans and returns them in a variable
called debt_to_income_approval_list.
"""

def filter_debt_to_income(monthly_debt_ratio, bank_list):
    debt_to_income_approval_list = []
    for bank in bank_list:
        if monthly_debt_ratio <= float(bank[3]):
            debt_to_income_approval_list.append(bank)
    return debt_to_income_approval_list