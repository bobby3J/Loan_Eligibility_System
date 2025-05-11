from django import forms
from .models import LoanApplication

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['full_name', 'income', 'credit_score', 'total_debt', 'loan_amount', 'employment_status']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'income': forms.NumberInput(attrs={'class': 'form-control'}),
            'credit_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_debt': forms.NumberInput(attrs={'class': 'form-control'}),
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'employment_status': forms.Select(attrs={'class': 'form-control'}),
        }
