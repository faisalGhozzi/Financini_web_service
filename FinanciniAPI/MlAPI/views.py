from .forms import ApprovalForm
from django.shortcuts import render
# from .forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.parsers import JSONParser
from .models import approvals
from .serializers import approvalSerializers
import pickle
import joblib
import json
import numpy as np
import pandas as pd


# Create your views here.
class ApprovalsView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = approvalSerializers

# @api_view(["POST"])
def approvereject(unit):
    try:
        if float(unit['security_deposit']) == 0.0:
            print('first cond')
            return 'Rejected'
        if(float(unit['security_deposit']) >= float(unit['loan_ammount'])):
            print('snd cond')
            return 'Approved'
        if float(unit['security_deposit']) / float(unit['loan_ammount']) < 0.5:
            print('third cond')
            return 'Rejected'
        if float(unit['security_deposit']) / float(unit['loan_ammount']) >= 0.5 and float(unit['security_deposit']) / float(unit['loan_ammount']) < 1:
            print('frth cond')
            mdl=joblib.load("../research/loan_model_lr.pkl")
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
        form=ApprovalForm(request.POST)
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
    
    form=ApprovalForm()

    return render(request, 'myform/exform.html', {'form':form})