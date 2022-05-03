from api.models import MotherShip, Ship, Crew


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
