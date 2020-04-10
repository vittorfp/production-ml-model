import numpy as np
import pandas as pd
from collections import Counter
from shapely.geometry import Point
from .geoprocessing_helper import GeoHelper

class DataRepository:

    types = {
        'faculdades', 'escolas', 'ponto_de_onibus', 'concorrentes__pequeno_varejista', 'concorrentes__grandes_redes',
        'minhas_lojas', 'agencia_bancaria', 'padaria', 'acougue', 'restaurante', 'correio', 'loterica'
    }

    def __init__(self):
        self.data = pd.read_csv('./app/resources/pois.csv')

    def get_points_inside_isocota(self, isocota):
        min_lng, min_lat, max_lng, max_lat = isocota.bounds

        # cuts the square area
        mask = (
            self.data.latitude.between(min_lat, max_lat) &
            self.data.longitude.between(min_lng, max_lng)
        )

        # then cuts the circle area
        return pd.DataFrame([
            row
            for row in self.data.loc[mask].itertuples()
            if Point(row.longitude, row.latitude).within(isocota)
        ]).drop(columns=['Index'])

    def get_points_count(self, isocota):
        points = self.get_points_inside_isocota(isocota)
        counter = Counter(points.tipo_POI)
        df_data = pd.DataFrame(counter, index=[0]).fillna(0)

        for i in self.types:
            if i not in df_data:
                df_data[i] = 0

        return df_data