from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn import model_selection
import pickle

crop = pd.read_csv('Data/crop_recommendation.csv')

# Initializing empty lists to append all model's name and corresponding name
acc = []
model = []

features = crop[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']].values
target = crop['label'].values

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=10)

model.append(('rf',RandomForestClassifier(n_estimators = 55)))
model.append(('xg', XGBClassifier()))
model.append(('gb', GaussianNB()))

vot_soft = VotingClassifier(estimators=model, voting='soft')
vot_soft.fit(X_train, y_train)
y_pred = vot_soft.predict(X_test)

scores = model_selection.cross_val_score(vot_soft, features, target, cv=5, scoring='accuracy')
print("Accuracy: ", scores.mean())

score = accuracy_score(y_test, y_pred)
print("Voting Score % d" % score)

print(classification_report(y_test, y_pred))

score = cross_val_score(vot_soft, features, target, cv=5)

pkl_filename = 'recommendation.pkl'
Model_pkl = open(pkl_filename, 'wb')
pickle.dump(vot_soft, Model_pkl)
Model_pkl.close()
