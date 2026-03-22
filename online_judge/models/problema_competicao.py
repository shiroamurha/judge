from django.db import models
from online_judge.models.base_model import BaseModel
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator



class ProblemaCompeticao(BaseModel):

    label = models.CharField(
        validators=[MinValueValidator(1)],
        max_length=5
    )

    pontos = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ],
        default=100
    )
    
    ordem = models.IntegerField(
        validators=[MinValueValidator(1)]
    )



    def __str__(self):
        return self.label