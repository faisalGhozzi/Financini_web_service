from rest_framework import serializers
from .models import approvalsDl

class approvalDlSerializers(serializers.ModelSerializer):
    class Meta:
        model=approvalsDl
        fields='__all__'