import numpy as np
import pandas as pd
from warnings import simplefilter
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
simplefilter(action='ignore', category=FutureWarning)
class ML():
    def __init__(self):
        self.rf = RandomForestClassifier(n_estimators = 1000, random_state = 1)
        data = pd.read_csv('heart.csv')
        y = data.target.values
        x_data = data.drop(['target'], axis=1)
        x_data = x_data.drop(['age'], axis=1)
        x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data)).values
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
        rf = RandomForestClassifier(n_estimators=1000, random_state=1)
        rf.fit(x_train, y_train)
        self.rf = rf
    def predict(self, x_test):
        return self.rf.predict(x_test)

algo = ML()