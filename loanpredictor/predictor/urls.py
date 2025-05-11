from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('', views.apply_for_loan, name='apply'),
]