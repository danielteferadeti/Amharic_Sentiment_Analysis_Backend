from django.db import models

# Create your models here.
class Crowdsource_Sentence(models.Model):
    sentence = models.CharField(max_length=300)
    classification = models.CharField(max_length=100)
    
    

    def __str__(self):
        return self.sentence