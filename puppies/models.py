from django.db import models

# Create your models here.


class Puppy(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_breed(self):
        return self.name + " belongs to " + self.breed + " breed."

    def __repr__(self):
        return self.name + " is added."
