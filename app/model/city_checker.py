from shapely.geometry import Point
from shapely.wkt import load


class CityChecker:

    def __init__(self, file):
        self.city_limits = load(open(file, 'r'))

    def is_inside(self, lat=None, lng=None):
        point = Point(lng, lat)
        return self.city_limits.contains(point)
