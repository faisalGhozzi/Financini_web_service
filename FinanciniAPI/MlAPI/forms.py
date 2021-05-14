from django import forms

class ApprovalForm(forms.Form):
    sct=forms.CharField(max_length=15)
    capitaux_propres=forms.FloatField()
    passifs_non_courant=forms.FloatField()
    total_bilan=forms.FloatField()
    stock=forms.FloatField()
    creance_client=forms.FloatField()
    actif_immobilier=forms.FloatField()
    resultat_net=forms.FloatField()
    chiffre_d_affaires=forms.FloatField()
