import pickle


class InvoiceModel:

    def __init__(self):
        self.model = pickle.load(open('./app/model/model_campifarma.pickle', 'rb'))

    def predict(self, x):
        return self.model.predict(x)
