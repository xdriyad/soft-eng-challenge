from django.http import Http404
from django.shortcuts import get_object_or_404

from api.models import Crew, MotherShip, Ship
from api.utils.exception_handlers import MethodNotAllowed


def create_mothership():
    mothership = MotherShip.objects.create()
    mothership.save()
    for i in range(3):
        create_ship(mothership=mothership)
    return mothership

def create_ship(mothership):
    if mothership.has_vacancy:
        ship = Ship.objects.create(mothership=mothership)
        for i in range(3):
            create_crew(ship=ship)
        return ship

def create_crew(ship, **kwargs):
    if not ship.has_vacancy:
        raise MethodNotAllowed(detail='Not enough vacancy in the Ship')
    return Crew.objects.create(ship=ship, **kwargs)


def validate_mothership_vacancy(mothership_id, count):
    try:
        mothership = MotherShip.objects.get(id=mothership_id)
    except MotherShip.DoesNotExist:
        raise Http404("No Mothership matches the given query.")
    if not mothership.vacancy >= count:
        raise MethodNotAllowed(detail='Not enough vacancy on MotherShip')


def swap_crew(from_ship_id, to_ship_id, name):
    from_ship = get_object_or_404(Ship, id=from_ship_id)
    to_ship = get_object_or_404(Ship, id=to_ship_id)
    if not to_ship.has_vacancy:
        raise MethodNotAllowed(detail='Not enough vacancy on ship to transfer crew')
    crew = get_object_or_404(Crew, ship=from_ship, name=name)
    crew.ship = to_ship
    crew.save()
    return crew
