"""
This module compares the loan size requested by the applicant to the 
maximum size loan available from Lenders.  It filters the available
Lenders and populates into a variable called loan_size_approval_list.
"""

def filter_max_loan_size(loan_amount, bank_list):
    loan_size_approval_list = []

    for bank in bank_list:
        if loan_amount <= int(bank[1]):
            loan_size_approval_list.append(bank)
    return loan_size_approval_list