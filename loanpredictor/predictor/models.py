from django.db import models

# Create your models here.

class LoanApplication(models.Model):
    Employment_choices = [
        ('Permanent', 'Permanent'),
        ('Self-Employed', 'Self-Employed'),
        ('Contract', 'Contract'),
        ('Unemployed', 'Unemployed'),
    ]

    full_name = models.CharField(max_length=100)
    income = models.FloatField()
    credit_score = models.IntegerField()
    total_debt = models.FloatField()
    loan_amount = models.FloatField()
    employment_status = models.CharField(max_length=20, choices=Employment_choices)
    eligibility_result = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
     return self.full_name