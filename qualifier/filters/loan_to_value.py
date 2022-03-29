"""
This module calculates the loan amount desired by the customer and 
compares it to the total value of the asset being purchased.  It filters the 
returned loan to value calculated against the criteria of a collection of 
Lenders and returns the list in a variable called loan_to_value_approval_list.
"""

def filter_loan_to_value(loan_to_value_ratio, bank_list):
    loan_to_value_approval_list = []
    for bank in bank_list:
        if loan_to_value_ratio <= float(bank[2]):
            loan_to_value_approval_list.append(bank)
    return loan_to_value_approval_list