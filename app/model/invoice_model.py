import pickle


class InvoiceModel:

    def __init__(self, file):
        self.model = pickle.load(open(file, 'rb'))

    def predict(self, x):
        return self.model.predict(x)
