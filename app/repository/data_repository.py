import pandas as pd
from collections import Counter
from shapely.geometry import Point
from app.repository.postgres_configuration import PostgresConnection


class DataRepository:

    types = {
        'faculdades', 'escolas', 'ponto_de_onibus', 'concorrentes__pequeno_varejista', 'concorrentes__grandes_redes',
        'minhas_lojas', 'agencia_bancaria', 'padaria', 'acougue', 'restaurante', 'correio', 'loterica'
    }

    def __init__(self):
        self.db = PostgresConnection()

    def get_points_inside_isocota(self, isocota):
        min_lng, min_lat, max_lng, max_lat = isocota.bounds

        # cuts the square area
        points = self.get_nearby_points(min_lng, min_lat, max_lng, max_lat)

        # then cuts the circle area
        return pd.DataFrame([
            row
            for row in points
            if Point(row[2], row[1]).within(isocota)
        ], columns=['id', 'latitude', 'longitude', 'tipo_POI'])

    def get_points_count(self, isocota):
        points = self.get_points_inside_isocota(isocota)
        counter = Counter(points.tipo_POI)
        df_data = pd.DataFrame(counter, index=[0]).fillna(0)

        for i in self.types:
            if i not in df_data:
                df_data[i] = 0

        return df_data[sorted(df_data.columns)]

    def get_nearby_points(self, min_lng, min_lat, max_lng, max_lat):
        sql = f"""
            SELECT * 
            FROM points_of_interest
            WHERE 
                latitude BETWEEN {min_lat} AND {max_lat} AND
                longitude BETWEEN {min_lng} AND {max_lng}
        """
        return self.db.query(sql)
