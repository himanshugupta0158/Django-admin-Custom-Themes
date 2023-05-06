from django.db import models

# Create your models here.


INDIVIDUAL_STATUS = [
    ("MEMBER NOMINATED", "Member Nominated"),
    ("INDEPENDENT", "Independent")
]

# On 03/05/2023
class Individual(models.Model):
    ghana_card_id = models.CharField(max_length=30, unique=True)
    TIN_number = models.CharField(max_length=30, unique=True)
    name_of_individual = models.CharField(max_length=100)
    status = models.CharField(max_length=30,choices=INDIVIDUAL_STATUS)

    @property
    def individual_id(self):
        return self.id


    def __str__(self) -> str:
        return f"{self.name_of_individual} (id : {self.individual_id} | Ghana Card : {self.ghana_card_id} )"