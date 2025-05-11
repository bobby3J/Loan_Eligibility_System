from django.shortcuts import render, redirect
from .forms import LoanApplicationForm
from .utils import check_loan_eligibility

# Create your views here.
def apply_for_loan(request):
    form = LoanApplicationForm(request.POST)
    if form.is_valid():
        loan_app = form.save(commit=False)
        result = check_loan_eligibility(
            loan_app.income,
            loan_app.credit_score,
            loan_app.total_debt,
            loan_app.loan_amount,
            loan_app.employment_status
        )
        loan_app.eligibility_result = result
        loan_app.save()
        return render(request, 'predictor/result.html', {'loan_app': loan_app})
    else:
        form = LoanApplicationForm()
    return render(request, 'predictor/apply.html', {'form': form})

