from django.http import Http404

from api.models import MotherShip, Ship, Crew
from api.utils.exception_handlers import MethodNotAllowed
from django.shortcuts import get_object_or_404

def create_mother_ship():
    mother_ship = MotherShip.objects.create()
    mother_ship.save()
    for i in range(3):
        create_ship(mother_ship=mother_ship)
    return mother_ship

def create_ship(mother_ship):
    ship = Ship.objects.create(mother_ship=mother_ship)
    if ship.clean():
        ship.save()
        for i in range(3):
            create_crew(ship=ship)
    return ship

def create_crew(ship, name=None):
    crew = Crew.objects.create(ship=ship, name=name)
    if crew.clean():
        crew.save()
        return crew

def validate_mothership_vacancy(mother_ship_id, count):
    try:
        mother_ship = MotherShip.objects.get(id=mother_ship_id)
    except MotherShip.DoesNotExist:
        raise Http404("No Mothership matches the given query.")
    if not mother_ship.vacancy >= count:
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
