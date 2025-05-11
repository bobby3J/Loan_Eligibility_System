


def check_loan_eligibility(income, credit_score, total_debt, loan_amount, employment_status):
    dti = (total_debt / income) * 100

    if credit_score < 500:
        return "Not Eligible: Credit score too low"
    elif dti > 40:
        return "Not Eligible: Debt-to-Income ratio too high "
    elif loan_amount > (income * 5):
        return "Not Eligible: Loan amount exceeds limit"
    elif employment_status not in ["Permanent", "Self-Employed"]:
        return "Not Eligible: Unstable employment status"
    else:
        return "Eligible: You qualify for the loan"
    