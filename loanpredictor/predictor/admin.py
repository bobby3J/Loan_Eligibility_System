from django.contrib import admin
from .models import LoanApplication

# Register your models here.
@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'income', 'credit_score', 'total_debt', 'loan_amount', 'employment_status', 'eligibility_result')
    search_fields = ('full_name', 'employment_status')
    list_filter = ('employment_status', 'credit_score')