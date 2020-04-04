from shapely.geometry import Point
from shapely.wkt import load


class CityChecker:

    def __init__(self, file):
        self.city_limits = load(file)

    def is_inside_city(self, lat, lon):
        point = Point(lat, lon)
        return self.city_limits.contains(point)
