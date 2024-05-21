import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data = pd.DataFrame({
    'income': [60,85.5,64.8,61.5,87,110.1,108,82.8,69,93,51,81,75,52.8,64.8,43.2,84,49.2],
    'lotSize' : [18.4,16.8,21.6,20.8,23.6,19.2,17.6,22.4,20,20.8,22,20,19.6,20.8,17.2,20.4,17.6,17.6],
    'owner' : [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0]

})
print(data.head())

X = data.drop(['owner'], axis=1)
y = data['owner']

k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

new_data = pd.DataFrame({
    'income': [70],
    'lotSize': [35]
})

prediction = model.predict(new_data)
print("Predicted owner :", prediction)