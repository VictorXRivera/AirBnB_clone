#!/usr/bin/python3
'''place: inherits from BaseModel'''


class Place (BaseModel):
    '''Place: stores description of places (empty)
    '''
    name = ''
    city_id = ''
    user_id = ''
    description = ''
    number_rooms = 0
    max_guest = 0
    price_by_height = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ()
