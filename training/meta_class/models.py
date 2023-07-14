from django.db import models
from django.db.models.constraints import CheckConstraint, UniqueConstraint
from django.db.models import Q, F

# Create your models here.

"""
    ******* UniqueConstraint *******
    garante que os valores dos campos 
    especificados sejam únicos
"""

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    note = models.IntegerField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    class Meta:
        db_table = "Person"
        ordering = ['-age', 'name']
        verbose_name="Person"
        verbose_name_plural = "Persons"
        unique_together = ['name'] # or [['name', 'age'], ['name']] etc...
        #abstract = True # Informa que esse classe serve somente como abstract para outras Models
        # permissions = [
        #     ('change_all', 'change_all')
        # ]
        default_permissions = ('add', 'change', 'delete', 'view')
        indexes = [models.Index(fields=['name'])]
        constraints = [
            CheckConstraint(check=Q(age__gte=1), name='age_not_support'),
            CheckConstraint(check=Q(end_date__gt=F('start_date')), name='start_end_dates')
        ]

    def __str__(self) -> str:
        return f"Nome: {self.name} with age {self.age}"