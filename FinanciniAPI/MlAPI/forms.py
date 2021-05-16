from django import forms

class ApprovalForm(forms.Form):
    sct=forms.CharField(max_length=15, label= 'Enterprise', widget=forms.TextInput(attrs={'placeholder' : "Enter enterprise name"}))
    capitaux_propres=forms.FloatField(label= "Shareholders' equity", widget=forms.NumberInput(attrs={'placeholder' : "Shareholders equity"}))
    passifs_non_courant=forms.FloatField(label= 'Non-current liabilities', widget=forms.NumberInput(attrs={'placeholder' : "Non-current liabilities"}))
    total_bilan=forms.FloatField(label= 'Balance sheet total', widget=forms.NumberInput(attrs={'placeholder' : "Total balance sheet"}))
    stock=forms.FloatField(label= 'Stock', widget=forms.NumberInput(attrs={'placeholder' : "Stock/Inventory"}))
    creance_client=forms.FloatField(label= 'Receivables', widget=forms.NumberInput(attrs={'placeholder' : "Receivables"}))
    actif_immobilier=forms.FloatField(label= 'Property assets', widget=forms.NumberInput(attrs={'placeholder' : "Real estate asset"}))
    resultat_net=forms.FloatField(label= 'Net result', widget=forms.NumberInput(attrs={'placeholder' : "Net income"}))
    chiffre_d_affaires=forms.FloatField(label= 'Revenues', widget=forms.NumberInput(attrs={'placeholder' : "Revenues"}))
    security_deposit=forms.FloatField(label= 'Security deposit', widget=forms.NumberInput(attrs={'placeholder' : "Security deposit"}))
    loan_ammount=forms.FloatField(label= 'Loan ammount', widget=forms.NumberInput(attrs={'placeholder' : "Loan ammount"}))
