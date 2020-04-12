import pyproj
from functools import partial
from shapely.geometry import Point
from shapely.ops import transform
import warnings


class GeoHelper:

    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def lat_lng_to_utm(lat_lng_geom):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            project = partial(
                pyproj.transform,
                pyproj.Proj(init='epsg:4326'),  # source coordinate system
                pyproj.Proj(init='epsg:3857')   # destination coordinate system
            )
            utm_geom = transform(project, lat_lng_geom)
        return utm_geom

    @staticmethod
    def utm_to_lat_lng(utm_geom):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            project = partial(
                pyproj.transform,
                pyproj.Proj(init='epsg:3857'),  # source coordinate system
                pyproj.Proj(init='epsg:4326')   # destination coordinate system
            )
            lat_lng_geom = transform(project, utm_geom)
        return lat_lng_geom

    def generate_isocota(self, point, radius):
        utm_radius = self.lat_lng_to_utm(point).buffer(radius)
        lat_lng_radius = self.utm_to_lat_lng(utm_radius)
        return lat_lng_radius

    def get_isocota(self, lat, lng):
        pt = Point(lng, lat)
        return self.generate_isocota(pt, self.radius)
