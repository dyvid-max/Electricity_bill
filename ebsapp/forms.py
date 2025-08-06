from django import forms
from .models import Customer, Connection, Bill, Payment

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class ConnectionForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['card_number', 'expiry_date', 'cvc']
        widgets = {
            'card_number': forms.TextInput(attrs={'placeholder': '1234567890123456'}),
            'expiry_date': forms.TextInput(attrs={'placeholder': 'MM/YY'}),
            'cvc': forms.PasswordInput(attrs={'placeholder': 'CVC'}),
        }