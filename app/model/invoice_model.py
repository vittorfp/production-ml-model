import pickle
import numpy as np
from sklearn.pipeline import Pipeline


scale = pickle.load('scale.pkl')
lr = pickle.load('model.pkl')

model_pipeline = Pipeline([scale, lr])



class InvoiceModel:

    def __init__(self, lat, lon):
        # validate if the point is in Campinas

        # query the data

        self.X = np.array([])

    def predict(self):
        return model_pipeline.predict(self.X)
