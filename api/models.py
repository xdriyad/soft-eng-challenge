import names
from django.db import models
from django.utils import timezone
from api.utils.exception_handlers import MethodNotAllowed

class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MotherShip(BaseModel):
    capacity = models.IntegerField(default=9)

    def __str__(self):
        return str(self.id)
    @property
    def vacancy(self):
        return self.capacity - Ship.objects.filter(mother_ship=self).count()

    @property
    def has_vacancy(self):
        return self.capacity > Ship.objects.filter(mother_ship=self).count()


class Ship(BaseModel):
    capacity = models.IntegerField(default=5)
    mother_ship = models.ForeignKey(MotherShip, on_delete=models.CASCADE)

    def clean(self):
        if not self.mother_ship.has_vacancy:
            raise MethodNotAllowed(detail="Cannot create a ship, the MotherShip has no capacity")
        return True

    @property
    def has_vacancy(self):
        return self.capacity > Crew.objects.filter(ship=self.id).count()

    def __str__(self):
        return str(self.id)


class Crew(BaseModel):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    name = models.CharField(default=names.get_first_name, max_length=128)

    def clean(self):
        if not self.ship.has_vacancy:
            raise MethodNotAllowed(detail="Cannot create a crew, ship has no capacity")
        return True

    def __str__(self):
        return '{} : {}'.format(self.id, self.name)


