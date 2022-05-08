from drf_yasg import openapi

ship_create_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'count': openapi.Schema(type=openapi.TYPE_INTEGER, default=3, description='How many ships?'),
        'mothership': openapi.Schema(type=openapi.TYPE_INTEGER, default=4, description='Mothership id'),
    })

crew_create_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, default='Jon', description='Name of the crew'),
        'ship': openapi.Schema(type=openapi.TYPE_INTEGER, default=4, description='Ship id'),
    })

crew_swap_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, default='Jon', description='Name of the crew'),
        'from_ship': openapi.Schema(type=openapi.TYPE_INTEGER, default=4, description='From Ship id'),
        'to_ship': openapi.Schema(type=openapi.TYPE_INTEGER, default=8, description='From Ship id'),
    })
