from .forms import ApprovalDlForm
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.parsers import JSONParser
from .models import approvalsDl
from .serializers import approvalDlSerializers
from keras.models import load_model
import json
import numpy as np
import pandas as pd

# Create your views here.
class ApprovalsDlView(viewsets.ModelViewSet):
    queryset = approvalsDl.objects.all()
    serializer_class = approvalDlSerializers

# @api_view(["POST"])
def approvereject(unit):
    try:
        if float(unit['security_deposit']) == 0.0:
            return 'Rejected'
        if(float(unit['security_deposit']) >= float(unit['loan_ammount'])):
            return 'Approved'
        if float(unit['security_deposit']) / float(unit['loan_ammount']) < 0.5:
            return 'Rejected'
        if float(unit['security_deposit']) / float(unit['loan_ammount']) >= 0.5 and float(unit['security_deposit']) / float(unit['loan_ammount']) < 1:
            mdl= load_model("../research/loan_model_dl.h5")
            unit['ratio_de_solvabilite'] = float(unit['passifs_non_courant']) / float(unit['capitaux_propres'])
            unit['ratio_de_rentabilite'] = float(unit['resultat_net']) / float(unit['capitaux_propres'])
            unit['ratio_d_endettement'] = (float(unit['total_bilan']) - float(unit['capitaux_propres'])) / float(unit['total_bilan'])
            unit['marge_nette_sur_vente'] = (float(unit['resultat_net']) / float(unit['chiffre_d_affaires'])) * 100
            x_cols = ['ratio_de_solvabilite', 'ratio_de_rentabilite', 'ratio_d_endettement', 'marge_nette_sur_vente']
            y_pred=mdl.predict(unit[x_cols])
            newdf=pd.DataFrame(y_pred, columns=['Status'])
            newdf=newdf.replace({1:'Approved', 0:'Rejected'})
            return newdf.values[0][0]
    except ValueError as e:
        return (e.args[0])

def sctcontact(request):
    if request.method == 'POST':
        form=ApprovalDlForm(request.POST)
        if form.is_valid():
            sct = form.cleaned_data['sct']
            capitaux_propres = form.cleaned_data['capitaux_propres']
            passifs_non_courant = form.cleaned_data['passifs_non_courant']
            total_bilan = form.cleaned_data['total_bilan']
            stock = form.cleaned_data['stock']
            creance_client = form.cleaned_data['creance_client']
            actif_immobilier = form.cleaned_data['actif_immobilier']
            resultat_net = form.cleaned_data['resultat_net']
            chiffre_d_affaires = form.cleaned_data['chiffre_d_affaires']
            security_deposit = form.cleaned_data['security_deposit']
            loan_ammount = form.cleaned_data['loan_ammount']
            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict, index=[0])
            answer = approvereject(df)
            messages.success(request, 'Application Status: {}'.format(answer))
    
    form=ApprovalDlForm()

    return render(request, 'myform/form.html', {'form':form})