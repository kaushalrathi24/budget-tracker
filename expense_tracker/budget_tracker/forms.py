# from dataclasses import fields
# from django import forms
    
from dataclasses import fields
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Transactions

class TransactionForm(BSModalModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'
