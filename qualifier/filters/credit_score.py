"""
This module filters the credit score input by the User and compares
it to minimum credit scores allowed by Lenders.  It then filters the available
list of Lenders that meet the criteria and returns them to a variable called
credit_score_approval_list.
"""

def filter_credit_score(credit_score, bank_list):
    credit_score_approval_list = []
    for bank in bank_list:
         if credit_score >= int(bank[4]):
            credit_score_approval_list.append(bank)
    return credit_score_approval_list   
