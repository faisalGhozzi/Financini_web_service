from django.db import models

# Create your models here.
class approvals(models.Model):
    sct=models.CharField(max_length=15)
    capitaux_propres=models.FloatField(default=0)
    passifs_non_courant=models.FloatField(default=0)
    total_bilan=models.FloatField(default=0)
    stock=models.FloatField(default=0)
    creance_client=models.FloatField(default=0)
    actif_immobilier=models.FloatField(default=0)
    resultat_net=models.FloatField(default=0)
    chiffre_d_affaires=models.FloatField(default=0)

    def __str__(self):
        return self.sct