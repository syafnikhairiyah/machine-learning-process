
#import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as scs
import matplotlib.pyplot as plt
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler, SMOTE
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import model_selection


from sklearn.svm import SVC
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

#Load dataset
df = pd.read_csv('datasusu.csv')
new_df = df.replace("medium", "high")

#handling duplicate
duplicate_status = new_df.duplicated()
data = new_df.drop_duplicates()
data.shape

#labelling data
labelencoder = LabelEncoder()
new_data = data.copy()
new_data["Grade"] = labelencoder.fit_transform(new_data["Grade"])

new_data.head()

# define x and y
x = new_data.drop(columns='Grade')
y = new_data['Grade']

#oversampling
from imblearn.over_sampling import SMOTE
sample = SMOTE(random_state=0)
x,y = sample.fit_resample(x,y)
y.value_counts()

# train dan test data split
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2, random_state=7)

# Scaling untuk X_train dan X_test
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

svm = SVC(kernel='sigmoid')
svm.fit(x_train,y_train)


def predict_grade(data):
    y_db = svm.predict([[
        data.pH,
        data.Temprature,
        data.Taste,
        data.Odor,
        data.Fat,
        data.Turbidity,
        data.Colour
        ]])
    if y_db == 1:
        return "High"
    elif y_db == 0:
        return "Low"
    else:
        return "Unknown"
