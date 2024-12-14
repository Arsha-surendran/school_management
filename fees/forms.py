from django import forms
from core.models import FeesHistory

class FeesHistoryForm(forms.ModelForm):
    class Meta:
        model = FeesHistory
        fields = ['student', 'fee_type', 'amount', 'payment_date', 'remarks']  # Include all relevant fields
