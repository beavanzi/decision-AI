import pandas as pd

db = pd.read_csv('db/diabetes.csv')


class Dataset():
    qtt_total: int
    qtt_diab: int
    qtt_not_diab: int

    def __init__(self):
        self.age = db['Age']
        self.bmi = db['BMI']
        self.glucose = db['Glucose']
        self.insulin = db['Insulin']
        self.diab_pedigree = db['DiabetesPedigreeFunction']
        self.qtt_total = db.shape[0]
        self.qtt_diab = db.loc[self.has_diab()].shape[0]
        self.qtt_not_diab = self.qtt_total - self.qtt_diab

    def has_diab(self):
        return db['Outcome'] == 1

    def has_not_diab(self):
        return db['Outcome'] == 0

    def loc(self, cond):
        return db.loc[cond]

