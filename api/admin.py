from django.contrib import admin

from api.models import Crew, MotherShip, Ship

admin.site.register(MotherShip)
admin.site.register(Ship)
admin.site.register(Crew)
