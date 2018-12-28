import math


class Position:

    def __init__(self, longitude_degrees, latitude_degrees):
        # We store the degree values, but we will be mostly using radians
        # because they are much more convenient for computation purposes.

        # assert : Lève une exception si renvoie False
        assert -180 <= longitude_degrees <= 180
        self.longitude_degrees = longitude_degrees

        assert -90 <= latitude_degrees <= 90
        self.latitude_degrees = latitude_degrees

    @property
    def longitude(self):
        """Longitude in radians"""
        return self.longitude_degrees * math.pi / 180

    @property
    def latitude(self):
        """Latitude in radians"""
        return self.latitude_degrees * math.pi / 180
