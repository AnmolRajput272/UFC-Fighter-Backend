from django.db import models

class weight_division(models.Model):
    weight = models.IntegerField()

class ufc_fighter(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    rank = models.IntegerField(null=True, default=None)
    is_champ = models.BooleanField(default=True)
    next_opponent = models.CharField(max_length=100, null=True, blank=False)
    weight_division = models.ForeignKey(weight_division, null=True, on_delete=models.CASCADE, related_name="fighters")

    def __repr__(self) -> str:
        return f"{self.name}"
    