from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
#from django.core.validators import MinLengthValidator
from online_judge.models.teste import Teste


class Caso(Teste):

    ordem = models.IntegerField(
        default=1,
        unique=True,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )