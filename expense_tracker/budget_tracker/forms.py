# from django import forms
# from .models import *

# class CreateForm(forms.ModelForm):
#     class Meta:
#         model = Transactions
#         fields = ('title', 'description', 'amount', 'to', 'date', 'category', 'type')
#         TYPE_CHOICES = (
#             ('income', "Income"),
#             ('expense', "Expense")
#         )
#         widgets = {
#             'title': forms.CharField(attrs={'class': 'form-control'}),
#             'description' : forms.Textarea(attrs={'class': 'form-control'}),
#             'amount': forms.FloatField(attrs={'class': 'form-control'}),
#             'to': forms.CharField(attrs={'class': 'form-control'}),
#             'date': forms.DateTimeField(attrs={'class': 'form-control'}),
#             'category' : forms.CharField(attrs={'class': 'form-control'}),
#             'type' : forms.ChoiceField(attrs={'class': 'form-control'}, choices=TYPE_CHOICES)
#         }