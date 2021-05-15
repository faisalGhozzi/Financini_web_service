from django import forms

class ApprovalForm(forms.Form):
    sct=forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder' : "Enter enterprise name"}))
    capitaux_propres=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder' : "Shareholders equity"}))
    passifs_non_courant=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder' : "Non-current liabilities"}))
    total_bilan=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder' : "Total balance sheet"}))
    stock=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder' : "Stock/Inventory"}))
    creance_client=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder' : "Receivables"}))
    actif_immobilier=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder' : "Real estate asset"}))
    resultat_net=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder' : "Net income"}))
    chiffre_d_affaires=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder' : "Revenues"}))
    security_deposit=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder' : "Security deposit"}))
    loan_ammount=forms.FloatField(widget=forms.NumberInput(attrs={'placeholder' : "Loan ammount"}))
