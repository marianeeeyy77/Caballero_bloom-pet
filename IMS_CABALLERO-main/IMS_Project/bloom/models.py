from django.db import models


class Pet(models.Model):
    pet_id = models.IntegerField(primary_key=True)
    pet_name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    owner_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.pet_name
