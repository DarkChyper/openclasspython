from classes.position import *


class Zone:
    """
    A rectangular geographic area bounded by two corners. The corners can
    be top-left and bottom right, or top-right and bottom-left so you should be
    careful when computing the distances between them.
    """

    ZONES = []
    # The width and height of the zones that will be added to ZONES. Here, we
    # choose square zones but we could just as well use rectangular shapes.

    # Attributs de classe (constante si hors de la classe) car on fait
    # cls.WIDTH_DEGREES
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1 # degrees of longitude
    HEIGHT_DEGREES = 1 # degrees of latitude

    # S'il y a un attribut d'instance, il va dans __init__

    EARTH_RADIUS_KILOMETERS = 6371

    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = []

    @property
    def population(self):
        """Number of inhabitants in the zone"""
        return len(self.inhabitants)

    @property
    def width(self):
        """Zone width, in kilometers"""
        # Note that here we access the class attribute via "self" and it
        # doesn't make any difference
        return abs(self.corner1.longitude - self.corner2.longitude) * self.EARTH_RADIUS_KILOMETERS

    @property
    def height(self):
        """Zone height, in kilometers"""
        # Note that here we access the class attribute via "self" and it
        # doesn't make any difference
        return abs(self.corner1.latitude - self.corner2.latitude) * self.EARTH_RADIUS_KILOMETERS

    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)

    def population_density(self):
        """Population density of the zone, (people/km²)"""
        # Note that this will crash with a ZeroDivisionError if the zone has 0
        # area, but it should really not happen
        return self.population / self.area()

    def area(self):
        """Compute the zone area, in square kilometers"""
        return self.height * self.width

    def average_agreeableness(self):
        if not self.inhabitants:
            return 0
        return sum([inhabitant.agreeableness for inhabitant in self.inhabitants]) / self.population

    def contains(self, position):
        """Return True if the zone contains this position"""
        return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
            position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
            position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
            position.latitude < max(self.corner1.latitude, self.corner2.latitude)

    @classmethod
    def find_zone_that_contains(cls, position):
        if not cls.ZONES:
            # Initialize zones automatically if necessary
            cls._initialize_zones()

        # Compute the index in the ZONES array that contains the given position
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES)/ cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES)/ cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES) # 180-(-180) / 1
        zone_index = latitude_index * longitude_bins + longitude_index

        # Just checking that the index is correct
        zone = cls.ZONES[zone_index]
        assert zone.contains(position)

        return zone

    @classmethod
    def _initialize_zones(cls):
        # Note that this method is "private": we prefix the method name with "_".
        cls.ZONES = []
        for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, latitude)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)

