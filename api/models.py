import names
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MotherShip(BaseModel):
    capacity = models.IntegerField(default=9)

    @property
    def vacancy(self):
        return self.capacity - Ship.objects.filter(mother_ship=self).count()

    @property
    def has_vacancy(self):
        return self.capacity > Ship.objects.filter(mother_ship=self).count()

    def __str__(self):
        return 'ID: {}'.format(self.id)


class Ship(BaseModel):
    capacity = models.IntegerField(default=5)
    mother_ship = models.ForeignKey(MotherShip, on_delete=models.CASCADE)

    @property
    def vacancy(self):
        return self.capacity - Crew.objects.filter(ship=self).count()

    @property
    def has_vacancy(self):
        return self.capacity > Crew.objects.filter(ship=self.id).count()

    def __str__(self):
        return 'ID: {}'.format(self.id)


class Crew(BaseModel):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    name = models.CharField(default=names.get_first_name, max_length=128)

    def __str__(self):
        return '{} : {}'.format(self.id, self.name)


