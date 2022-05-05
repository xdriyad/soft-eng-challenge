from django.http import Http404

from api.models import MotherShip, Ship, Crew
from api.utils.exception_handlers import MethodNotAllowed


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

def create_crew(ship):
    crew = Crew.objects.create(ship=ship)
    if crew.clean():
        crew.save()
        return crew

def validate_mothership_vacancy(mother_ship_id, count):
    try:
        mother_ship = MotherShip.objects.get(id=mother_ship_id)
    except MotherShip.DoesNotExist:
        raise Http404("No MotherShip matches the given query.")
    if not mother_ship.vacancy >= count:
        raise MethodNotAllowed(detail='Not enough vacancy on MotherShip')